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

TARGETID="VGD1ZV"
HEADURL="https://cdn.zepeto.cn/users/6170e59889dbbe36ea764bd0/profile/6170e59c62b1103df9e2926f.png"
HEADER_LIST = {}
USER = {}

class Modify:
    global logger
    logger = Log_info().main(__name__.split('.')[1])


    def __init__(self):
        # 线程池
        print("------启动线程-------")
   

    def request(self, flow):
        # print("已进入request")

        # IOS
        if "UsersInfoRequest" in flow.request.url:
            print("userinfo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for k, v in flow.request.headers.items():
                # print("%-30s: %s" % (k.upper(), v))
                HEADER_LIST[k.upper()] = v
            # print(HEADER_LIST)

        if "CounterRequest" in flow.request.url:
            print("CounterRequest ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for k, v in flow.request.headers.items():
                # print("%-30s: %s" % (k.upper(), v))
                HEADER_LIST[k.upper()] = v

        if "gapi.zepeto.cn/user/post" in flow.request.url:
            print("gapi.zepeto.cn/user/post ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            resp_json = json.loads(flow.request.get_text())
                # print("%-30s: %s" % (k.upper(), v))
            HEADER_LIST['userId'] = resp_json['userId']
         

        if "helpTicket" in flow.request.url:
            for i in range(10):
                print("-------------")
            print(flow.request.url)
            for i in range(10):
                print("-------------")
            print(HEADER_LIST)
            modified = int(round(time.time() * 1000))
            au = HEADER_LIST['AUTHORIZATION']
            while 1:
                # try:
                    # targetId为目标用户
                    data = {
                        "authToken":au,
                        "duid":HEADER_LIST['X-ZEPETO-DUID'],
                        "zzId":HEADER_LIST['hashCode'],
                        "targetId":TARGETID,
                        "userId":HEADER_LIST['userId'],
                        "nickName":HEADER_LIST['hashCode'],
                        "headUrl":HEADURL,
                        "modified":str(modified)
                    }
                    print(data)
                    res = requests.post("https://api-zepeto.kajicam.com/zepeto/activity/fashion/pk/api/pkCoin/helpTicket",data=data)
                    resp = json.loads(res.text)
                    print(resp)
                    time.sleep(0.1)
                    if resp['result']['code'] == 200:
                        print("success")
                        continue
                        
                    else:
                        # code返回300为评审券不足
                        break;

                # except Exception as e:
                #     logger(e)
                #     break

    def response(self, flow):
        if "UsersInfoRequest" in flow.request.url:
            response = json.loads(flow.response.get_text())
            print(response)
            try:
                HEADER_LIST['hashCode'] = response['users'][0]['hashCode']
                HEADER_LIST['userId'] = response['users'][0]['userId']
                HEADER_LIST['name'] = response['users'][0]['name']
            except Exception as e:
                print("error")
            for i in range(10):
                print("1111111111111111111")
            print(HEADER_LIST)
            # pass


addons = [
    Modify()
]
