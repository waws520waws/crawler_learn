var aa = function (t){
    // console.log(this)
    t()
}

var xx = function (){
    console.log('xxx')
}

aa(xx);
