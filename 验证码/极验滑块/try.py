import execjs
import time

with open('./slide.7.8.6.js', 'r') as f:
    js = f.read()

docjs = execjs.compile(js)

aa = 'P-!!Bsttt)t(yty!!-($*R?:7.:A?5$,l$-7'
rp = 'e89f1bc0672333a4b7bd5eb89bd44d4d'
userresponse = '5c50048413'
passtime = 792

t = round(time.time() * 1000, 1)

u = docjs.call('get_u')
l = docjs.call('get_l', aa, rp, userresponse, passtime, t)
h = docjs.call('get_h', l)
print(h+u)

