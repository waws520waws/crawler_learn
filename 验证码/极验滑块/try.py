import requests
import json

gt = '019924a82c70bb123aae90d483087f94'
challenge = '06eb4d22d470e2481cc7070146cf966ekh'
w = '5cee17268bc71ede8d087dcb26e06cd7d7211cf1a3e827f952c54a745a3dbefe8bb3079fcca201c45193f397f60e6296bdbd894a8ce4f13c438be4f3fbd06416f36e85ec260fc29e1bbdb4900aa482f82a0546d4adf6c685ca37e8ac5cb8470003cbddb2635af115c73eb9e12bc82118dac90119b989e65f4c14bee1a6c89914'

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    }
try:
    print('ajax w: ', w)
    params = {
        "gt": gt,
        "challenge": challenge,
        "lang": "zh-cn",
        "$_BBF": 0,
        "client_type": "web",
        "w": w,
    }
    url_ajax = 'https://api.geetest.com/ajax.php'
    response = requests.get(url_ajax, headers=headers, params=params)
    print('validate: ', response.text)
    response_dict = response.text[1:-1]
    response_dict = json.loads(response_dict)

    if response_dict["message"] == "success":
        print(f"验证通过 -> {response.status_code, response_dict}")

    elif response_dict["message"] == "fail":
        print(f"验证不通过,未能正确拼合图像 -> {response.status_code, response_dict}")

    elif response_dict["message"] == "forbidden":
        print(f"轨迹验证不通过 -> {response.status_code, response_dict}")


except Exception as e:
    raise e