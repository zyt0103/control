/**
 * Created by zyt on 2016/6/14.
 */
$(function() {
    //验证 function,type_name_de
    var $addOKDemodul = $("#addOKDemodul");
    $("#addModalDemodul").on('focus', "#type_name_de", function () {
        $("#addOKDemodul").attr("disabled",false);
        document.getElementById("type_name_de").style.background = "white";
    });
    $("#addModalDemodul").on('blur', "#type_name_de", function () {
        var text1 = document.getElementById("type_name_de").value;

        if (text1.length > 20 || text1 == null || text1 == "") {
            document.getElementById("type_name_de").style.background = "orangered";
            document.getElementById("type_name_decheck").style.visibility = "hidden";
            $("#addOKDemodul").attr("disabled",true);
        }
        else {
            document.getElementById("type_name_de").style.background = "white";
            $("#addOKDemodul").attr("disabled",false);
            document.getElementById("type_name_decheck").style.visibility = "visible";
        }
    });
    //$('#addModalDemodul').on('click','#addOKDemodul',function() {
    //    if (!($("#addOKDemodul").disable)) {
    //        var addStringDemodul = {};
    //        var $showTableDemodul = $("#showTableDemodul")
    //        var $addTableDemodulTr = $("#addTableDemodul").find("tr");
    //        for (var i = 1; i < $addTableDemodulTr.length; i++) {
    //            addStringDemodul[i] = $($addTableDemodulTr[i]).find("option").val();
    //        }
    //        addStringDemodul[0] = $($addTableDemodulTr[0]).find("input").val();
    //        var strTipDemodul;
    //        strTipDemodul = "<tr><td class='table-time'><input type='checkbox'>" + addStringDemodul[0] +
    //            "</td><td class='table-time'>" + addStringDemodul[1] +
    //            "</td><td class='table-time'>" + addStringDemodul[2] +
    //            "</td><td class='table-time'>" + addStringDemodul[3] +
    //            "</td><td class='table-time'>" + addStringDemodul[4] +
    //            "</td></tr>"
    //        $(strTipDemodul).appendTo($showTableDemodul);
    //        $("#addClose").click();
    //    }
    //});
    function ajCreateDemodulType(){
        var protocol_num;
        var sync_type_num;
        if($('#protocol_de').val()=="GMSK"){
            protocol_num="1";
        }
        if($('#sync_type').val()=="DEFAULT"){
            sync_type_num="1";
        }
        var param={
            "demod_type_name": $('#type_name_de').val(),
            "ant_num":$('#ant_num_de').val(),
            "protocol":protocol_num,
            "sync_type":sync_type_num,
        }
        $.ajax({
            type: 'POST',
            dataType: 'JSON',
            url: '/demod/demodtypecreate',
            success: function (res) {
                if (res.ret_code == 0) {
                    alert("创建解调方式成功！")
                }
                else {
                    alert("创建解调方式不成功！")
                }
                //$('input:checkbox').removeAttr("checked");
                //location.reload();
            },
            data: JSON.stringify(param),
            headers: {
                'X-CSRFToken': 'qUgKcDvT6UcljCIfYvTyHNMMIGtGuqXu',
                'Content-Type': 'application/json',
            }
        });
    }
    function CreateDemodulType(){
        ajCreateDemodulType();
        $("#addClose").click();
    }
    $("#addModalDemodul").on("click","#addOKDemodul",CreateDemodulType);

     function ajDeleteDemodulType() {
         var type_id=$('input:checkbox:checked').parent().next();
         var length=type_id.length;
         if(length == 1){
             var type = new Array();
             type[0]=type_id.html();
             var param = {"demod_type_id":type}
         }
         else{
             var type_id = new Array();
             for(var i=0; i<length; i++){
                 type_id[i]=type_id[i].innerHTML;
             }
             var param = {"demod_type_id":type_id}
         }
         $.ajax({
            type: 'POST',
            dataType: 'JSON',
            url: '/demod/demodtypedelete',
            success: function (res) {
                if (res.ret_code == 0) {
                    alert("删除方式成功！")
                }
                else {
                    alert("删除方式不成功！")
                }
                $('input:checkbox').removeAttr("checked");
                //location.reload();
            },
            data: JSON.stringify(param),
            headers: {
                //'X-CSRFToken': 'qUgKcDvT6UcljCIfYvTyHNMMIGtGuqXu',
                'Content-Type': 'application/json',
            }
         });
    }
    $("#deleteDemodul").bind("click",function(){
        var val=$(':checkbox:checked').val();
        if(val) {
            ajDeleteDemodulType();
        }
    });
});
