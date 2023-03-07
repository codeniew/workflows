# filename: dingtalk.py
import base64
import hashlib
import hmac
import time
import urllib
import os
import requests
import json
import sys

def gaojing(data):
    # 将消息提交给钉钉机器人
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    # 注意替换钉钉群的机器人webhook
    access_token = os.getenv("TOKEN")
    print(access_token)
    timestamp, sign = timeSign()
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=%s&timestamp=%s&sign=%s' % (access_token, timestamp, sign)
    print(webhook)
    repson = requests.post(url=webhook, data=json.dumps(data), headers=headers)
    print(repson.text)

def get_data(text_content):
    # 返回钉钉机器人所需的文本格式
    text = {
        "msgtype": "text",
        "text": {
            "content": text_content
        },
    }
    return text

def timeSign():
    timestamp = str(round(time.time() * 1000))
    secret = 'SEC7f8eb6fd58c0ca97134258ce0b4561fda9897ec177fddb8709093064d2fe569b'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp, sign
    # print(timestamp)
    # print(sign)

if __name__ == "__main__":
    # 命令行第一个参数为告警内容
    text_content = "test"
    data = get_data(text_content)
    gaojing(data)