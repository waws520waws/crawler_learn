
 
const CryptoJS = require('crypto-js');
var keq = "bFRHIi8WFj!b1as9mM^WU7GoEOcoOmHg"
var key = "bFRHIi8WFj!b1as9mM^WU7Go"
let a = CryptoJS.enc.Utf8.parse(key)
    , n = {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    }
    , i = CryptoJS.TripleDES.encrypt("1650535353515", a, n);
var aa = i.ciphertext.toString()

console.log(i.ciphertext)
console.log(aa)

/*
878e68df2e53b1d9a44b5f7617baab8fbc19b7a587abcfbfd83ee06844dcdf5c2c400b9bf9299556c8f41fa6d3991a4128fd3e7c2b16fdf0ce2c8384697fcac49d62fd7cc4007799f6501894c5b5a357bd1f966cc22c449e676abde86527a364aa768327edb1e5296379c907c11e606861ee3e3ed05634bd72fa2e5d72bbe075
878e68df2e53b1d9a44b5f7617baab8fbc19b7a587abcfbfd83ee06844dcdf5c2c400b9bf9299556c8f41fa6d3991a4128fd3e7c2b16fdf0ce2c8384697fcac49d62fd7cc4007799f6501894c5b5a357bd1f966cc22c449e676abde86527a364aa768327edb1e5296379c907c11e606861ee3e3ed05634bd72fa2e5d72bbe075
 */