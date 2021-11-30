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



def sign_new():

    poco(text='创建新账号').click()
    poco(text='想要创作新角色').click()
    if poco(text='删除已有角色的所有数据，开始创作新角色').exists():
        poco(text='好的').click()
    sleep(3)
    poco(text='同意').click()
    sleep(3)
    
    poco(text='下一步').wait(3).click()
    poco(text='以后再说').wait(1).click()
    sleep(5)
    check_pop()
    poco(text='主页').click()
    sleep(3)
    touch(Template(r"tpl1637993599623.png", record_pos=(0.402, 0.811), resolution=(1080, 1920)))
    check_pop()
    poco(text='主页').click()
    sleep(3)
    poco(text='穿搭PK').click()
    sleep(10)
    keyevent("back")
    sleep(3)


def sign_in():
#     poco(resourceId='cn.zepeto.main:id/fragmentMainBottomHomeIcon').click()
    if exists(Template(r"tpl1637998226479.png", record_pos=(0.407, 0.804), resolution=(1080, 1920))):
        touch(Template(r"tpl1637998322395.png", record_pos=(0.402, 0.809), resolution=(1080, 1920)))
    else:
        touch(Template(r"tpl1637944225956.png", record_pos=(0.402, 0.806), resolution=(1080, 1920)))
    sleep(3)
    check_pop()
    poco(text='注册崽崽').click()
    sleep(3)
    poco(text='登录').click()
    sleep(3)
    poco(name='cn.zepeto.main:id/inputPhoneEditText').click()
    sleep(3)
    text('16210909117')
    poco(text='密码').click()
    text('a2222222')
    poco(resourceId='cn.zepeto.main:id/view_bar_button_text').click()
    check_pop()
    sleep(5)
    
def sign_out():
    check_pop()
    if exists(Template(r"tpl1637998226479.png", record_pos=(0.407, 0.804), resolution=(1080, 1920))):
        touch(Template(r"tpl1637998322395.png", record_pos=(0.402, 0.809), resolution=(1080, 1920)))
    else:
        touch(Template(r"tpl1637944225956.png", record_pos=(0.402, 0.806), resolution=(1080, 1920)))

    time.sleep(2)
    check_pop()
    poco(name='cn.zepeto.main:id/vhProfileTabSettingButton').click()
    poco(text='账号与安全').click()
    sleep(1)
    poco(text='退出登录').click()
    sleep(3)
    
def check_pop():
    if poco(resourceId="cn.zepeto.main:id/dialogDailyBonusCloseButton").exists():
        poco(resourceId="cn.zepeto.main:id/dialogDailyBonusCloseButton").click()
    
    if poco(resourceId="cn.zepeto.main:id/dialogFollowingCloseButton").exists():
        poco(resourceId="cn.zepeto.main:id/dialogFollowingCloseButton").click()
 
def work():
    for i in range(100):
        sign_new()
        sign_in()
        sign_out()
        
# work()
# sign_new()
sign_in()
sign_out()
# text('121.4.168.61')
# text('8222')
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)


