
// var e = new X()[$_CBEEc(342)](this[$_CBEEc(742)](t));

// this[$_CBEEc(742)](t)
function random_() {
    var data = ''
    for(var i=0; i<4; i++){
        data += (65536 * (1 + Math["random"]()) | 0)["toString"](16)["substring"](1)
    }
    return data;
}
