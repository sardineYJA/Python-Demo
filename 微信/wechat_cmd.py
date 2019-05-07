import itchat
import os
import time
import cv2

sendMsg = "{消息助手}：暂时无法回复"
usageMsg = "使用方法：\n1.运行CMD命令：cmd xxx (xxx为命令)\n"\
    "-例如关机命令:\ncmd shutdown -s -t 0 \n"\
    "2.获取当前电脑摄影：cap\n"

flag = 0  # 消息助手开关


@itchat.msg_register('Text')
def text_reply(msg):
    global flagl
    message = msg['Text']
    fromName = msg['FromUserName']
    toName = msg['ToUserName']

    if toName == "filehelper":
        if message == "cap":
            cap = cv2.VideoCapture(0)
            ret, img = cap.read()
            cv2.imwrite("weixinTemp.jpg", img)
            itchat.send('@img@%s' % u'weixinTemp.jpg', 'filehelper')
            cap.release()

        if message[0:3] == "cmd":
            result = os.popen(message.strip(message[0:4]))
            result = result.read()
            itchat.send(result, 'filehelper')


if __name__ == '__main__':
    itchat.auto_login()
    itchat.send(usageMsg, "filehelper")
    itchat.run()
