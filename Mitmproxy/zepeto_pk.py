from mitmproxy import ctx, http
from concurrent.futures import ThreadPoolExecutor
import json
import datetime
import time
import os
import copy
import requests
from debug_info import Log_info
import threading

TARGETID="YBE29I"
HEADURL="https://cdn.zepeto.cn/users/619375e7cc34fc6ca1f182e2/profile/619375ea89dbbe189a31435e.png"
HEADER_LIST = {}

class Modify:
    global logger
    logger = Log_info().main(__name__.split('.')[1])


    def __init__(self):
        # 线程池
        print("------启动线程-------")
   

    def request(self, flow):
        # print("已进入request")
    
        if "UsersInfoRequest" or "CounterRequest" in flow.request.url:
            print("userinfo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for k, v in flow.request.headers.items():
                print("%-30s: %s" % (k.upper(), v))
                HEADER_LIST[k.upper()] = v
            # print(HEADER_LIST)
         


        if flow.request.url.startswith("https://api-zepeto.kajicam.com/zepeto/activity/fashion/pk"):
            modified = int(round(time.time() * 1000))
            while 1:
                try:
                    # targetId为目标用户
                    data = {
                        "authToken":HEADER_LIST['AUTHORIZATION'],
                        "duid":HEADER_LIST['X-ZEPETO-DUID'],
                        "zzId":HEADER_LIST['hashCode'],
                        "targetId":TARGETID,
                        "userId":HEADER_LIST['userId'],
                        "nickName":HEADER_LIST['name'],
                        "headUrl":HEADURL,
                        "modified": modified
                    }
                    resp = requests.post("https://api-zepeto.kajicam.com/zepeto/activity/fashion/pk/api/pkCoin/helpTicket",data=data)
                    print(resp)
                    if resp['result']['code'] == "200":
                        return True
                    else:
                        # code返回300为评审券不足
                        break;

                except Exception as e:
                    logger(e)
                    break

    def response(self, flow):
        if "UsersInfoRequest" in flow.request.url:
            response = json.loads(flow.response.get_text())
            # print(response)
            HEADER_LIST['hashCode'] = response['users']['hashCode']
            HEADER_LIST['userId'] = response['users']['userId']
            HEADER_LIST['name'] = response['users']['name']
            # print(HEADER_LIST)
            # pass

addons = [
    Modify()
]
