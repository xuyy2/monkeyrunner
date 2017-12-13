# coding:utf-8
import sys
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi

from com.android.monkeyrunner.easy import EasyMonkeyDevice  #提供了根据ID进行访问
from com.android.monkeyrunner.easy import By    #根据ID返回PyObject的方法
# from com.android.chimpchat.hierarchyviewer import HierarchyViewer
# from com.android.hierarchyviewerlib.device import ViewNode
# from com.android.monkeyrunner import MonkeyView
# from com.android.monkeyrunner.recorder import MonkeyRecorder as recorder

device=mr.waitForConnection()#手机devices
# easy_device = EasyMonkeyDevice(device)
device.startActivity(component='com.android.systemui/com.android.systemui.statusbar.preferences.PackageListActivity')#打开微信 device.touch()
# device.touch(500,200,'DOWN_AND_UP')

for i in range(1,100):
    device.touch(500,200,'DOWN_AND_UP')
    mr.sleep(1)
    device.touch(650,210,'DOWN_AND_UP')
    mr.sleep(1)
    device.touch(50,100,'DOWN_AND_UP')
    mr.sleep(1)
    device.drag((500,330),(500,200),0.1,10)
    mr.sleep(1)
