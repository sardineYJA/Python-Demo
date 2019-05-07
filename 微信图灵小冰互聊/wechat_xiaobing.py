import os
import time
import itchat
import re
from itchat.content import *


current_dir = os.path.dirname(os.path.realpath(__file__))
itchat.auto_login(enableCmdQR=2,hotReload=True)    # 微信热登陆
Raisound = itchat.search_friends(name="")[0]['UserName']
tuling = itchat.search_mps(name='图灵机器人')[0]['UserName']    # 获取图灵机器人的用户名

questions = []
answers = [] 
tag = 0 # 设置为微信公众号的标识位，防止微信号转发两条信息
cn_regex = re.compile(r"^([\u4e00-\u9fa5]|\w)|[\u3002|\uff1f|\uff01|\uff0c|\u3001|\uff1b|\uff1a|\u201c|\u201d|\u2018|\u2019|\uff08|\uff09|\u300a|\u300b|\u3008|\u3009|\u3010|\u3011|\u300e|\u300f|\u300c|\u300d|\ufe43|\ufe44|\u3014|\u3015|\u2026|\u2014|\uff5e|\ufe4f|\uffe5]|[@|#|?|!|,|.|[|\]|]|{|}]")
fw = open(os.path.join(current_dir, 'data', 'record.txt'), 'a', encoding='utf-8')


def regx(wechat):
    result = ''
    global cn_regex
    for char in wechat:
        if re.match(cn_regex, char):
            result += char
    return result


@itchat.msg_register(TEXT,isFriendChat = True,isMpChat = False)  # 获取joven的信息，再转发给图灵机器人
def fw_tuling(question):
    """转发对话信息给小冰"""
    msg_text = question['Text']
    question_r = '冰：' + msg_text + '\n'
    print("冰：", msg_text)
    fw.write(question_r)
    fw.flush()
    if '人家要休息1个小时再跟你接着说。' in msg_text:
        print('小冰要休息一个小时！')
        time.sleep(3600)
    global tag
    tag = 1
    itchat.send(msg_text, tuling)


@itchat.msg_register([TEXT,PICTURE,RECORDING,ATTACHMENT,VIDEO,MAP,SHARING],isMpChat=True,isFriendChat = False)    # 图灵机器人回复之后，将问题发给raisound
def get_tuling(msg):
    if msg['Type'] == TEXT:
        tuling_msg_first = msg['Text']
        tuling_msg = regx(tuling_msg_first)
    else:
        tuling_msg = '给我讲个笑话呗'
    if tuling_msg == '':
        tuling_msg = '给我讲个笑话呗'
    global tag
    if tag == 1:
        print("图：{}".format(tuling_msg))
        answer_r = '图：' + tuling_msg + '\n'
        fw.write(answer_r)
        fw.flush()
        tag = 0
        itchat.send_msg(tuling_msg, Raisound)
 
itchat.run()
fw.close()
