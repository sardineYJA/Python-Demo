import itchat
from itchat.content import *


# 获取好友信息
def get_my_friends():
    my_friends_list = itchat.get_friends(update=True)

    num = 1    # 打印每一位好友信息
    for friend_dict in my_friends_list:
        print('==========我的第 ', num, ' 位朋友===========')

        print('用户名：', friend_dict['NickName'])
        print('备注名：', friend_dict['RemarkName'])
        print('性  别：', friend_dict['Sex'])  # 1男 2女 0其他
        print('省  份：', friend_dict['Province'])
        print('城  市：', friend_dict['City'])
        print('个性签名：', friend_dict['Signature'])

        # for key in friend_dict:  # 输出全部信息
        #print(key, ' : ', friend_dict[key])
        num = num + 1

    return my_friends_list


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    # msg.user.send('%s: %s' % (msg.type, msg.text))  # 注释回复
    print(msg['Content'], '------', msg['User']['NickName'])
    # 收到信息，回复


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    # 收到文件并下载，回复
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    # return '@%s@%s' % (typeSymbol, msg.fileName) # 注释回复


if __name__ == '__main__':

        # 参数表示保持登录，生成文件itcht.pkl存储登录状态
    itchat.auto_login(hotReload=True)

    # 向文件传输助手发送信息
    itchat.send('Hello, filehelper', toUserName='filehelper')

    # get_my_friends()

    itchat.run()
