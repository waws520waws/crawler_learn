import requests

cookie_str = ""

li = cookie_str.split('; ')

cookie_dic = {}
for i in li:
    k, v = i.split('=', 1)
    cookie_dic[k] = v
