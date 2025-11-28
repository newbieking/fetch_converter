fetch("https://cm.bilibili.com/cm/api/fees/pc", {
    "headers": {
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
        "cookie": "buvid3=3EA24EF4-D309-2B94-7223-D4204B964BA830244infoc; b_nut=1758370030; _uuid=B4107E375-2AE5-FBBC-E214-6EAF81F107C3B31799infoc; buvid_fp=dd041eae79e6099d9403f2305503aef1; buvid4=91AE3D80-5BB3-C253-105F-5C6307D3CDA231022-025092020-yiSTobjEeGgjoffZbkizdQ%3D%3D; enable_web_push=DISABLE; SESSDATA=6009476d%2C1773939908%2C019ad%2A92CjAw82wxVKJ1IrYdQ_lhaEVS5BDDnPg2t3cui4zLUU_jPSjnwr4-pf3SB6f5Q9oq7_oSVnI4LW5KbXFEaFVZWXNpaEdoNy1La1hfWUlxZkFrT0c1WmI0elFBcVVXcG5wX19CRWpJeFdYYjN2dktQWFV3c19qaXRWbE8zUEVLXzhlMjRULVJqWmlRIIEC; bili_jct=8803d97c4a5051b5adc7ba255d0d34f7; DedeUserID=383823074; DedeUserID__ckMd5=f20c08ba74388a35; theme-tip-show=SHOWED; rpdid=0zbfAI6vhC|WUEAtyRB|EPH|3w1V0JDF; LIVE_BUVID=AUTO4017613685022674; theme-avatar-tip-show=SHOWED; home_feed_column=5; theme-switch-show=SHOWED; CURRENT_QUALITY=80; bp_t_offset_383823074=1138137655943364608; PVID=1; browser_resolution=1912-962; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjQ2MDE5MTMsImlhdCI6MTc2NDM0MjY1MywicGx0IjotMX0.YfzjW2RyD1ag3b1CGhdKg-kK0sWM42uZT55KMshI-qA; bili_ticket_expires=1764601853; CURRENT_FNVAL=4048; b_lsid=BFC78BCB_19ACB2F1BF1",
        "Referer": "https://www.bilibili.com/"
    },
    "body": "{\"uploads\":[{\"src_id\":4697,\"track_id\":\"\",\"up_mid\":\"\",\"ad_server\":\"bilibili\",\"is_ad\":0,\"area\":1,\"ad_cb\":\"\",\"event\":\"show\",\"is_visible\":1,\"idx\":3,\"mid\":\"383823074\",\"client_version\":\"\",\"ts\":1764345463944,\"resource_id\":4694,\"load_ts\":1764345453834,\"server_type\":0,\"id\":1722159,\"event_from\":\"\",\"request_id\":\"1764345453838q17 2a24a58a35q7594\"}]}",
    "method": "POST"
}).then(r => t.json())
    .then(j => {
        console.log(j)
    });