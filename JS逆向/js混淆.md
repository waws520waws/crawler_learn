【参考】https://www.bilibili.com/video/BV1Kh411r7uR?p=14&spm_id_from=pageDriver

### 一、一些常见混淆

#### 1、eval混淆

​	1）混淆常量的名和值

​	2）混淆代码执行流程

​	`eval()`：可执行js代码（自带一个VM虚拟机），将js代码加密后放入其中，起到混淆作用，如下图：

![image-20220329102118614](D:\PycharmProjects\crawler_learn\JS逆向\md_picture\js逆向2.png)

#### 2、aa 与 jj 与 FUCK 加密混淆

一般是对js代码加密。

##### 1）aa加密

简介：JS默认支持Unicode，那么就支持全球所有的语言，那么就可以用其它语言的字符做变量，就会出现看着像 `O` 但不是 `o`，看着像 `0` 但不是 `0`，看着像 `p` 但不是 `p`

【在线js加密工具】https://www.sojson.com/aaencode.html

如下，将 `var a = 1;` 进行 aa 加密：

![image-20220329103552640](D:\PycharmProjects\crawler_learn\JS逆向\md_picture\js逆向3.png)

实例：【链接】http://spider.wangluozhe.com/challenge/3

![image-20220425094958115](./md_picture/js逆向24.png)

​	如上图，我们可以看到关键信息，在代码最后，使用了Function、constructor，并且在最后一个括号中return了一句代码，所以我们写以下的hook代码：

```js
Function.prototype.constructor_ = Function.prototype.constructor;
Function.prototype.constructor = function(x){
	debugger;
	return Function.prototype.constructor_(x);
}
```

​	如下图，当第二次调用此代码时，可以看到明文代码，

​		![](D:\PycharmProjects\crawler_learn\JS逆向\md_picture\js逆向25.png)

##### 2）jj 加密

将 `var a = 1;` 进行 jj 加密：

![image-20220329112431918](D:\PycharmProjects\crawler_learn\JS逆向\md_picture\js逆向5.png)

这种加密方式，一般是经过一些方法的处理得到明文，如下图，经过了两个方法进行处理，可在此文件的控制台中打印两个方法处理后的代码，可得到明文：【实例链接】http://spider.wangluozhe.com/challenge/2

![image-20220424165946687](./md_picture/js逆向23.png)

##### 3）FUCK加密

将 `var a = 1;` 进行 FUCK 加密：

![image-20220329132807218](D:\PycharmProjects\crawler_learn\JS逆向\md_picture\js逆向6.png)

​	实例：【链接】http://spider.wangluozhe.com/challenge/4，此加密更恶心，我们可以先使用上面aa加密的方法进行尝试，如下：

​			![image-20220425102809943](./md_picture/js逆向26.png)

​	发现，使用了eval，所以我们还需要hook住 eval，代码如下

```js
eval_ = eval;
eval = function(x){
	debugger;
	return eval_(x);
}
```

​	然后执行，就可以看到明文了，如下

​		![image-20220425105034907](./md_picture/js逆向27.png)



##### 4）应对措施

- 1）先把最后的自执行括号删除，然后执行，看是否得到结果
- 2）其他方式见上面每种加密方式后的实例

#### 3、ob混淆

对变量和方法名进行替换，如下：

```js
var _0x30bb = ['log', 'Hello\x20World!'];  //变量数组

(function (_0x38d89d, _0x30bbb2) {
    var _0xae0a32 = function (_0x2e4e9d) {  //数组的移位操作
        while (--_0x2e4e9d) {
            _0x38d89d['push'](_0x38d89d['shift']());
        }
    };
    _0xae0a32(++_0x30bbb2);
}(_0x30bb, 0x153));

var _0xae0a = function (_0x38d89d, _0x30bbb2) {  //解密函数
    _0x38d89d = _0x38d89d - 0x0;
    var _0xae0a32 = _0x30bb[_0x38d89d];
    return _0xae0a32;
};

function hi() {  //加密后的函数
    console[_0xae0a('0x1')](_0xae0a('0x0'));
}

hi();
```

ob混淆的常见特性：

​		第一行可以看到明显的一个数组；

​		会有解密函数进行解密（一般是频繁调用的那个函数；可能会有多个解密函数）



之前这个网站有 ob混淆破解测试版：http://tool.yuanrenxue.com/，现在无了

### 二、AST 抽象语法树 + babel

【视频教程】https://www.bilibili.com/video/BV1Kh411r7uR?p=31&spm_id_from=pageDriver

1、AST 抽象语法树

【参考】https://blog.csdn.net/huangpb123/article/details/84799198

简介：从纯文本转换成树形结构的数据，每个条目和树中的节点一一对应；当下的编译器都做了纯文本转AST的事情，

混淆过程：提交一段js代码 —> 混淆器（AST）—> 返回到网页。在文本转成AST后，对其进行一些增删改查操作，进行混淆。

2、babel

【官网】https://www.babeljs.cn/

【github使用手册】https://github.com/jamiebuilds/babel-handbook/blob/master/translations/zh-Hans/README.md

简介：Babel 是一个工具链，主要用于将采用 ECMAScript 2015+ 语法编写的代码转换为向后兼容的 JavaScript 语法，以便能够运行在当前和旧版本的浏览器或其他环境中（解决不兼容问题）。Babel 使用一个基于 [ESTree](https://github.com/estree/estree) 并修改过的 AST。

原理及使用：https://github.com/jamiebuilds/babel-handbook/blob/master/translations/zh-Hans/plugin-handbook.md

- 主要用到下面这些：

  <img src="./md_picture/js逆向19.png" alt="image-20220402174014787" style="zoom:80%;" />

使用：我们做反混淆，只需要安装 babel-core

-  先在当前js文件目录下安装 babel-core：`npm install --save-dev @babel/core`

- 第一份简单示例（用的是pycharm）：检查是否可用

```js
const babel = require("@babel/core");
var code = "var a = 1"

const result = babel.transform(code);
console.log(result.code);
console.log(result)
```

- 第一份实例：见`./AST-babel/firstBabel.js`



