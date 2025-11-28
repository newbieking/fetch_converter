import requests

url = "https://cm.bilibili.com/cm/api/fees/pc"
headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-type": "application/json",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Microsoft Edge\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "cookie": "buvid3=3EA24EF4-D309-2B94-7223-D4204B964BA830244infoc; b_nut=1758370030; _uuid=B4107E375-2AE5-FBBC-E214-6EAF81F107C3B31799infoc; buvid_fp=dd041eae79e6099d9403f2305503aef1; buvid4=91AE3D80-5BB3-C253-105F-5C6307D3CDA231022-025092020-yiSTobjEeGgjoffZbkizdQ%3D%3D; enable_web_push=DISABLE; SESSDATA=6009476d%2C1773939908%2C019ad%2A92CjAw82wxVKJ1IrYdQ_lhaEVS5BDDnPg2t3cui4zLUU_jPSjnwr4-pf3SB6f5Q9oq7_oSVnI4LW5KbXFEaFVZWXNpaEdoNy1La1hfWUlxZkFrT0c1WmI0elFBcVVXcG5wX19CRWpJeFdYYjN2dktQWFV3c19qaXRWbE8zUEVLXzhlMjRULVJqWmlRIIEC; bili_jct=8803d97c4a5051b5adc7ba255d0d34f7; DedeUserID=383823074; DedeUserID__ckMd5=f20c08ba74388a35; theme-tip-show=SHOWED; rpdid=0zbfAI6vhC|WUEAtyRB|EPH|3w1V0JDF; LIVE_BUVID=AUTO4017613685022674; theme-avatar-tip-show=SHOWED; home_feed_column=5; theme-switch-show=SHOWED; CURRENT_QUALITY=80; bp_t_offset_383823074=1138137655943364608; PVID=1; browser_resolution=1912-962; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjQ2MDE5MTMsImlhdCI6MTc2NDM0MjY1MywicGx0IjotMX0.YfzjW2RyD1ag3b1CGhdKg-kK0sWM42uZT55KMshI-qA; bili_ticket_expires=1764601853; CURRENT_FNVAL=2000; sid=elmbjwjp; b_lsid=75A101E5A_19ACB31DE60",
    "Referer": "https://www.bilibili.com/"
}
cookies = {
    "buvid3": "3EA24EF4-D309-2B94-7223-D4204B964BA830244infoc",
    "b_nut": "1758370030",
    "_uuid": "B4107E375-2AE5-FBBC-E214-6EAF81F107C3B31799infoc",
    "buvid_fp": "dd041eae79e6099d9403f2305503aef1",
    "buvid4": "91AE3D80-5BB3-C253-105F-5C6307D3CDA231022-025092020-yiSTobjEeGgjoffZbkizdQ%3D%3D",
    "enable_web_push": "DISABLE",
    "SESSDATA": "6009476d%2C1773939908%2C019ad%2A92CjAw82wxVKJ1IrYdQ_lhaEVS5BDDnPg2t3cui4zLUU_jPSjnwr4-pf3SB6f5Q9oq7_oSVnI4LW5KbXFEaFVZWXNpaEdoNy1La1hfWUlxZkFrT0c1WmI0elFBcVVXcG5wX19CRWpJeFdYYjN2dktQWFV3c19qaXRWbE8zUEVLXzhlMjRULVJqWmlRIIEC",
    "bili_jct": "8803d97c4a5051b5adc7ba255d0d34f7",
    "DedeUserID": "383823074",
    "DedeUserID__ckMd5": "f20c08ba74388a35",
    "theme-tip-show": "SHOWED",
    "rpdid": "0zbfAI6vhC|WUEAtyRB|EPH|3w1V0JDF",
    "LIVE_BUVID": "AUTO4017613685022674",
    "theme-avatar-tip-show": "SHOWED",
    "home_feed_column": "5",
    "theme-switch-show": "SHOWED",
    "CURRENT_QUALITY": "80",
    "bp_t_offset_383823074": "1138137655943364608",
    "PVID": "1",
    "browser_resolution": "1912-962",
    "bili_ticket": "eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjQ2MDE5MTMsImlhdCI6MTc2NDM0MjY1MywicGx0IjotMX0.YfzjW2RyD1ag3b1CGhdKg-kK0sWM42uZT55KMshI-qA",
    "bili_ticket_expires": "1764601853",
    "CURRENT_FNVAL": "2000",
    "sid": "elmbjwjp",
    "b_lsid": "75A101E5A_19ACB31DE60"
}
json_data = {
    "uploads": [
        {
            "src_id": 5614,
            "track_id": "",
            "up_mid": "",
            "ad_server": "bilibili",
            "is_ad": 1,
            "area": 0,
            "ad_cb": "CM+TlQsQruivRRjMnOLFAiDvCCgBMOKQ5wE47itCIDE3NjQzNDY4NzMyOTNxMTcyYTI1YTIzOGEyOXE2NTQ3SM2Lk9qsM1IM5YWL5ouJ546b5L6dWgbmlrDnloZiBuS4reWbvWgBcAB4gICAgKA5gAEBiAEAkgEnMjQwOTo4YTdjOjE0MTA6NzQwMTpmNTcxOjVkMDM6MjY5YToxN2I5oAH2FagBGLIBINHgfieVVzCDmfhU3nq53HnjwYIcq91LS01SUFmlSrdYugHSA2h0dHBzOi8vd3d3LmxpYmxpYi5hcnQvaW1hZ2UtbW9kZWw/YmZmPTQmc291cmNlaWQ9MDIwMTA2JmZyb21fYmNnPWJjZ18xMV82ODI3MzU3MjAmdHJhY2tfaWQ9cGJhZXMuZDA1ekhIOWxITHUzRkIzZFJGTVhYWGZPRklYb0szVlRtbHRCZjY0bF9COVZ5X0FrblB4Z1RSOUlyN3kweHktdGZ0anRqOENValJWT19YcEo2M2p4X3RSZUdHYmhMUTVJQ3RKV3dSVElFSTRtOWJqa25INDRsMGVQY3VMR3pEZ3RaRzNkS2FKb01mUnZaZ3pEaldPcU5Ud0c0T0hVZlpLVFFCZmI0WmJNRWJZeHJoUGNnWUZSaVhVbFc0QW5ORWJ6JmNhaWQ9X19DQUlEX18mcmVzb3VyY2VfaWQ9X19SRVNPVVJDRUlEX18mc291cmNlX2lkPTU2MTQmZnJvbV9zcG1pZD1fX0ZST01TUE1JRF9fJnJlcXVlc3RfaWQ9MTc2NDM0Njg3MzI5M3ExNzJhMjVhMjM4YTI5cTY1NDcmY3JlYXRpdmVfaWQ9NjgyNzM1NzIwJmxpbmtlZF9jcmVhdGl2ZV9pZD02ODMxODM2OTLCAQEx0gEA2AHKA+ABgJTr3APoAf/miNgD8AEA+AHaE4ACAogCAJICAJgCtrsBoAIiqALKB7ACAbgCAMAC0IYDyAKiAuoCAPgC7aUBiAMCkgMAqAMAsAMAuAMAyAMA0gO0AXsiMSI6IjY4MzE4MzY5MiIsIjEyIjoiNTYxNCIsIjEzIjoiMTY0NTM4OSIsIjE0IjoiMTA4MCIsIjE1IjoiMTA4MSIsIjE2IjoiMTY0NTM4OV8yMTIyOSIsIjIiOiIzNzg2ODUwIiwiMjQiOiIxIiwiMjUiOiIxMDM4IiwiMjYiOiIyMzExIiwiMyI6IjM3ODY4NTAiLCI0IjoiMCIsIjUiOiIwIiwiNiI6IjM3ODY4NTAifeADAOgDAPADAPoDBW90aGVyggQJbnVsbDpudWxsiAT2FZAEAJgEAaAEAaoEBwjM98s0EASqBAcIosePNBABuAQKwAQEygQA0AQA2AQA4gTwATU2LnsicHNJZCI6ODk5NTAsInYyIjoiSlp1Y3pkTXhYY2daRDhkNkRMdW5GcmZnc3RMMVlYT1R4cVFpdTE3ZDAzSFNNZF9JclpoWlZYSS1tdl90eGVsSU9lNndmekpuaVJtZlpOYXpEclZ5YmNSSWtiR2czVUR5TDlXcE1BRHJ0ZmFsTGNxV2pmLTBiQW43SUhyWUxXTEN5c3V5UDZzdHlWTjdHbVFYMHN3NU9NNWpyT3N0In07NjMueyJwc0lkIjo4OTg1NCwidjIiOiJCUjQifTs3MC57InBzSWQiOjgzNzM2LCJ2MiI6IkJLUkkifegEAPAEAPoE1wV7ImFjY2VsZXJhdGVfZmFjdG9yIjoxLjAsImFjY2VsZXJhdGVfaWQiOjAsImFkX3R5cGVfZml4IjoiY3BtIiwiYWR2dl9pbmZvIjoie1wiYWRqdXN0X2JlZm9yZV9jb3N0XCI6XCIyNTIyLjgzOFwiLFwiYWRqdXN0X3JhdGlvXCI6XCIwLjQ1MFwiLFwiYmFsYW5jZXJfaWRcIjowLFwiYmFsYW5jZXJfcmF0aW9cIjpcIjAuMDAwXCIsXCJjaGFyZ2VfZXhwX2tleV9kZXB0aFwiOlwiXCIsXCJjaGFyZ2VfZXhwX2tleV9saWdodFwiOlwiX2ZseV9jcGFfb25saW5lX2NoYXJnZThcIixcImNvc3RfZGlmZlwiOlwiLTEzODcuNTYxXCJ9IiwiYml6X3R5cGUiOjEyLCJiaXpfdHlwZV9maXgiOjMsImNwYSI6IntcImNwYV9sZXZlbFwiOjIsXCJjcGFfc2V0XCI6MjUwMDB9IiwiY3BhVGFyZ2V0VHlwZSI6NCwiZnJvbVRyYWNraWQiOiJ3ZWJfcGVnYXN1c18wLnJvdXRlci13ZWItcGVnYXN1cy0yMzU2MDYxLXdtMjk0LjE3NjQzNDY4NzMzMDIuNDciLCJpYWFfY2hlYXRfZmxvdyI6MCwiaW5uZXIiOjAsImlzX2NvbW1lcmNlIjoxLCJpc19vY3BjX2FudG91X29jcG0iOjAsIm1pbmlfZ2FtZV9pZCI6IiIsIm1pbmlfZ2FtZV9wb3NpdGlvbl9pZCI6IiIsIm1vZGVsU2NvcmUiOiJ7XCJjdHJcIjpcIjI0LjgwNzA0NVwiLFwiY3ZyX2wwXCI6XCIyOTAuMjcyNzk3XCIsXCJmaW5hbF9wY3RyXCI6XCIyNC44MDcwNDVcIixcImZpbmFsX3BjdnJcIjpcIjI5MC4yNzI3OTdcIn0iLCJ2aWRlb191cF9taWQiOjB9gAUAkAUjkAUzkAVIkAVVkAWOApAFmgKQBcACkAXCApAFxQKQBcsCkAXOApAF0wKQBdYCkAXYApAF2QKQBdoCkAXfApAF4QKQBeMCkAXlApAF8AKQBfECkAX1ApAF/wKQBYwDkAWNA5AFkwOQBZQDkAWYA5AFmQOQBZoDkAWbA5AFpQOQBacDkAW2A5AFtwOQBcADkAXBA5AFxAOQBc0DkAXgA5AF4QOQBeQDkAX1A5AF+AOQBf8DkAWHBJAFiQSQBckEkAXLBJAFzQSQBYMFkAWgBZAFqgWQBa8FkAWxBZAFtQWQBcYFkAXOBZAF0gWQBdMFkAXvBZAFowaQBaYGkAXaBpAF8AaQBfkGkAX/BpAFuweQBcIHkAX1B5AFvQiQBaERoAUAuAUEwAXNtmTIBQfgBQToBQDyBVhDQXdRQVNpb3d3RXdCRlZvclIxRlhmUnhyY1JsNnlLUlEyMEFRQnhHZFFBQWdEK1ZBZXNpa1VPZ0FheVNxMFdvQWVqd3hzVUNzQUVCd0FHb3d3SElBUVE9+AWskqtFgAb/k+vcA4gG6PDGxQI=",
            "event": "strict_show",
            "is_visible": 1,
            "idx": 1,
            "mid": "383823074",
            "client_version": "",
            "ts": 1764346875146,
            "resource_id": 5636,
            "load_ts": 1764346873536,
            "server_type": 1,
            "id": 0,
            "event_from": "",
            "request_id": "1764346873293q172a25a238a29q6547"
        }
    ]
}

response = requests.post(url, headers=headers, cookies=cookies, json=json_data)
print(response.status_code)
print(response.text)