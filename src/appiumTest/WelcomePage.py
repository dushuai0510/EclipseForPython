# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: Administrator
'''
from logging.handlers import WatchedFileHandler
'''
此类用来处理系统弹窗，各种权限
但是优先执行
未能做成多线程监听
'''

from appiumTest.PublicClass import *
import time

class TanChuangChuLi(): 
    def tanChuang(self):
        myBoolean=True
        while myBoolean:   
            try:
                if findText("写入/删除短信"):
                    clickText("允许") 
                    continue  
                elif findText("读取联系人"):
                    clickText("允许")
                    continue
                elif findText("读取位置信息"):
                    clickText("允许")
                    continue
                elif findText("读取通话记录"):
                    clickText("允许")
                    continue
                elif findText("读取已安装应用列表"):
                    clickText("同 意")
                    continue
                elif findText("启用录音"):                                                                                                                                                  
                    clickText("同 意")
                    continue
                elif findText("免责声明"):
                    clickText("同 意")
                    continue
                elif findText("跳过"):
                    clickText("跳过")
                    continue
                elif findText("喜欢亿连吗?去应用市场给个评分吧!~求鼓励~求鼓励~ (^_^)"):
                    clickText("不喜欢")
                    continue
                elif clickResourceID("net.easyconn.carman:id/home_app_guide_view"):
                    continue
                else:
                    print("未弹出权限处理")   
                    myBoolean=False     
            except:
                print("捕获到异常")
                continue
        else:
            print("退出弹框处理")

    def tanChuangOne(self):
            myBoolean=True
            while myBoolean:   
                try:
                    if clickText("允许"):
                        continue  
                    elif clickText("同 意"):
                        continue
                    elif clickText("跳过"):
                        continue
                    elif clickText("不喜欢"):
                        continue
                    elif clickResourceID("net.easyconn.carman:id/home_app_guide_view"):
                        continue
                    else:
                        print("未弹出权限处理")   
                        myBoolean=False     
                except:
                    print("捕获到异常")
                    continue
            else:
                print("退出弹框处理")

    def clickAlert(self):
        alerttext=["写入/删除短信","读取联系人","读取位置信息","读取通话记录","读取已安装应用列表","启用录音","免责声明","喜欢亿连吗?去应用市场给个评分吧!~求鼓励~求鼓励~ (^_^)"]
        myBoolean=True
        while myBoolean: 
            getalert= getAlertText
            for getalert in alerttext:
                if findText("允许"):
                    clickText('允许')
                    continue
                elif findText("同 意"):
                    clickText("同 意")
                    continue
                elif findText("跳过"):
                    clickText('跳过')
                    continue
                elif findText("不喜欢"):
                    clickText("不喜欢")
                    continue
                elif clickResourceID("net.easyconn.carman:id/home_app_guide_view"):
                    continue
                else:
                    print("error!")
                    myBoolean=False  
                    break
            print("ok")
            continue
        else:
            print("oooook")
    