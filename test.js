var is_Mobile = 0;
if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    var is_Mobile = 1;
    var link = document.createElement("link");
    link.setAttribute("rel", "stylesheet");
    link.setAttribute("type", "text/css");
    link.setAttribute("href", mbcss);
    document.getElementsByTagName("head")[0].appendChild(link);
}
function sg() {
    ga_url = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js';
    document.writeln('<script async src="' + ga_url + '"></script>');
    document.writeln('<ins class="adsbygoogle"');
    document.writeln('style="display:block; height:90px; max-width:728px;"');
    //  document.writeln('data-ad-format="auto"');
    // document.writeln('data-full-width-responsive="true"');
    document.writeln('data-ad-client="ca-pub-8086936760373158"');
    document.writeln('data-ad-slot="6004497390"></ins>');
    document.writeln('<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>');
}

var tim = 1;
setInterval("tim++", 10);
var b = 1;
function start(c) {
    if (c == 1) {
        var i1 = 1;
        var i2 = ns
        var tnm = '学术镜像';
    } else {
        var i1 = ns + 1;
        var i2 = nt;
        var tnm = '网页镜像';
    }
    for (var i = i1; i <= i2; i++) {
        ts[i] = tim;
        document.write('<div class="url"><span class="name">' + tnm + String(i - i1 + 1) + '：</span><span class="txt" id="txt' + i + '"><img src="res/loading.gif" border=0 /></span><\/div>');
    }
}
function auto(b) {
    t = (tim - ts[b]) / 100;
    tt = t.toString().split('.');
    if (tt.length == 1)
        t = t.toString() + '.00';
    else if (tt[1].length < 2)
        t = t.toString() + '0';
    if (t > 4)
        document.getElementById("txt" + b).innerHTML = '<font color=red>连接超时！<\/font>';
    else
        document.getElementById("txt" + b).innerHTML = 'takes ' + t + 's.   <a href="javascript:;" class="ok" onclick="visit(\'' + autourl[b] + '\')"> 现在访问 <\/a>';
}
function visit(url) {
    var newTab = window.open('about:blank');
    if (Gword != '')
        url = strdecode(url);
    newTab.location.href = url;
}
function run() {
    for (var i = 1; i < autourl.length; i++) {
        url = autourl[i];
        if (Gword != '')
            url = strdecode(url);
        var st = url.indexOf("//", 1);
        var _domain = url.substring(st + 1, url.length);
        var et = _domain.indexOf("/", 1);
        surl = url.substring(0, et + st + 2);
        document.write('<img class="hidden" src="' + surl + '#g' + Math.ceil(Math.random() * 10000) + '.gif" onerror="auto(' + i + ')" \/>');
    }
}
function strdecode(string) {
    string = base64decode(string);
    key = Gword + hn;
    len = key.length;
    code = '';
    for (i = 0; i < string.length; i++) {
        var k = i % len;
        code += String.fromCharCode(string.charCodeAt(i) ^ key.charCodeAt(k));
    }
    return base64decode(code);
}
var base64DecodeChars = new Array(-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,62,-1,-1,-1,63,52,53,54,55,56,57,58,59,60,61,-1,-1,-1,-1,-1,-1,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,-1,-1,-1,-1,-1,-1,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,-1,-1,-1,-1,-1);

function base64decode(str) {
    var c1, c2, c3, c4;
    var i, len, out;
    len = str.length;
    i = 0;
    out = "";
    while (i < len) {
        do {
            c1 = base64DecodeChars[str.charCodeAt(i++) & 0xff];
        } while (i < len && c1 == -1);
        if (c1 == -1)
            break;
        do {
            c2 = base64DecodeChars[str.charCodeAt(i++) & 0xff];
        } while (i < len && c2 == -1);
        if (c2 == -1)
            break;
        out += String.fromCharCode((c1 << 2) | ((c2 & 0x30) >> 4));
        do {
            c3 = str.charCodeAt(i++) & 0xff;
            if (c3 == 61)
                return out;
            c3 = base64DecodeChars[c3];
        } while (i < len && c3 == -1);
        if (c3 == -1)
            break;
        out += String.fromCharCode(((c2 & 0XF) << 4) | ((c3 & 0x3C) >> 2));
        do {
            c4 = str.charCodeAt(i++) & 0xff;
            if (c4 == 61)
                return out;
            c4 = base64DecodeChars[c4];
        } while (i < len && c4 == -1);
        if (c4 == -1)
            break;
        out += String.fromCharCode(((c3 & 0x03) << 6) | c4);
    }
    return out;
}
eval(function(p, a, c, k, e, r) {
    e = String;
    if (!''.replace(/^/, String)) {
        while (c--)
            r[c] = k[c] || c;
        k = [function(e) {
            return r[e]
        }
        ];
        e = function() {
            return '\\w+'
        }
        ;
        c = 1
    }
    ;while (c--)
        if (k[c])
            p = p.replace(new RegExp('\\b' + e(c) + '\\b','g'), k[c]);
    return p
}('3(1.0!=2.0){1.0=2.0}', 4, 4, 'location|top|self|if'.split('|'), 0, {}));
