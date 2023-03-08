
import requests
import os
from dingding import get_data, gaojing


def auto_card():
    cookie = os.getenv('COOKIE')
    # user_agent = os.getenv('USER_AGENT')
    # cookie = 'koa:sess=eyJ1c2VySWQiOjE2NjQzNywiX2V4cGlyZSI6MTcwNDE3ODQyMjgzOCwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=0JSqbRNpBbQK7-Q68Zdooru92wc'
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'
    form_data = {"token": "glados.network"}
    url = "https://glados.one/api/user/checkin"
    headers = {
        "User-Agent": user_agent,
        "Cookie": cookie
    }
    print("ss")
    print("cookie已经打印")
    response = requests.post(url, data=form_data, headers=headers)
    response_data = response.json()
    print(response_data)
    if response_data['message'] == "Please Try Tomorrow":
        print("nw已重复打卡")
        data = get_data("nw已重复打卡")
        gaojing(data)
    elif response_data['code'] == -2:
        data = get_data(response_data['message'])
        gaojing(data)
        print(response_data['message'])
    else:
        print("nw打卡成功")
        data = get_data("nw打卡成功")
        gaojing(data)


if __name__ == '__main__':
    auto_card()
