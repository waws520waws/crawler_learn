function t(){
    return (65536 * (1 + Math["random"]()) | 0)["toString"](16)["substring"](1)
}

function rt(){
    return t() + t() + t() + t();
}

var data = '';
for(var i=0; i<4; i++){
    data += (65536 * (1 + Math["random"]()) | 0)["toString"](16)["substring"](1);
}
