import requests

url = 'https://static.geetest.com' + "/static/js/gct.861a4938461c8226f84ed59a1e2d0214.js"

res = requests.get(url)

print(res.text)