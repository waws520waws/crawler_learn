### 1、变量调用

```js
//在函数中调用 函数之后 声明的变量
function aa() {
	console.log(qqq);
	var c = 123;
}
var qqq = 222;
```

2、类型

在js中，`任何类型数据 + ""` 后均为字符串类型，如下图：

![image-20220329132253611](./md_picture\js基础1.png)

