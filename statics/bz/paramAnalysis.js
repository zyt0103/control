/**
 * Created by zyt on 2016/7/6.
 */
$(function() {
    $("body").on("click", "#ves_distribute", function () {
        $('#picture2').empty();
        if ($('#picture1').text()) {
            return false;
        }
        else {
            $('#picture1').load("/pic?pic=1", function () {
                //$.getScript('statics/bz/x3dom.js');
                //$('#picture1').siblings().attr("class","hidden");

            });
        }
    });
    $("body").on("click", "#power", function () {
        $('#picture1').empty();
        if ($('#picture2').text()) {
            return false;
        }
        else {
            $('#picture2').load("/pic?pic=2", function () {
                //$.getScript('statics/bz/x3dom.js');
                //$('#picture2').siblings().attr("class","hidden");

            });
        }
    });
});


