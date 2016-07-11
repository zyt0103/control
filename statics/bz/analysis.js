/**
 * Created by zyt on 2016/6/17.
 */
$(function() {
    $(":checkbox").on('mouseleave',function() {
        var val = $(':checkbox:checked').val();
        if (val) {
            $("#paramAnalysis").removeClass("noclick");
            $("#demodulResult").removeClass("noclick");
            $("#checkPro").removeClass("noclick");
        }
        else {
            //$("#demoul").attr("disabled",true)
            $("#paramAnalysis").addClass("noclick");
            $("#demodulResult").addClass("noclick");
            $("#checkPro").addClass("noclick");
        }
    })
    $(":checkbox").click(function() {
        $(":checkbox").each(function () {
            $(this).prop("checked",false);
        });
        $(this).prop("checked",true);
    });
    $("#paramAnalysis").click(function(){
        var val=$(':checkbox:checked').val();
        var signal_id=$('input:checkbox:checked').parent().text();
        if(val){
            window.open("paramAnalysis.html?signal_id="+signal_id+"&"+"param=3","_blank");
            return true;
        }
        else{
            return false;
        }
    });
    $("#demodulResult").click(function(){
        var val=$(':checkbox:checked').val();
        var signal_id=$('input:checkbox:checked').parent().text();
        var demod_type_id=$('input:checkbox:checked').parent().next().text();
        if(val){
            window.open("demodulResult.html?signal_id="+signal_id+"&"+"demod_type_id="+demod_type_id,"_blank");
            return true;
        }
        else{
            return false;
        }
    });
});
