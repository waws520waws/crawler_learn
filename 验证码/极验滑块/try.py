import execjs

with open('./slide.7.8.6.js', 'r') as f:
    js = f.read()

docjs = execjs.compile(js)

r = docjs.call('get_s')
print(r)
