import requests

url = "https://cn.bing.com/ttranslatev3?isVertical=1&&IG=F943110341A44203A435A460E25E17EF&IID=translator.5026"
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-type": "application/x-www-form-urlencoded",
    "ect": "4g",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Microsoft Edge\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"142.0.3595.94\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"142.0.7444.176\", \"Microsoft Edge\";v=\"142.0.3595.94\", \"Not_A Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-ms-gec": "FD5D38132ADF3D61B70CB8D7165FFF0AD783899035D1D50BDE381F801B79D716",
    "sec-ms-gec-version": "1-142.0.3595.94",
    "x-client-data": "eyIxIjoiMTgiLCIyIjoiMSIsIjMiOiIwIiwiNCI6Ii0zMzQyNjAwODA3MjYzMTE2MTgxIiwiNiI6InN0YWJsZSIsIjkiOiJkZXNrdG9wIn0=",
    "x-edge-shopping-flag": "1",
    "cookie": "MUID=2B30F401BF9663A60185E264BE0F6205; MUIDB=2B30F401BF9663A60185E264BE0F6205; SRCHD=AF=ANNTA1; SRCHUID=V=2&GUID=2A3589F03E7441E3AEEE03B628E452A7&dmnchg=1; MUIDV=NU=1; MUIDB=2B30F401BF9663A60185E264BE0F6205; _UR=QS=0&TQS=0&Pn=0; BFBUSR=BFBHP=0; MMCASM=ID=6F8E10E052914B22B5830CA99897BFA8; _clck=szp6z5%5E2%5Eg0h%5E0%5E2116; _uetvid=e60740d0a64511f0bec4bf4ee31fc94d; ANON=A=BA082C6BA13B32D6CCBB1D8DFFFFFFFF; USRLOC=HS=1&ELOC=LAT=39.99467086791992|LON=116.2906265258789|N=%E5%8C%97%E4%BA%AC%EF%BC%8C%E5%8C%97%E4%BA%AC%E5%B8%82|ELT=1|&BID=MjUxMTI4MjM0MjU4X2EzYjE0ZjM2NWVkNGU4MTE0NzdjN2Y1ODllZTFkNGY5ZTg1ZjhiOTQ3NDg3MDdiMDM2MGZmZDUxZTk4Yzk3MDY=; _tarLang=default=zh-Hans; _TTSS_OUT=hist=WyJlbiIsInpoLUhhbnMiXQ==; btstkn=YSLrRWrTvKTMnbPYBSZ3ni%252BzMIlyBpBG%252BiTEvqTggWM44yUBgSwv8uTMHgkhvK1xdifwCTacNhK0Nk1pUiWt%252FcpWuaspTvqyMdc%252FOjjlPoI%253D; _TTSS_IN=hist=WyJ6aC1IYW5zIiwiZnIiLCJlbiIsImF1dG8tZGV0ZWN0Il0=&isADRU=0; GC=OHshzyzIHLHjzPZvfnclTJ38I2tHItnVmqEsBQiEu3dzD7EW2gcXlOLog5wj2CNQ2PgeAU8xd1hIfCXqx8bEcg; _RwBf=mta=0&rc=200&rb=200&rg=0&pc=200&mtu=0&rbb=0.0&clo=0&v=3&l=2025-11-28T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=-62135539200&rwflt=-62135539200&rwaul2=0&g=&o=0&p=MSAAUTOENROLL&c=MR000T&t=4104&s=2023-12-16T12:36:22.7295196+00:00&ts=2025-11-28T12:13:19.5516025+00:00&rwred=0&wls=0&wlb=0&wle=1&ccp=2&cpt=0&lka=0&lkt=0&aad=0&TH=&cid=0&gb=2025w18_u&e=6L_Midxh8d2UjGetBriX5HmuhYH56oDBAd_6KUTrUZGJ0zAbck-AK9LOe32Jq8kCSE9KSjAtxp7sXI9GTMrltw; _EDGE_S=ui=en-us&SID=12A6A3FCA1EB648702FCB54EA0A865C2; SNRHOP=I=&TS=; _SS=PC=WSBQUF&SID=12A6A3FCA1EB648702FCB54EA0A865C2; CortanaAppUID=4925FB7A69AEBA34461D6ACF51AA70E8; SRCHHPGUSR=SRCHLANG=en&PV=10.0.0&BZA=0&PREFCOL=0&BRW=XW&BRH=M&CW=1912&CH=962&SCW=1897&SCH=3247&DPR=1.0&UTC=480&B=0&EXLTT=31&HV=1764344860&HVE=CfDJ8BJecyNyfxpMtsfDoM3OqQuJxrIjgxsH-2P74GMwpdiM1ErGKDNOyEuejK8jH8YUtTmP1rDQUe6QQArcCWEM4JtziBPJWXwJoYb2EZ56sejo-2xfnP_AIHTjGhlp5tpZ-8JQ4lbx5SGamNgxd___LqkuHxqcCgoF9jy6TUTog7QCucB9kTa_wu4rTBY1kc28mQ&PRVCW=1912&PRVCH=962; SRCHUSR=DOB=20251112&DS=1",
    "Referer": "https://cn.bing.com/translator?ref=TThis&text=&from=en&to=zh-Hans"
}
cookies = {
    "MUID": "2B30F401BF9663A60185E264BE0F6205",
    "MUIDB": "2B30F401BF9663A60185E264BE0F6205",
    "SRCHD": "AF=ANNTA1",
    "SRCHUID": "V=2&GUID=2A3589F03E7441E3AEEE03B628E452A7&dmnchg=1",
    "MUIDV": "NU=1",
    "_UR": "QS=0&TQS=0&Pn=0",
    "BFBUSR": "BFBHP=0",
    "MMCASM": "ID=6F8E10E052914B22B5830CA99897BFA8",
    "_clck": "szp6z5%5E2%5Eg0h%5E0%5E2116",
    "_uetvid": "e60740d0a64511f0bec4bf4ee31fc94d",
    "ANON": "A=BA082C6BA13B32D6CCBB1D8DFFFFFFFF",
    "USRLOC": "HS=1&ELOC=LAT=39.99467086791992|LON=116.2906265258789|N=%E5%8C%97%E4%BA%AC%EF%BC%8C%E5%8C%97%E4%BA%AC%E5%B8%82|ELT=1|&BID=MjUxMTI4MjM0MjU4X2EzYjE0ZjM2NWVkNGU4MTE0NzdjN2Y1ODllZTFkNGY5ZTg1ZjhiOTQ3NDg3MDdiMDM2MGZmZDUxZTk4Yzk3MDY=",
    "_tarLang": "default=zh-Hans",
    "_TTSS_OUT": "hist=WyJlbiIsInpoLUhhbnMiXQ==",
    "btstkn": "YSLrRWrTvKTMnbPYBSZ3ni%252BzMIlyBpBG%252BiTEvqTggWM44yUBgSwv8uTMHgkhvK1xdifwCTacNhK0Nk1pUiWt%252FcpWuaspTvqyMdc%252FOjjlPoI%253D",
    "_TTSS_IN": "hist=WyJ6aC1IYW5zIiwiZnIiLCJlbiIsImF1dG8tZGV0ZWN0Il0=&isADRU=0",
    "GC": "OHshzyzIHLHjzPZvfnclTJ38I2tHItnVmqEsBQiEu3dzD7EW2gcXlOLog5wj2CNQ2PgeAU8xd1hIfCXqx8bEcg",
    "_RwBf": "mta=0&rc=200&rb=200&rg=0&pc=200&mtu=0&rbb=0.0&clo=0&v=3&l=2025-11-28T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=-62135539200&rwflt=-62135539200&rwaul2=0&g=&o=0&p=MSAAUTOENROLL&c=MR000T&t=4104&s=2023-12-16T12:36:22.7295196+00:00&ts=2025-11-28T12:13:19.5516025+00:00&rwred=0&wls=0&wlb=0&wle=1&ccp=2&cpt=0&lka=0&lkt=0&aad=0&TH=&cid=0&gb=2025w18_u&e=6L_Midxh8d2UjGetBriX5HmuhYH56oDBAd_6KUTrUZGJ0zAbck-AK9LOe32Jq8kCSE9KSjAtxp7sXI9GTMrltw",
    "_EDGE_S": "ui=en-us&SID=12A6A3FCA1EB648702FCB54EA0A865C2",
    "SNRHOP": "I=&TS=",
    "_SS": "PC=WSBQUF&SID=12A6A3FCA1EB648702FCB54EA0A865C2",
    "CortanaAppUID": "4925FB7A69AEBA34461D6ACF51AA70E8",
    "SRCHHPGUSR": "SRCHLANG=en&PV=10.0.0&BZA=0&PREFCOL=0&BRW=XW&BRH=M&CW=1912&CH=962&SCW=1897&SCH=3247&DPR=1.0&UTC=480&B=0&EXLTT=31&HV=1764344860&HVE=CfDJ8BJecyNyfxpMtsfDoM3OqQuJxrIjgxsH-2P74GMwpdiM1ErGKDNOyEuejK8jH8YUtTmP1rDQUe6QQArcCWEM4JtziBPJWXwJoYb2EZ56sejo-2xfnP_AIHTjGhlp5tpZ-8JQ4lbx5SGamNgxd___LqkuHxqcCgoF9jy6TUTog7QCucB9kTa_wu4rTBY1kc28mQ&PRVCW=1912&PRVCH=962",
    "SRCHUSR": "DOB=20251112&DS=1"
}
data = 'fromLang=en&to=zh-Hans&text=jack%0A%0A&tryFetchingGenderDebiasedTranslatio ns=true&token=4F5tprLYLplF2E_g_4D-0swaZvJkbfkb&key=1764344858538'

response = requests.post(url, headers=headers, cookies=cookies, data=data)
print(response.status_code)
print(response.text)