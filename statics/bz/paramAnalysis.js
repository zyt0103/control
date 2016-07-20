/**
 * Created by zyt on 2016/7/6.
 */
$(function() {
    function GetRequest(strName){
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
    var param_Array=$("ul button span");
    var param_name=new Array();
    var param_num=new Array();
    $.each(param_Array,function(i,item){
        param_name[i]="#"+item.id;
        param_num[i]=i+1;
        if(i==param-1){
            $(param_name[i]).attr("class","color");
        }
        $("body").on("click", param_name[i], function () {
            window.location.href="paramAnalysis.html?signal_id="+signal_id+"&param="+param_num[i];
        //$.getScript('statics/bz/x3dom.js');
         });
    });
});



