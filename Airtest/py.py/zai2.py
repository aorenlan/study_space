# -*- encoding=utf8 -*-
__author__ = "DELL"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/SJE7N17522001140?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])








# script content
print("start...")



def sign_new():
    sleep(2)
    poco(text='创建新账号').wait(60).click()
    sleep(2)
    poco(text='想要创作新角色').wait(20).click()
    if poco(text='删除已有角色的所有数据，开始创作新角色').wait(60).exists():
        poco(text='好的').click()
    poco(text='同意').wait(60).click()
    sleep(2)
    poco(text='下一步').wait(60).click()
    sleep(2)
    poco(text='以后再说').wait(60).click()
    sleep(10)
    check_pop()
    sleep(2)
    check_pop()
    sleep(2)
    poco(text='主页').wait(20).click()
    sleep(3)
    touch(Template(r"tpl1637993599623.png", record_pos=(0.402, 0.811), resolution=(1080, 1920)))
    sleep(5)
    check_mine_pop()
    poco(text='我').wait(20).click()
    check_mine_pop()
    sleep(1)
    check_mine_pop()
    poco(text='主页').wait(20).click()
    sleep(3)
#     swipe(Template(r"tpl1638253514553.png", record_pos=(-0.019, 0.325), resolution=(1080, 1920)), vector=[-0.255, -0.0133])

    poco(text='穿搭PK').wait(20).click()
    sleep(10)
    keyevent("back")
    sleep(3)


def sign_in():
#     poco(resourceId='cn.zepeto.main:id/fragmentMainBottomHomeIcon').click()
    sleep(2)
    if exists(Template(r"tpl1637998226479.png", record_pos=(0.407, 0.804), resolution=(1080, 1920))):
        touch(Template(r"tpl1637998322395.png", record_pos=(0.402, 0.809), resolution=(1080, 1920)))
    else:
        touch(Template(r"tpl1637944225956.png", record_pos=(0.402, 0.806), resolution=(1080, 1920)))
    sleep(3)
    check_mine_pop()
    poco(text='注册崽崽').wait(60).click()
    sleep(2)
    poco(text='登录').wait(60).click()
    poco(name='cn.zepeto.main:id/inputPhoneEditText').wait(60).click()
    sleep(3)
    text('16210909117')
    poco(text='密码').click()
    text('a2222222')
    poco(resourceId='cn.zepeto.main:id/view_bar_button_text').wait(60).click()
    check_pop()
    sleep(5)
    check_pop()
    
def sign_out():
    sleep(5)
    check_pop()
    sleep(10)
    check_pop()
    sleep(2)
    if exists(Template(r"tpl1637998226479.png", record_pos=(0.407, 0.804), resolution=(1080, 1920))):
        touch(Template(r"tpl1637998322395.png", record_pos=(0.402, 0.809), resolution=(1080, 1920)))
    else:
        touch(Template(r"tpl1637944225956.png", record_pos=(0.402, 0.806), resolution=(1080, 1920)))
    sleep(2)
    if exists(Template(r"tpl1637998226479.png", record_pos=(0.407, 0.804), resolution=(1080, 1920))):
        touch(Template(r"tpl1637998322395.png", record_pos=(0.402, 0.809), resolution=(1080, 1920)))
    else:
        touch(Template(r"tpl1637944225956.png", record_pos=(0.402, 0.806), resolution=(1080, 1920)))
    sleep(10)
    check_mine_pop()
    sleep(3)
    if exists(Template(r"tpl1638072622082.png", record_pos=(0.406, -0.746), resolution=(1080, 1920))):

        poco(name='cn.zepeto.main:id/vhProfileTabSettingButton').click()
    else:
        touch(Template(r"tpl1638072763496.png", record_pos=(0.408, 0.81), resolution=(1080, 1920)))
        sleep(2)
        poco(name='cn.zepeto.main:id/vhProfileTabSettingButton').click()
    poco(text='账号与安全').wait(20).click()
    poco(text='退出登录').wait(20).click()
    sleep(3)
    
def check_pop():
    if poco(resourceId="cn.zepeto.main:id/dialogDailyBonusCloseButton").exists():
        poco(resourceId="cn.zepeto.main:id/dialogDailyBonusCloseButton").click()

    if poco(resourceId='cn.zepeto.main:id/closeButton').exists():
        poco(resourceId='cn.zepeto.main:id/closeButton').click()

        
def check_mine_pop():
     
    if poco(resourceId="cn.zepeto.main:id/dialogFollowingCloseButton").exists():
        poco(resourceId="cn.zepeto.main:id/dialogFollowingCloseButton").click()
        
def work():
    for i in range(100):
        sign_new()
        sign_in()
        sign_out()
def work_s():
    sign_in()
    sign_out()
work()
# work_s()
# sign_out()
# sign_new()
# sign_in()
# sign_out()
# text('121.4.168.61')
# text('8222')
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
