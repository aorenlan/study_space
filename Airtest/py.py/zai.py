# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import time

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/KRUWNFSSDA5XDI8L?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH",])





# script content
print("start...")



def test():


    poco(text='创建新账号').click()
    poco(text='想要创作新角色').click()
    if poco(text='删除已有角色的所有数据，开始创作新角色').exists():
        poco(text='好的').click()
    time.sleep(2)
    poco(text='同意').click()
    poco(text='下一步').wait(3).click()
    poco(text='以后再说').wait(1).click()
    time.sleep(8)
    check_pop()
    poco(text='穿搭PK').click()

def check_pop():
    if poco(resourceId="cn.zepeto.main:id/dialogDailyBonusCloseButton").exists():
        poco(resourceId="cn.zepeto.main:id/dialogDailyBonusCloseButton").click()
    
    if poco(resourceId="cn.zepeto.main:id/dialogFollowingCloseButton").exists():
        poco(resourceId="cn.zepeto.main:id/dialogFollowingCloseButton").click()
        
test()
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
