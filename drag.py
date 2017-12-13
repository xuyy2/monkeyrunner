#coding:utf-8
import sys
import datetime
import time
import os
import random
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
# from com.android.monkeyrunner.easy import EasyMonkeyDevice  #提供了根据ID进行访问
# from com.android.monkeyrunner.easy import By    #根据ID返回PyObject的方法

# from com.android.monkeyrunner.recorder import MonkeyRecorder as recorder

# device=mr.waitForConnection(1,'d7954cfb')#手机devices
device=mr.waitForConnection()#手机devices
for i in range(1,100):
    device.drag((250,530),(250,1000),0.1,10)
    device.drag((250,530),(250,1000),0.1,10)
    device.drag((250,1000),(250,530),0.1,10)
    device.drag((250,1000),(250,530),0.1,10)
    mr.sleep(1)
# device.touch(280,1230,'DOWN_AND_UP')#营销
print 'drag over'
