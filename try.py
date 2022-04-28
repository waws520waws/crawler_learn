import base64

s = b'01234567890qweqweweqeeqeqqeweqewqeqeqewqeqweqewqewqewqeqweqeqewqeqwewqewqeqeqweq'

a = base64.b64encode(s)
print(a)