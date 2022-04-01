### 一、hook是什么？

浏览器交互流程：连接服务器——拿回资源——渲染（解析）资源

js执行流程：初始化（自执行）——页面逻辑——等待用户输入——加密数据——提交数据

hook就是在上面流程任意的环节，插入自己的代码，让浏览器先执行自己的代码，再执行原本的网站代码；hook只影响hook之后的操作。

### 二、如何hook

hook：改变原方法或原代码的执行流程（结合断点）

如何做？

#### 1、赋值给全局变量

- 将需要打印的值赋值给一个全局变量 `window.jieyang = xx_value`，如 ‘./js逆向.md’ 中的第五点

#### 2、覆盖原方法（覆盖的方法需要比原方法后执行）

- 1）直接将原方法等于某个值或另一个方法 `xxxfunc = function(){}`，如 ‘./js逆向.md’ 中的第八点的第2点

- 2）ES6语法：`Object.defineProperty`

  - 给对象重新定义属性
  - 监听属性的设置值和获取值

  ```js
  // hook全局的cookie设置点
  !(function(){
      // 严谨模式，检查所有错误
      'use strict';
      var cookieTemp = "";
      // document是要hook的对象；这里hook的是cookie
      Object.defineProperty(document, 'cookie', {
          // hook set方法，赋值的方法
          set: function(val){
              console.log('Hook捕获到cookie设置->', val);
              cookieTemp = val;
              return val;
          },
          // hook get方法，取值的方法
          get: function(){
              return cookieTemp;
          }       
      });
  })();
  ```


#### 3、js中的Proxy

- `const p = new Proxy(target, handler)`

#### 4、ajax请求hook

- ajax请求包含的方法在 `XMLHttpRequest` 对象下边

  ![image-20220401155528419](./md_picture/js逆向11.png)

- hook方法：

  - 先在控制台执行以下内容（这里以发送数据为例）：

  ![image-20220401160058835](./md_picture/js逆向12.png)

  - 然后再执行发送数据时（不是刷新网页），由于上面的代码，浏览器就会被debugger住；然后就能知道在哪里进行的 send ，如下图：

    ![image-20220401161939667](./md_picture/js逆向13.png)

#### 5、刷新网页时hook

- 即我想在浏览器器初始化时就hook，那么就可以借助第三方插件了

  - 油猴（浏览器插件）

  - fiddler（代理）

    - 需要安装fiddler的[插件](https://blog.csdn.net/qq_36759224/article/details/120783727)，这里用到的是编程猫的插件（大佬写好的）

    - 插件安装好后，打开fiddler，编写hook代码，并开启hook，如下：

      ![image-20220401175232575](./md_picture/js逆向14.png)

    - 然后浏览器打开某个网页（fiddler能抓包），会发现在网页源码开头会有我们的hook代码，那么这段代码就会先执行，再执行网页原代码，如下：

      ![image-20220401175723194](./md_picture/js逆向15.png)

- 如果不想用第三方插件，可以在网页第一个请求的js中的第一行插入断点，然后刷新页面，被断住，然后在控制台执行hook代码，一样的效果。为什么是js？因为hook肯定是在js上啊


### 三、hook时的一些问题

#### 1、上下文

上下文：一个环境（js中：V8虚拟机；浏览器中：新页面），在 hook 时要注意上下文，

​	如下，我要 hook住 `ff()`方法，

​		在 `var ww = 2;` 处设置断点1，运行，在控制台处输出 `ff`，发现报错，原因是我们执行到断点处，已经出`zz()`方法了，已经是在全局作用域了，无 `ff()` 方法；

​		所以，要在断点2出设置断点。

```js
var qq = 1;
!(function zz(){
    var ff = function(){
        console.log('aaaaa');
    }
    debugger; //在此处设置断点2
})();
var ww = 2;  //在此处设置断点1
```

#### 2、打不上断点 + hook不住函数

在某些地方无法设置断点，可以在此处写一句代码 `debugger;` ，程序运行到此处会自动断掉。

​	看如下代码存在的问题：

```js
var qq = 1;
!(function zz(){
    function aa(){
        console.log('aaaaa');
    }
    //debugger;
    var bb = 3;
})();
var ww = 2;
```

​	上面代码在 `var bb = 3;` 处打断点时，打不上，此时要用 `debugger;`。

​	打上断点后，运行，此时已经在 `zz()`上下文中了，但是控制台输出 `aa` ，发现还是报错，此时需要使用 `var aa = function(){}` 来声明函数。
