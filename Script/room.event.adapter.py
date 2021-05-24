#!/usr/bin/env python
#-*-coding:utf-8

import json, requests, time, sys
uid = sys.argv[1]
now = int(time.time())
taskid = 'close_live_notify-11181341-%d' %now
pushid = 'close_live_notify-20200103-close_live_notify-11181341-%d' %now
payload = {"taskid":taskid,"timestamp":now,"type":"close_live_notify", "link":"inke://?pname=anchor_recall_activity", "pop_limit":"app"}  
body = {
    "android":{
         "aps":{
            "alert":{
                "body":"单场直播超过20min会获得更多的流量推荐哦～",
                "title":"小映@了你"
            }
        },
        "payload":json.dumps(payload),
    },
    "ios":{
        "aps":{
            "alert":{
                "body":"单场直播超过20min会获得更多的流量推荐哦～",
                "title":"小映@了你"
            }
        },
        "payload":json.dumps(payload)
    },
    "link":{
        "alert":{
            "body":"单场直播超过20min会获得更多的流量推荐哦～",
            "title":"小映@了你"
        },
        "category":"close_live_notify",
        "type":"close_live_notify",
        "taskid":taskid,
        "timestamp": now
    },
    "push_id":pushid,
    "ids":[
        uid
    ],
    "push_type":[
        1,
        2,
        3,
        4,
        8,
        9,
        10
    ],
    "app":"inke",
    "aggtype":"close_live_notify-20200617",
    "notify":1,
    "push_all":False,
    "channel_id":"close_live_notify",
    "push_target":"",
    "freq_priority":0,
    "vivo_field":{
        "classification":0
    }
}

host = 'http://10.128.0.187:6100/push/send'
resp = requests.post(host, data=json.dumps(body))
print resp.text

'''
host = 'http://127.1:10010/api/live/active/router?uid=457295'
body = {
    "business_line":"active",
    "action":"private_letter"
}

resp = requests.post(host, data=json.dumps(body))
print resp.text
'''
