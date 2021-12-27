import execjs

with open('test3.js', 'r', encoding='utf-8') as f:
    js = f.read()

exe = execjs.compile(js)

res = exe.call('fs')

print(res)

aa = exe.eval('bb')

print(aa)