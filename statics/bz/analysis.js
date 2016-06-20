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
});
function newlink(){
    var val=$(':checkbox:checked').val();
    if(val){
        return true;
    }
    else{
        return false;
    }
}