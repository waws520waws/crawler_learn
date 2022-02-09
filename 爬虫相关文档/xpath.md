1、  
`//p[last()]/preceding::* ` ：取最后一个p标签之前的所有节点  
`/li[last()]/preceding-sibling::*`    ：取最后一个p标签之前的所有兄弟节点

`//div[@id=“aaa”]//following::*` : 取当前节点以及其之后的所有节点  
`//div[@id=“aaa”]/following::*` ：不包含当前节点

3、`//p[not(contains(.//a/@href,".mp3”))]`

4、  
`//div[@class=‘qwe’]`		匹配出多个时，我只想取第一个，有以下两种情况：  
	`//div[@class=‘qwe’][1]`	若父节点不同，则会匹配每个父节点下的此标签，还是会匹配出多个【可用第二种加括号的方法解决】；若是同一个父节点，则只匹配第一个  
	`(//div[@class=‘qwe’])[1]`	无论怎样，只取第一个

5、  
`//div[@class="article"]/@content`		根据属性值定位div标签，并选取此div标签中其他属性

6、  
【选取‘后代节点含有某个标签’的标签】  
`//div[@id='qwe'][descendant::h3]`  
`//p[a]`	选取子节点为a的p节点

7、  
【取两个标签之间的内容】  
`//h2[text()="采标情况"]/../following-sibling::*[position()<count(//h2[text()="采标情况"]/../following-sibling::*) - count(//h2[text()="目的意义"]/../following-sibling::*)]//text()`

8、  
【选取无文本的p标签下的a标签】  
```html
<p>
    <a href="">wenben</a>
</p>
```
`//p[not(text())]/a`

9、  
不区分大小写  
translate(string1,string2,string3); 把string1中的string2替换为string3  
如：`translate('12:30','0123','abcd')` 结果为'bc:da'  
如：`//p[text()[contains(translate(., 'ALSO READ', 'also read'), 'also read')]]`

10、  
`//p[count(a)=1 and count(a)=count(*) and count(text())=0 and not(contains(*//img/@src,"/"))]`

11、其他  
`//*[contains(text(), ':') and string-length(text())<30][.//a[string-length()>30]]`  

`//p[.//strong[contains(text(), 'More')]]`  
`//p[.//strong[contains(text(), 'More')]]/following-sibling::ul[1][.//a]`

`//strong/text()[contains(translate(.,’CADEQ,’cadeq’), 'also read')]`

### 12、各解析库的对比
- lxml，bs4，re，pyquery
	- bs4：纯python写的文档树解析库，它有4种解析器(lxml,html.parser,html5lib),我们测试的是lxml，主要可以通过标签进行定位，也可以通过css选择器进行定位
	- pyquery：模拟前端jQuery写的python文档树解析库，用起来跟jQuery非常相似，用的都是css语法进行定位元素（CSS选择器）
	- xpath：lxml是用c语言编写通过python调用的解析库，用的xpath语法
	- re：python正则表达式库
- 4个库各有优缺点：
	- bs4更多的用于解析script标签的文本，因为它的速度实在太慢了
	- re则是进行非结构化的文档进行匹配
	- lxml底层是c实现的，在速度上毋庸置疑，同时易用性也很高
	- pyquery使用更加比xpath和bs4更加灵活（可修改节点），PyQuery对象可以直接解析html文件，url(通过urllib进行请求返回结果)，文档字符串。
