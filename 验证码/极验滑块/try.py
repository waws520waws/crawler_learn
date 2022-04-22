from Crypto.Cipher import AES,DES3
import time
from Crypto.Util.Padding import pad
from base64 import b64encode


t = "1650535353515"

'''
PKCS7：(1) 数据如果长度刚好合适，就填充数据长度的字节，填充数据为ASCII码编号为数据长度的字符
      （2）数据长度如果没对齐，则差n长度，就补充n长度的ASCII码编号为n的字符
'''
pad_text = pad(t.encode('utf-8'), DES3.block_size, style='pkcs7')  # 选择pkcs7补全

key = "bFRHIi8WFj!b1as9mM^WU7Go"
des = DES3.new(key.encode('utf-8'), DES3.MODE_ECB)
data_byte = des.encrypt(pad_text)
print(data_byte)
# 加密后的数据无法用decode，解码不出来，因为是加密

aa = str(b64encode(data_byte), 'utf-8')
print(aa)

str1 = str(data_byte)

import hashlib
## ====================== bv


### 或者只需要一句代码
str1_md5 = hashlib.md5(str1.encode(encoding='utf-8')).hexdigest()
print(str1_md5)