
import requests
import os
from dingding import get_data, gaojing


def auto_card():
    print(os.getenv('COOKIE'))
    form_data = {"token": "glados.network"}
    url = "https://glados.one/api/user/checkin"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Cookie": os.getenv('COOKIE')
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
