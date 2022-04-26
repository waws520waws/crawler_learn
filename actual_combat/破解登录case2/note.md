破解此网站的步骤：

1、随便登录，有 '用户或密码错误' 提示，可直接在开发者工具中搜，大概率可定位到发送数据的API，如下图

​		![image-20220426175349947](./pic_note/image-20220426175349947.png)

​	这个包，提交了两个加密参数 val、password；并且发现，Type 为 document、Initiator 为 Other，这种一般在网页源码中搜这个url。如下图:

![image-20220426180619391](./pic_note/image-20220426180619391.png)

​	发现是form表单提交的数据，并调用了 `return loginCheck(this)`，然后直接搜 loginCheck，定位到源码中的位置，如下图：

​								![image-20220426181249294](./pic_note/image-20220426181249294.png)

