/**
 * Created by zyt on 2016/7/6.
 */
$(function() {
    //if (param=2){
    //        $('#picture3').load("/pic?param=3", function () {
    //        //$.getScript('statics/bz/x3dom.js');
    //        $('#delay').attr("class","color");
    //
    //    });
    //}
    $("body").on("click", "#power", function () {
        window.location.href="paramAnalysis.html?signal_id=signal-iaythb8m&param=2";
        $('#picture2').load("/pic?param=2", function () {
            //$.getScript('statics/bz/x3dom.js');
            $('#power').attr("class","color");

        });
    });
});

function GetRequest(strName) {
    var strHref = window.location.href; //获取Url字串
    var intPos = strHref.indexOf("?");  // 参数开始位置，检索字符串
    var strRight = strHref.substr(intPos + 1);//返回一个新的字符串，从起始到结尾
    var arrTmp = strRight.split("&"); //参数分割符
    for(var i = 0; i < arrTmp.length; i++) {
              var arrTemp = arrTmp[i].split("=");
              if(arrTemp[0].toUpperCase() == strName.toUpperCase()) return arrTemp[1];
        }
    return"";
}
 var signal_id=GetRequest("signal_id");
 var param=GetRequest("param");

