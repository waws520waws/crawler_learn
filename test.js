function m(t) {
    if (t)
        console.log('123')
    return 'qwe'
}

var a = Object(m(''))
console.log(a)

CryptoJS.enc.Utf8.parse