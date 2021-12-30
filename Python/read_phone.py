# -*- coding: utf-8 -*-
import requests
import json

bear_token = ""
auth_token = ""
user_id = ""
hash_code = ""
profile_pic = ""
name = ""
encode_token = ""

def read_phone_number():
    with open("phone_list.txt", "r", encoding="utf-8") as f:  # 打开文件
        data = f.read()  # 读取文件
    # print(data)
    return data


def cut_phone(data):
    # print(data.split("\n"))
    for i in data.split("\n"):
        print(i.split()[0])


def get_auth(phone):
    global bear_token,user_id,auth_token
    header = {"Accept":r"*/*",
              "Content-Type": r"application/json; charset=UTF-8",
              "X-ZEPETO-DUID": "D3F4A802-0FD2-41D6-BCB3-28A014E81304",
              "Accept-Encoding": "gzip, deflate, br", 
              "User-Agent": "ios.zepeto_cn/3.8.3 (ios; U; iOS 14.1; zh-Hans-CN; occ-CN; iPhone XS Max);ZEPETO",
              "Connection":"keep-alive",
            #   "Content-Length":"62",
              "Host":"napi.zepeto.cn"
              }
    data = {
        "userId": phone,
        "password": "a1111111"
    }
    re = requests.post(
        "https://napi.zepeto.cn/AuthenticationRequest_v2", headers=header,data=json.dumps(data)).text
    re_json = json.loads(re)
    auth_token = re_json['authToken']
    user_id = re_json['userId']
    bear_token = "Bearer "+str(auth_token)

def get_user_info():
    global profile_pic,name,hash_code

    header = {"Accept":r"*/*",
              "Content-Type": r"application/json; charset=UTF-8",
              "X-ZEPETO-DUID": "D3F4A802-0FD2-41D6-BCB3-28A014E81304",
              "Accept-Encoding": "gzip, deflate, br", 
              "User-Agent": "ios.zepeto_cn/3.8.3 (ios; U; iOS 14.1; zh-Hans-CN; occ-CN; iPhone XS Max);ZEPETO",
              "Connection":"keep-alive",
            #   "Content-Length":"62",
              "Host":"napi.zepeto.cn",
              "Authorization":bear_token
              }
    data = {"userIds":[user_id]}
    re = requests.post(
        "https://napi.zepeto.cn/UsersInfoRequest", headers=header,data=json.dumps(data)).text
    re_json = json.loads(re)
    print(re_json)
    user_info = re_json['users'][0]
    hash_code = user_info['hashCode']
    profile_pic = user_info['profilePic']

def get_ticket():
    def get_user_info():
    global profile_pic,name,hash_code

    header = {"Accept":r"*/*",
              "Content-Type": r"application/json; charset=UTF-8",
              "X-ZEPETO-DUID": "D3F4A802-0FD2-41D6-BCB3-28A014E81304",
              "Accept-Encoding": "gzip, deflate, br", 
              "User-Agent": "ios.zepeto_cn/3.8.3 (ios; U; iOS 14.1; zh-Hans-CN; occ-CN; iPhone XS Max);ZEPETO",
              "Connection":"keep-alive",
            #   "Content-Length":"62",
              "Host":"napi.zepeto.cn",
              "Authorization":bear_token
              }
    data = {"userIds":[user_id]}
    re = requests.post(
        "https://napi.zepeto.cn/UsersInfoRequest", headers=header,data=json.dumps(data)).text
    re_json = json.loads(re)
    
get_auth("17050830546")
get_user_info()