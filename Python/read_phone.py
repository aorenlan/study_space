# -*- coding: utf-8 -*-
from asyncio import sleep
from os import times
import random
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
error_password = []
zepeto_id = ""
# target_id = "FPR4U5"
target_id = "888D3U"
error_change = ""
DUID = "D3F4A802-0FD2-41D6-BCB3-28A014E81303"


def read_phone_number():
    with open("phone_list_2.txt", "r", encoding="utf-8") as f:  # 打开文件
        data = f.read()  # 读取文件

    # print(data)
    return data


def cut_phone(data):
    # phone_set = set()
    phone_list = []
    # print(data.split("\n"))
    for i in data.split("\n"):
        print(i.split()[0])
        phone_list.append(i.split()[0])
    return phone_list


def get_auth(phone):
    global bear_token, user_id, auth_token, encode_token, zepeto_id,error_change
    header = {"Accept": r"*/*",
              "Content-Type": r"application/json; charset=UTF-8",
              "X-ZEPETO-DUID": DUID,
              "Accept-Encoding": "gzip, deflate, br",
              "User-Agent": "ios.zepeto_cn/3.8.3 (ios; U; iOS 14.1; zh-Hans-CN; occ-CN; iPhone XS);ZEPETO",
              "Connection": "keep-alive",
              #   "Content-Length":"62",
              "Host": "napi.zepeto.cn"
              }
    data = {
        "userId": phone,
        "password": "b1111111"
    }
    try:
        re = requests.post(
            "https://napi.zepeto.cn/AuthenticationRequest_v2", headers=header, data=json.dumps(data)).text

        time.sleep(2)
        if "authToken" not in re:
            error_password.append(phone)
            return 0
        re_json = json.loads(re)
        auth_token = re_json['authToken']
        user_id = re_json['userId']
        bear_token = "Bearer "+str(auth_token)
        encode_token = urllib.parse.quote(auth_token)
        error_change = phone
        # print(bear_token)
    except Exception as e:
        print(e)


def get_user_info():
    global profile_pic, name, hash_code, zepeto_id

    header = {"Accept": r"*/*",
              "Content-Type": r"application/json; charset=UTF-8",
              "X-ZEPETO-DUID": DUID,
              "Accept-Encoding": "gzip, deflate, br",
              "User-Agent": "ios.zepeto_cn/3.8.3 (ios; U; iOS 14.1; zh-Hans-CN; occ-CN; iPhone XS);ZEPETO",
              "Connection": "keep-alive",
              #   "Content-Length":"62",
              "Host": "napi.zepeto.cn",
              "Authorization": bear_token
              }
    data = {"userIds": [user_id]}
    try:
        re = requests.post(
            "https://napi.zepeto.cn/UsersInfoRequest", headers=header, data=json.dumps(data)).text
    except Exception as e:
        print(e)
    time.sleep(2)
    re_json = json.loads(re)
    print(re_json)
    user_info = re_json['users'][0]
    zepeto_id = user_info['zepetoId']
    hash_code = user_info['hashCode']
    profile_pic = user_info['profilePic']
    name = user_info['name']


def get_ticket():
    print(hash_code)
    global last_count
    try:
        re = requests.get(
            "https://api-zepeto.kajicam.com/zepeto/activity/fashion/pk/api/pkCoin/getTickets?zzId="+hash_code+"").text
    except Exception as e:
        print(e)
    time.sleep(2)
    re_json = json.loads(re)
    last_count = int(re_json['result'])
    print(last_count)


def help_ticket():
    for i in range(last_count):
        re = requests.post(
            "https://api-zepeto.kajicam.com/zepeto/activity/fashion/pk/api/pkCoin/helpTicket?authToken="+encode_token+"&duid=D3F4A802-0FD2-41D6-BCB3-28A014E81303&zzId="+hash_code+"&targetId="+target_id+"&userId="+user_id+"&nickName="+name+"&headUrl="+profile_pic).text
        re_json = json.loads(re)
        print(re_json)
        # time.sleep(1)


def sign_out():
    header = {"Accept": r"*/*",
              "Content-Type": r"application/json; charset=UTF-8",
              "X-ZEPETO-DUID": DUID,
              "Accept-Encoding": "gzip, deflate, br",
              "User-Agent": "ios.zepeto_cn/3.8.3 (ios; U; iOS 14.1; zh-Hans-CN; occ-CN; iPhone XS);ZEPETO",
              "Connection": "keep-alive",
              #   "Content-Length":"62",
              "Authorization": auth_token
              }

    re = requests.post(
        "https://napi.zepeto.cn/LogoutRequest", headers=header).text
    #print(re)
    time.sleep(0.5)


def like():
    header = {"Accept": r"*/*",
              "Content-Type": r"application/json; charset=UTF-8",
              "X-ZEPETO-DUID": DUID,
              "Accept-Encoding": "gzip, deflate, br",
              "User-Agent": "ios.zepeto_cn/3.8.3 (ios; U; iOS 14.1; zh-Hans-CN; occ-CN; iPhone XS);ZEPETO",
              "Connection": "keep-alive",
              #   "Content-Length":"62",
              "Host": "napi.zepeto.cn",
              "Authorization": bear_token
              }
    data = {
        "postId": 50237266
    }
    try:
        re = requests.post(
            "https://gapi.zepeto.cn/like/post", headers=header, data=json.dumps(data)).text

        time.sleep(2)
    except Exception as e:
        print(e)


def rename():
    header = {"Accept": r"*/*",
              "Content-Type": r"application/json; charset=UTF-8",
              "X-ZEPETO-DUID": DUID,
              "Accept-Encoding": "gzip, deflate, br",
              "User-Agent": "ios.zepeto_cn/3.8.3 (ios; U; iOS 14.1; zh-Hans-CN; occ-CN; iPhone XS);ZEPETO",
              "Connection": "keep-alive",
              #   "Content-Length":"62",
              "Host": "napi.zepeto.cn",
              "Authorization": bear_token
              }
    data = {
        "statusMessage": "", "nationality": "", "job": "", "name": hash_code, "zepetoId": zepeto_id,

    }
    try:
        re = requests.post(
            "https://napi.zepeto.cn/SaveProfileRequest_v2", headers=header, data=json.dumps(data)).text

        time.sleep(2)
        print(re)
    except Exception as e:
        print(e)

def change_password():
    global error_change
    header = {"Accept": r"*/*",
              "Content-Type": r"application/json; charset=UTF-8",
              "X-ZEPETO-DUID": DUID,
              "Accept-Encoding": "gzip, deflate, br",
              "User-Agent": "ios.zepeto_cn/3.8.3 (ios; U; iOS 14.1; zh-Hans-CN; occ-CN; iPhone XS);ZEPETO",
              "Connection": "keep-alive",
              #   "Content-Length":"62",
              "Host": "napi.zepeto.cn",
              "Authorization": bear_token
              }
    data = {"oldPassword":"a11111111","newPassword":"b1111111"}
    try:
        re = requests.post(
            "https://napi.zaizai.net/ChangeUserDetailsRequest", headers=header, data=json.dumps(data)).text

        time.sleep(2)
        print("修改密码"+re)
        re_json = json.loads(re)
        if re_json["isSuccess"] != True:
            error_password.append(error_change)
            error_change = ""

    except Exception as e:
        print(e)


def sign_get_coin():
    try:
        header = {"Accept": r"*/*",
                  "Content-Type": r"application/json; charset=UTF-8",
                  "X-ZEPETO-DUID": DUID,
                  "Accept-Encoding": "gzip, deflate, br",
                  "User-Agent": "ios.zepeto_cn/3.8.3 (ios; U; iOS 14.1; zh-Hans-CN; occ-CN; iPhone XS);ZEPETO",
                  "Connection": "keep-alive",
                  #   "Content-Length":"62",
                  "Host": "napi.zaizai.net",
                  "Authorization": bear_token}
        # 获取连续签到天数
        re = requests.post(
            "https://napi.zaizai.net/AttendanceListRequest", headers=header).text
        re_json = json.loads(re)
        #print(re_json)
        attendance_day = re_json['attendanceDay']
        #print(attendance_day)
        data_sign = {"attendanceNum": attendance_day}
        # 签到领取金币
        re_sign = requests.post(
            "https://napi.zaizai.net/ReceiveAttendanceBonus", headers=header, data=json.dumps(data_sign)).text
        re_json_sign = json.loads(re_sign)
        #print(re_json_sign)
        data_sign_log = {
            "timeZone": "Asia/Shanghai"
        }
        # 上报登录日志信息
        re_sign_log = requests.post(
            "https://napi.zaizai.net/AccountUser_v5", headers=header, data=json.dumps(data_sign_log)).text
        # print(re_sign_log)
        re_json_sign = json.loads(re_sign)
        time.sleep(random.randint(1,5))
        # 充值每日luckycoin
        re_json_daily_coin = requests.post(
            "https://napi.zaizai.net/DailyBonusRefreshRequest", headers=header
        ).text
        #print(re_json_daily_coin)
        daily_data = {"params": {"isAdvertising": False}}
        sign_result = requests.post(
            "https://napi.zaizai.net/DailyBonusReceiveRequest", headers=header, data=json.dumps(daily_data)).text
        #print(sign_result)
        return json.loads(sign_result)["coin"]
    except Exception as e:
        print("catch error in get coin")

# 批量获得金币
def get_coin():
    phone_data = read_phone_number()
    phone_list = cut_phone(phone_data)
    print("*************共{0}个账号**************".format(len(set(phone_list))))
    count = 1
    for i in phone_list:
        get_auth(str(i))
        coin = sign_get_coin()
        sign_out()
        time.sleep(random.randint(30, 50))
        print(count,"-",i,"-",coin)   
        count = count + 1

# 批量修改密码
def pl_change_password():
    phone_data = read_phone_number()
    phone_list = cut_phone(phone_data)
    for i in phone_list:
        print(i)
        get_auth(str(i))
        sign_get_coin()
        change_password()
        sign_out()
        time.sleep(random.randint(10, 20))


def total_like():
    phone_data = read_phone_number()
    phone_list = cut_phone(phone_data)
    for i in phone_list:
        print(i)
        get_auth(str(i))
        like()
        sign_out()


def total():
    phone_data = read_phone_number()
    phone_list = cut_phone(phone_data)
    count = 0
    for i in phone_list:
        count = count + 1
        print(count)
        print(i)
        status_code = get_auth(str(i))
        if status_code == 0:
            continue
        get_user_info()
        get_ticket()
        help_ticket()
        sign_out()
        bear_token = ""
        auth_token = ""
        user_id = ""
        hash_code = ""
        profile_pic = ""
        name = ""
        encode_token = ""
        last_count = 0
    print(error_password)


def rename_total():
    phone_data = read_phone_number()
    phone_list = cut_phone(phone_data)
    for i in phone_list:
        print(i)
        get_auth(str(i))
        get_user_info()
        rename()
        sign_out()
        bear_token = ""
        auth_token = ""
        user_id = ""
        hash_code = ""
        profile_pic = ""
        name = ""
        encode_token = ""
        last_count = 0


get_coin()
# pl_change_password()
print(error_password)
