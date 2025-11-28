#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 Node.js fetch 代码批量转成 Python-requests 代码
读取文件 → 写入文件（或 stdout）
"""
import re
import json
import sys
from pathlib import Path

# ---------- 正则 ----------
FETCH_RE = re.compile(
    r'fetch\s*\(\s*["\'](?P<url>.*?)["\']'
    r'(?P<opt>,\s*\{[\s\S]*?\})\s*\);?',
    re.MULTILINE | re.DOTALL
)
HEADERS_RE = re.compile(r'"headers"\s*:\s*(\{[\s\S]*?\})')
# 1. 先粗抓 "body": 开始 到 行尾逗号 或 下一个顶层 } 之前
BODY_RE = re.compile(
    r'"body"\s*:\s*('
    r'null|'                     # null
    r'"(?:\\.|[^"\\])*"|'        # 双引号字符串（支持 \" 转义）
    r"'(?:\\.|[^'\\])*'|"        # 单引号字符串（支持 \' 转义）
    r'`(?:\\.|[^`\\])*`|'        # 模板字符串
    r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'  # 最简嵌套{}（支持一级嵌套）
    r')',
    re.MULTILINE | re.DOTALL
)
METHOD_RE  = re.compile(r'"method"\s*:\s*["\'](.*?)["\']')
COOKIE_RE  = re.compile(r'"cookie"\s*:\s*["\'](.*?)["\']')

# ---------- 工具 ----------
def js_obj_to_py_dict(js_obj: str) -> dict:
    s = re.sub(r'([{,])\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*:', r'\1"\2":', js_obj)
    s = s.replace("'", '"').strip().rstrip(';')
    try:
        return json.loads(s)
    except Exception as e:
        print('⚠️  解析 JS 对象失败，返回空 dict：', e, file=sys.stderr)
        return {}

def cookie_str_to_dict(cookie: str) -> dict:
    return {kv.split('=', 1)[0].strip(): kv.split('=', 1)[1].strip()
            for kv in cookie.split(';') if '=' in kv}

def convert_one_fetch(code: str) -> str:
    m = FETCH_RE.search(code)
    if not m:
        return '# 未匹配到 fetch 调用'
    url = m.group('url')
    opt = m.group('opt')

    method = 'GET'
    if mm := METHOD_RE.search(opt):
        method = mm.group(1).upper()

    headers = {}
    if hm := HEADERS_RE.search(opt):
        headers = js_obj_to_py_dict(hm.group(1))

    cookies = {}
    if cm := COOKIE_RE.search(opt):
        cookies = cookie_str_to_dict(cm.group(1))

    json_data = None
    data = None
    if bm := BODY_RE.search(opt):
        raw = bm.group(1).strip()
        if raw == 'null':
            pass
        elif raw.startswith('"') and raw.endswith('"'):
            # 去掉两端引号，再解转义
            json_str = raw[1:-1].encode('utf-8').decode('unicode_escape')
            try:
                json_data = json.loads(json_str)
            except ValueError:
                data = json_str
        elif raw.startswith('{') and raw.endswith('}'):
            json_data = js_obj_to_py_dict(raw)
        else:
            data = raw

    lines = ['import requests', '', f'url = "{url}"']
    if headers:
        lines.append(f'headers = {json.dumps(headers, ensure_ascii=False, indent=4)}')
    if cookies:
        lines.append(f'cookies = {json.dumps(cookies, ensure_ascii=False, indent=4)}')
    if json_data is not None:
        lines.append(f'json_data = {json.dumps(json_data, ensure_ascii=False, indent=4)}')
    elif data is not None:
        lines.append(f'data = {repr(data)}')

    args = []
    if headers: args.append('headers=headers')
    if cookies: args.append('cookies=cookies')
    if json_data is not None:
        args.append('json=json_data')
    elif data is not None:
        args.append('data=data')

    lines.append('')
    lines.append(f"response = requests.{method.lower()}(url, {', '.join(args)})")
    lines.append('print(response.status_code)')
    lines.append('print(response.text)')
    return '\n'.join(lines)
# ---------- 主流程 ----------
def main():
    if len(sys.argv) < 2:
        print('用法：python fetch2requests.py  <input.js>  [output.py]')
        sys.exit(1)

    in_file  = Path(sys.argv[1])
    out_file = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    if not in_file.exists():
        print(f'错误：文件不存在 → {in_file}')
        sys.exit(2)

    src = in_file.read_text(encoding='utf-8')
    results = [convert_one_fetch(block.group(0))
               for block in FETCH_RE.finditer(src)]

    out_text = '\n\n'.join(results)
    if out_file:
        out_file.write_text(out_text, encoding='utf-8')
        print(f'✅ 已生成 → {out_file}')
    else:
        print(out_text)

if __name__ == '__main__':
    main()