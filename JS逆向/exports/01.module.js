
console.log('我是01.module.js')

var x = 10;
var y = 20;

exports.a = 'i am a';
module.exports.b = 'i am b';
exports.fn1 = function () {}

// 一次性全部导出
module.exports = {
    aa: 'i am aa',
    bb: 'i am bb',
    fn2: function () {}
}

t = {}

t.exports = function () {
    console.log('aaaaa')
    module.exports.a = 'i am a';
}

