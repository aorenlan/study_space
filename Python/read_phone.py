# -*- coding: utf-8 -*-
from os import times
import requests
import json
import urllib.parse
import time

bear_token = ""
auth_token = ""
user_id = ""
hash_code = ""
profile_pic = ""
name = ""
encode_token = ""
last_count = 0


def read_phone_number():
    with open("phone_list.txt", "r", encoding="utf-8") as f:  # 打开文件
        data = f.read()  # 读取文件
    # print(data)
    return data


def cut_phone(data):
    phone_set = set()
    # print(data.split("\n"))
    for i in data.split("\n"):
        print(i.split()[0])
        phone_set.add(i.split()[0])
    return phone_set


def get_auth(phone):
    global bear_token, user_id, auth_token, encode_token
    header = {"Accept": r"*/*",
              "Content-Type": r"application/json; charset=UTF-8",
              "X-ZEPETO-DUID": "D3F4A802-0FD2-41D6-BCB3-28A014E81304",
              "Accept-Encoding": "gzip, deflate, br",
              "User-Agent": "ios.zepeto_cn/3.8.3 (ios; U; iOS 14.1; zh-Hans-CN; occ-CN; iPhone XS Max);ZEPETO",
              "Connection": "keep-alive",
              #   "Content-Length":"62",
              "Host": "napi.zepeto.cn"
              }
    data = {
        "userId": phone,
        "password": "a1111111"
    }
    re = requests.post(
        "https://napi.zepeto.cn/AuthenticationRequest_v2", headers=header, data=json.dumps(data)).text
    re_json = json.loads(re)
    auth_token = re_json['authToken']
    user_id = re_json['userId']
    bear_token = "Bearer "+str(auth_token)
    encode_token = urllib.parse.quote(auth_token)


def get_user_info():
    global profile_pic, name, hash_code

    header = {"Accept": r"*/*",
              "Content-Type": r"application/json; charset=UTF-8",
              "X-ZEPETO-DUID": "D3F4A802-0FD2-41D6-BCB3-28A014E81304",
              "Accept-Encoding": "gzip, deflate, br",
              "User-Agent": "ios.zepeto_cn/3.8.3 (ios; U; iOS 14.1; zh-Hans-CN; occ-CN; iPhone XS Max);ZEPETO",
              "Connection": "keep-alive",
              #   "Content-Length":"62",
              "Host": "napi.zepeto.cn",
              "Authorization": bear_token
              }
    data = {"userIds": [user_id]}
    re = requests.post(
        "https://napi.zepeto.cn/UsersInfoRequest", headers=header, data=json.dumps(data)).text
    re_json = json.loads(re)
    print(re_json)
    user_info = re_json['users'][0]
    hash_code = user_info['hashCode']
    profile_pic = user_info['profilePic']


def get_ticket():
    print(hash_code)
    global last_count
    re = requests.get(
        "https://api-zepeto.kajicam.com/zepeto/activity/fashion/pk/api/pkCoin/getTickets?zzId="+hash_code+"").text
    re_json = json.loads(re)
    last_count = int(re_json['result'])
    print(last_count)


def help_ticket():
    for i in range(last_count):
        re = requests.post(
            "https://api-zepeto.kajicam.com/zepeto/activity/fashion/pk/api/pkCoin/helpTicket?authToken="+encode_token+"&duid=6e7492c1-7734-4528-8b52-f68eb684425a&zzId="+hash_code+"&targetId=VGD1ZV&userId="+user_id+"&nickName="+name+"&headUrl="+profile_pic).text
        re_json = json.loads(re)
        print(re_json)
        time.sleep(1)

def total():
    phone_data = read_phone_number()
    phone_list = cut_phone(phone_data)
    for i in phone_list:
        # print (i)
        get_auth(str(i))
        get_user_info()
        get_ticket()
        help_ticket()
    bear_token = ""
    auth_token = ""
    user_id = ""
    hash_code = ""
    profile_pic = ""
    name = ""
    encode_token = ""
    last_count = 0

total()