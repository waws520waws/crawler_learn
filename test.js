// 主要是注意类型
var document = {
    createElement: function () {
        return {
            innerText: "",  // 因为原码中有赋值，所以这里可以置为空
            firstChild: {
                href: "xxx" // 下面的代码中浏览器控制台执行，查看结果xxx
            }
        }
    }
}

!function(){
    var t = document.createElement('div')
    t.innerText = "<a href='/'>x</a>"
    t = t.firstChild.href  // 浏览器控制台执行，查看结果
}()
