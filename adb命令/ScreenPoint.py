
import subprocess  # 执行adb命令
import re          # 字符查找
import time

def connectDevcie():
    '''检查设备是否连接成功，如果成功返回True，否则返回False'''
    try:
        deviceInfo = subprocess.check_output('adb devices')
        '''如果没有链接设备或者设备读取失败，第二个元素为空'''
        deviceInfo = bytes.decode(deviceInfo)    # 字节转字符串
        deviceInfo = deviceInfo.split("\r\n")
        if deviceInfo[1] == '':    #没有一个设备连接
            return False
        else:
            return True
    except:
        print("connect error")

def getAndroidVersion():
    try:
        if connectDevcie():
            # 获取系统设备系统信息
            sysInfo = subprocess.check_output('adb shell cat /system/build.prop')
            # 获取安卓版本号
            sysInfo = bytes.decode(sysInfo)  # 字节转字符串
            androidVersion = re.findall("version.release=(\d\.\d)*", sysInfo, re.S)[0]
            return androidVersion
        else:
            return "Connect Fail,Please reconnect Device..."
    except:
        print("getAndroidVersion error")

def getDeviceName():
    try:
        if connectDevcie():
            # 获取设备名
            deviceInfo = subprocess.check_output('adb devices -l')
            deviceInfo = bytes.decode(deviceInfo)  # 字节转字符串
            deviceName = re.findall(r'device product:(.*) model', deviceInfo)[0]
            return deviceName
        else:
            return "Connect Fail,Please reconnect Device..."
    except:
        print("getDeviceName error")


print(getDeviceName())
print(getAndroidVersion())

###################### 连接测试完毕，开始
i=0
while(True):
    time.sleep(0.001)
    subprocess.check_output('adb shell input tap 400 400') # 此命令执行时间将近1s
    print(i)
    i += 1
print('OK')
