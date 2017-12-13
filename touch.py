# coding:utf-8
import sys
import datetime
import time
import os
import random
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
# from com.android.monkeyrunner.recorder import MonkeyRecorder as recorder
device=mr.waitForConnection()#手机devices
# device.startActivity(component='com.tencent.mm/com.tencent.mm.ui.LauncherUI')#打开微信
# device.touch(420,200,'DOWN_AND_UP')

#输入数字
for i in range(0,15):
	print i
	if i<100:
		for a in range(1,50):
			device.touch(375,1009,'DOWN_AND_UP')
	mr.sleep(3)
	device.touch(337,772,'DOWN_AND_UP')

		# mr.sleep(1)
	# else:
	# 	for a in range(1,50):
	# 		device.touch(515,1000,'DOWN_AND_UP')
	# 	mr.sleep(3)

# # #百宝箱创建任务
# for i in range(0,10):
# 	print i
# 	for a in range(1,10):
# 		mr.sleep(1)
# 		device.touch(400,1200,'DOWN_AND_UP')
# 		mr.sleep(1)
# 		device.touch(666,777,'DOWN_AND_UP')
# 		mr.sleep(1)
# 		device.touch(210,1200,'DOWN_AND_UP')


#删除微信标签
# for i in range(0,100):
# 	device.touch(155,290,'DOWN_AND_UP')
# 	mr.sleep(1)
# 	device.touch(530,750,'DOWN_AND_UP')
# 	mr.sleep(1)
# 	device.touch(,,'DOWN_AND_UP')

# #以当天的日期创建一个文件夹
# now_time = datetime.datetime.now().strftime('%Y-%m%d-%H%M')
# path='E:/testPicture/'+now_time
# # # 去除首位空格
# # path=path.strip()
# # # 去除尾部 \ 符号
# # path=path.rstrip("\\")

# 	#获取时分秒
# def screenshot(str):
# 	documentname=str+datetime.datetime.now().strftime('%H%M')+'.png'
# 	documentpath=path+'/'+documentname
# 	print documentpath
# 	#截图并以时分保存
# 	result=device.takeSnapshot()
# 	result.writeToFile(documentpath,'png')
# 	mr.sleep(1)
# 	# # 图片比较
# 	# image = MonkeyRunner.loadImageFromFile(documentpath2,'png') #正确的图
#  #    MonkeyRunner.sleep(3.0)
#  #    if(image.sameAs(result,0.8)):
#  #        print "success!"
#  #    else:
#  #        print "fail!"

# print '\n******************************创建截图目录***********************************'
# if not os.path.exists(path):
#     # 如果不存在则创建目录
#     os.makedirs(path)
# else:
#     # 如果目录存在则不创建，并提示目录已存在
#     print path+' 目录已存在'

# print '\n******************************开始测试***************************************'
# device=mr.waitForConnection(1,'d7954cfb')#手机devices
# device.startActivity(component='com.weike.helper/com.weike.helper.ui.MainUiActivity')#打开营销助手
# device.touch(280,1230,'DOWN_AND_UP')#营销
# mr.sleep(1)
# # print '\n******************************添加通讯录好友*********************************'
# def addFriend():
# 	# 设置通讯录好友
# 	device.touch(620,400,'DOWN_AND_UP')#点击设置
# 	mr.sleep(1)
# 	#随机添加1-6个人
# 	device.touch(272,200,'DOWN_AND_UP')#添加好友数
# 	mr.sleep(1)
# 	device.touch(664,887,'DOWN_AND_UP')
# 	device.touch(664,887,'DOWN_AND_UP')#删除
# 	mr.sleep(1)
# 	addNumber=random.randint(1,6)
# 	device.type(str(addNumber))
# 	mr.sleep(1)
# 	#随机不重复添加好友
# 	reAdd=random.randint(1,2)
# 	if reAdd==1:
# 		device.touch(55,282,'DOWN_AND_UP')#重复添加
# 	else:
# 		device.touch(55,282,'DOWN_AND_UP')#重复添加
# 		device.touch(55,282,'DOWN_AND_UP')#重复添加
# 	# 添加间隔
# 	device.touch(286,355,'DOWN_AND_UP')#最小添加间隔
# 	mr.sleep(1)
# 	device.touch(664,887,'DOWN_AND_UP')
# 	device.touch(664,887,'DOWN_AND_UP')
# 	mr.sleep(1)
# 	waitNumber=random.randint(1,2)
# 	device.type(str(waitNumber))
# 	mr.sleep(1)
# 	device.touch(570,355,'DOWN_AND_UP')#最大添加间隔
# 	mr.sleep(1)
# 	device.touch(664,887,'DOWN_AND_UP')
# 	device.touch(664,887,'DOWN_AND_UP')
# 	mr.sleep(1)
# 	waitNumber=random.randint(5,10)
# 	device.type(str(waitNumber))
# 	#性别筛选:随机
# 	a=random.randint(1,3)
# 	# print a
# 	if a==1:
# 		device.touch(65,495,'DOWN_AND_UP')#全选
# 	if a==2:
# 		device.touch(286,495,'DOWN_AND_UP')#男
# 	if a==3:
# 		device.touch(500,495,'DOWN_AND_UP')#女
# 	mr.sleep(1)
# 	# 发送验证消息
# 	device.touch(65,561,'DOWN_AND_UP')#选择发送验证消息
# 	mr.sleep(1)
# 	device.touch(94,620,'DOWN_AND_UP')#选择第一条信息
# 	mr.sleep(1)
# 	device.touch(660,780,'DOWN_AND_UP')#收缩输入框
# 	screenshot('addFriend')
# 	mr.sleep(1)
# 	device.touch(355,1120,'DOWN_AND_UP')#保存
# 	mr.sleep(1)

# # addFriend()

# # print '\n******************************添加附近的人*********************************'
# def addNearby():
# 	# 设置附近的人
# 	device.touch(620,500,'DOWN_AND_UP')#点击设置
# 	mr.sleep(1)
# 	#打招呼数
# 	device.touch(240,224,'DOWN_AND_UP')
# 	mr.sleep(1)
# 	device.touch(666,895,'DOWN_AND_UP')#删除
# 	device.touch(666,895,'DOWN_AND_UP')#删除
# 	mr.sleep(1)
# 	device.type(str(random.randint(1,6)))#1-6随机生成
# 	mr.sleep(1)
# 	#不重复添加
# 	if random.randint(1,2)==1:
# 		device.touch(67,300,'DOWN_AND_UP')#点击不重复添加
# 	else:
# 		device.touch(67,300,'DOWN_AND_UP')#点击不重复添加
# 		device.touch(67,300,'DOWN_AND_UP')#点击不重复添加
# 	#添加间隔
# 	device.touch(290,376,'DOWN_AND_UP')#最小间隔
# 	mr.sleep(1)
# 	device.touch(666,895,'DOWN_AND_UP')#删除
# 	device.touch(666,895,'DOWN_AND_UP')#删除
# 	mr.sleep(1)
# 	device.type(str(random.randint(1,3)))#数字1
# 	mr.sleep(1)
# 	device.touch(590,380,'DOWN_AND_UP')#最大间隔
# 	mr.sleep(1)
# 	device.touch(666,895,'DOWN_AND_UP')#删除
# 	device.touch(666,895,'DOWN_AND_UP')#删除
# 	mr.sleep(1)
# 	device.type(str(random.randint(5,6)))#数字6
# 	mr.sleep(1)
# 	#性别筛选
# 	device.touch(75,586,'DOWN_AND_UP')#全选
# 	mr.sleep(1)
# 	device.touch(660,780,'DOWN_AND_UP')#收缩输入框
# 	mr.sleep(1)
# 	#发送验证消息
# 	# #新增
# 	# device.touch(340,1000,'DOWN_AND_UP')#新增消息
# 	# mr.sleep(1)
# 	# device.type('hello')
# 	# mr.sleep(3)
# 	# device.touch(400,600,'DOWN_AND_UP')#保存新消息
# 	# mr.sleep(1)
# 	# device.touch(71,640,'DOWN_AND_UP')#选择发送验证消息
# 	# mr.sleep(1)
# 	# device.touch(638,703,'DOWN_AND_UP')#删除第一条消息
# 	# mr.sleep(1)
# 	device.touch(88,720,'DOWN_AND_UP')#选择第一条消息
# 	mr.sleep(1)
# 	device.touch(660,780,'DOWN_AND_UP')#收缩输入框
# 	screenshot('addNearby')
# 	mr.sleep(1)
# 	device.touch(355,1120,'DOWN_AND_UP')#保存
# 	mr.sleep(1)
# # addNearby()

# # print '\n******************************朋友圈同步*********************************'

# def sameAsSomeone(str):
# 	device.touch(613,613,'DOWN_AND_UP')
# 	mr.sleep(1)
# 	device.touch(520,200,'DOWN_AND_UP')
# 	mr.sleep(1)
# 	for i in range(0,20):
# 		device.touch(670,1100,'DOWN_AND_UP')#删除
# 	mr.sleep(2)
# 	device.type(str)
# 	print '随机选择同步内容'
# 	mr.sleep(1)
# 	for i in range(1,random.randint(1,2)):
# 		device.touch(260,325,'DOWN_AND_UP')#文字
# 	for i in range(1,random.randint(1,2)):
# 		device.touch(260,390,'DOWN_AND_UP')#图片
# 	for i in range(1,random.randint(1,2)):
# 		device.touch(260,450,'DOWN_AND_UP')#视屏
# 	for i in range(1,random.randint(1,2)):
# 		device.touch(260,520,'DOWN_AND_UP')#链接
# 	# mr.sleep(1)
# 	# for i in range(1,random.randint(1,1)):
# 	# 	device.touch(260,325,'DOWN_AND_UP')#文字
# 	# for i in range(1,random.randint(1,1)):
# 	# 	device.touch(260,390,'DOWN_AND_UP')#图片
# 	# for i in range(1,random.randint(1,1)):
# 	# 	device.touch(260,450,'DOWN_AND_UP')#视屏
# 	# for i in range(1,random.randint(1,1)):
# 	# 	device.touch(260,520,'DOWN_AND_UP')#链接
# 	# device.touch(660,780,'DOWN_AND_UP')#收缩输入框
# 	# mr.sleep(1)
# 	device.touch(660,780,'DOWN_AND_UP')#收缩输入框
# 	screenshot('sameAsSomeone')
# 	mr.sleep(1)
# 	device.touch(355,1120,'DOWN_AND_UP')#保存
# 	mr.sleep(1)
# 	# device.touch(355,1220,'DOWN_AND_UP')#保存
# 	# mr.sleep(1)
# # sameAsSomeone('Uta')

# # print '\n******************************一键点赞*********************************'

# def autoThumbs():
# 	device.touch(620,730,'DOWN_AND_UP')
# 	mr.sleep(1)
# 	if 1==random.randint(1,2):
# 		print '全部点赞'
# 		device.touch(70,170,'DOWN_AND_UP')#全部点赞
# 	else:
# 		print '点别人点过的赞'
# 		device.touch(70,170,'DOWN_AND_UP')#点别人点过的赞
# 	for i in range(0,random.randint(1,2)):
# 		device.touch(71,342,'DOWN_AND_UP')
# 	device.touch(660,780,'DOWN_AND_UP')#收缩输入框
# 	mr.sleep(1)
# 	screenshot('autoThumbs')
# 	mr.sleep(1)
# 	device.touch(355,1220,'DOWN_AND_UP')#保存

# # print '\n******************************随机养号*********************************'
# def readSomething():
# 	device.touch(620,840,'DOWN_AND_UP')#点击设置
# 	mr.sleep(1)
# 	for i in range(1,random.randint(1,2)):
# 		device.touch(74,194,'DOWN_AND_UP')#阅读公众号文章
# 	for i in range(1,random.randint(1,2)):
# 		device.touch(74,270,'DOWN_AND_UP')#阅读腾讯新闻
# 	for i in range(1,random.randint(1,2)):
# 		device.touch(74,365,'DOWN_AND_UP')#看一看
# 	device.touch(660,780,'DOWN_AND_UP')#收缩输入框
# 	mr.sleep(1)
# 	screenshot('readSomething')
# 	mr.sleep(1)
# 	device.touch(355,1220,'DOWN_AND_UP')#保存
# #*****************************要执行的操作********************************************************
# # addFriend()#加通讯录好友
# # addNearby()#加附近的人
# # sameAsSomeone('Uta')#朋友圈同步
# autoThumbs()#一键点赞
# readSomething()#随机养号

# def begin():
# 	device.touch(60,400,'DOWN_AND_UP')#添加通讯录好友
# 	device.touch(60,400,'DOWN_AND_UP')#添加附近的人
# 	device.touch(60,400,'DOWN_AND_UP')#朋友圈同步
# 	device.touch(60,400,'DOWN_AND_UP')#一键点赞
# 	device.touch(60,400,'DOWN_AND_UP')#随机养好
# 	mr.sleep(1)
# 	device.touch(400,1060,'DOWN_AND_UP')#开始
# begin()
# print '\n******************************结束测试***************************************'
# print '\n******************************打开截图目录***********************************'
# #打开截图目录

# adbcommand='start'+' '+path
# os.system(adbcommand)
# #录屏
# adbsr='sr 180 markting'
# os.system('adbstr')
