//// 1、导入需要的模块
// 将JS源码转换成语法树
const parser = require("@babel/parser");
// 为parser提供模板引擎
const template = require("@babel/template").default;
// 遍历AST
const traverse = require("@babel/traverse").default;
// 操作节点，比如判断节点类型，生成新的节点等
const t = require("@babel/types");
// 将语法树转换为源代码
const generator = require("@babel/generator").default;


//// 2、 操作文件，读取原代码
const fs = require("fs");
var jscode = fs.readFileSync("read.js", {     //更改读取文件
    encoding: "utf-8"
});
console.log(jscode);


//// 3、 将JS源码转换成语法树
// 这个网站可在线将JS源码转换成语法树：https://astexplorer.net/
var ast = parser.parse(jscode);


//// 4、 对语法树进行增删改查
var MyVisitor  = {
    // Identifier为语法树中的type，当遇到此类型结点的时候会调用此函数。其他方法参考github文档
    Identifier(path){
        console.log(path.node.name); // 用path.node遍历结点
    },
    // VariableDeclarator为语法树中的type
    VariableDeclarator(path){
        console.log(path.node.init.value);
        // 修改结点的值
        // 左边为节点，右边为修改后的值（值为哪种类型，就用对应类型的方法，可在官网查到：https://www.babeljs.cn/docs/babel-types）
        path.node.init = t.StringLiteral('jieyang');
    }
}
traverse(ast, MyVisitor)


//// 5、 将（修改后的）语法树转换为源代码
var gcode = generator(ast)
console.log(gcode)