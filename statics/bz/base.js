/**
 * Created by baishengmei on 2016/5/13.
 */

$(function(){


    //delete function
    var $modul_contain = $("#modul_contain");
    var $delete = $("#delete");
	//function check(){
     //   if ($(".modul_contain tbody input").is(':checked')) {
	//		alert("aa")
	//	}
	//}
    //$delete.bind("click", function () {
     //   $(".modul_contain tbody input:checked").parent().parent().remove();
    //});

    //add function
    var $add = $("#add");
    var $addTable = $("#addTable");
    var $addTableTr = $("#addTable").find("tr");
    var $addOK = $("#addOK");
    var $showTable = $("#showTable");
    var $addClose = $("#addClose");
    //function addMessage(){
        //var addString={};
        //for(var i=0; i<$addTableTr.length; i++){
        //    addString[i] = $($addTableTr[i]).find("input").val();
        //    addString[8] = $($addTableTr[8]).find("option").val();
        //}
        //var strTip;
        //strTip = "<tr><td class='table-time'><input type='checkbox'>"+addString[0]+
        //         "</td><td class='table-time'>"+addString[1]+
        //         "</td><td class='table-time'>"+addString[2]+
        //         '</td><td class="table-time">'+addString[3]+
        //         '</td><td class="table-time">'+addString[4]+
        //         '</td><td class="table-time">'+addString[5]+
        //         '</td><td class="table-time">'+addString[6]+
        //         '</td><td class="table-time">'+addString[7]+
        //         '</td><td class="table-time">'+addString[8]+
        //         //'</td><td class="table-time">'+addString[9]+
        //         //'</td><td class="table-time">'+addString[10]+
			//     //'</td><td class="table-time">'+addString[11]+
			//     //'</td><td class="table-time">'+addString[12]+
			//     //'</td><td class="table-time">'+addString[13]+
        //         "</td></tr>"
        //$(strTip).appendTo($showTable);
        ////for(var j=0; j<$addTableTr.length; j++){
        ////$($addTableTr[j]).find("input").val("");
        ////}
       //$("#addClose").click();
  //  }

    ////modulation page
    //var $modul_btn = $("#modul_btn");
    //var $ais_modulation = $("#ais_modulation");
    //$modul_btn.bind("click", function(){
    //    $ais_modulation.attr("class", "show").siblings().attr("class", "hidden");
    //    $modul_btn.attr("class", "active").siblings().attr("class", "");
    //});
    //
    ////demodulation page
    //var $ais_demodulation = $("#ais_demodulation");
    //var $demodul = $("#demodul"); //demodulation button in the topbar
    //var $demodul_btn = $("#demodul_btn");
    ////$demodul.bind("click", function(){
    ////    $ais_demodulation.attr("class", "show").siblings().attr("class","hidden");
    ////    $demodul_btn.attr("class", "active").siblings().attr("class", "");
    ////});
    //$demodul_btn.bind("click", function(){
    //    $ais_demodulation.attr("class", "show").siblings().attr("class", "hidden");
    //    $demodul_btn.attr("class", "active").siblings().attr("class", "");
    //});
    //
    ////analysis page
    //var $analy_btn = $("#analy_btn");
    //var ais_analysis = $("#ais_analysis");
    //$analy_btn.bind("click", function(){
    //    ais_analysis.attr("class", "show").siblings().attr("class", "hidden");
    //    $analy_btn.attr("class", "active").siblings().attr("class", "");
    //});
    //

      //验证 function,filename
    var $filename = $("#filename");
    $("#addModal1").on('focus',"#filename", function() {
    	addOK.disabled = false;
    	document.getElementById("filename").style.background="white";
    })
    $("#addModal1").on('blur',"#filename", function() {
	    var text=document.getElementById("filename").value; 
	   
	    if(text.length>20||text==null||text==""){
	        document.getElementById("filename").style.background="orangered";
	        document.getElementById("filenamecheck").style.visibility="hidden";
	    }
	    else{
			document.getElementById("filename").style.background="white";
			addOK.disabled = false;
			document.getElementById("filenamecheck").style.visibility="visible";
		}
    });
    //验证 function,lat
    var $lat = $("#lat");
    $("#addModal1").on('focus',"#lat", function() {
		addOK.disabled = false;
		document.getElementById("lat").style.background = "white";
	});
    $("#addModal1").on('blur',"#lat", function(){
	    var text=document.getElementById("lat").value; 
	    var regExp = /^-?([1-9]\d*|[1-9]\d*\.\d*[1-9]\d*|0\.\d*[1-9]\d*|0?\.0+|0)$/;
		if((!regExp.test(text))||text>90||text<-90){
	        document.getElementById("lat").style.background="orangered";
//	        $("#latcheck").display="none";
	        document.getElementById("latcheck").style.visibility="hidden";
	    }
	    else{
			document.getElementById("lat").style.background="white";
			addOK.disabled=false;
			document.getElementById("latcheck").style.visibility="visible";

		}
    });
     //验证 function,lon
    var $lon = $("#lon");
    $("#addModal1").on('focus',"#lon", function() {
    	addOK.disabled=false;
    	document.getElementById("lon").style.background="white";
    })
    $("#addModal1").on('blur',"#lon", function() {
	    var text=document.getElementById("lon").value; 
//	    var regExp = /^-?\d+$/; 
	    var regExp = /^-?([1-9]\d*|[1-9]\d*\.\d*[1-9]\d*|0\.\d*[1-9]\d*|0?\.0+|0)$/;
		if((!regExp.test(text))||text>180||text<-180){
	        document.getElementById("lon").style.background="orangered";
	         document.getElementById("loncheck").style.visibility="hidden";
	    }
	    else{
			document.getElementById("lon").style.background="white";
			document.getElementById("loncheck").style.visibility="visible";
			addOK.disabled=false;
		}
    });
    
     //验证 function,height
    var $height = $("#height");
    $("#addModal1").on('focus',"#height", function() {
    	addOK.disabled=false;
    	document.getElementById("height").style.background="white";
    })
    $("#addModal1").on('blur',"#height", function() {
	    var text=document.getElementById("height").value; 
//	    var regExp = /^\d+$/; 
	    var regExp = /^([1-9]\d*|[1-9]\d*\.\d*[1-9]\d*|0\.\d*[1-9]\d*)$/;
		if(!regExp.test(text)){
	        document.getElementById("height").style.background="orangered";
	        document.getElementById("heightcheck").style.visibility="hidden";
	    }
	    else{
			document.getElementById("height").style.background="white";
			document.getElementById("heightcheck").style.visibility="visible";
			addOK.disabled=false;
		}
    });
    3
     //验证 function,vesnum
    var $vesnum = $("#vesnum");
    $("#addModal1").on('focus',"#vesnum", function() {
    	addOK.disabled=false;
    	document.getElementById("vesnum").style.background="white";
    })
    $("#addModal1").on('blur',"#vesnum", function() {
	    var text=document.getElementById("vesnum").value; 
	    var regExp = /^([1-9]\d*)$/;
		if(!regExp.test(text)){
	        document.getElementById("vesnum").style.background="orangered";
	        document.getElementById("vesnumcheck").style.visibility="hidden";
	    }
	    else{
			document.getElementById("vesnum").style.background="white";
			document.getElementById("vesnumcheck").style.visibility="visible";
			addOK.disabled=false;
		}
    });
    
     //验证 function,obtime
    var $obtime = $("#obtime");
    $("#addModal1").on('focus',"#obtime", function() {
    	addOK.disabled=false;
    	document.getElementById("obtime").style.background="white";
    })
    $("#addModal1").on('blur',"#obtime", function() {
	    var text=document.getElementById("obtime").value; 
	    var regExp = /^([1-9]\d*|[1-9]\d*\.\d*[1-9]\d*|0\.\d*[1-9]\d*)$/; 
	    if(!regExp.test(text)){
	        document.getElementById("obtime").style.background="orangered";
	        document.getElementById("obtimecheck").style.visibility="hidden";
	    }
	    else{
			document.getElementById("obtime").style.background="white";
			document.getElementById("obtimecheck").style.visibility="visible";
			addOK.disabled=false;
		}
    });
    
     //验证 function,ant_pitch
    var $ant_pitch = $("#ant_pitch");
    $("#addModal1").on('focus',"#ant_pitch", function() {
    	addOK.disabled=false;
    	document.getElementById("ant_pitch").style.background="white";
    })
    $("#addModal1").on('blur',"#ant_pitch", function() {
	    var text=document.getElementById("ant_pitch").value; 
	    var regExp = /^-?([1-9]\d*|[1-9]\d*\.\d*[1-9]\d*|0\.\d*[1-9]\d*|0?\.0+|0)$/;
		if((!regExp.test(text))||text>180||text<-180){
	        document.getElementById("ant_pitch").style.background="orangered";
	        document.getElementById("ant_pitchcheck").style.visibility="hidden";
	    }
	    else{
			document.getElementById("ant_pitch").style.background="white";
			document.getElementById("ant_pitchcheck").style.visibility="visible";
			addOK.disabled=false;
		}
    });
    
     //验证 function,ant_azimuth
    var $ant_azimuth = $("#ant_azimuth");
    $("#addModal1").on('focus',"#ant_azimuth", function() {
    	addOK.disabled=false;
    	document.getElementById("ant_azimuth").style.background="white";
    })
    $("#addModal1").on('blur',"#ant_azimuth", function() {
	    var text=document.getElementById("ant_azimuth").value; 
	    var regExp = /^-?([1-9]\d*|[1-9]\d*\.\d*[1-9]\d*|0\.\d*[1-9]\d*|0?\.0+|0)$/;
	    if((!regExp.test(text))||text>360||text<0){
	        document.getElementById("ant_azimuth").style.background="orangered";
//	       	$("#ant_azimuthcheck").removeClass("checkV").addClass("check");
			document.getElementById("ant_azimuthcheck").style.visibility="hidden";
	    }
	    else{
			document.getElementById("ant_azimuth").style.background="white";
//			$("#ant_azimuthcheck").removeClass("check").addClass("checkV");
			document.getElementById("ant_azimuthcheck").style.visibility="visible";
			addOK.disabled=false;
		}
    });
	//封装blurValidate()函数
	function blurValidate(elemId,elemCheckId,regExp){
		var text=document.getElementById(elemId).value;
	    if(!regExp.test(text)){
	        document.getElementById(elemId).style.background="orangered";
			document.getElementById(elemCheckId).style.visibility="hidden";
	    }
	    else{
			document.getElementById(elemeId).style.background="white";
			document.getElementById(elemCheckId).style.visibility="visible";
			addOK.disabled=false;
		}
	}



	 //验证 function,snr
    //var $snr = $("#snr");
    //$("#addModal1").on('focus',"#snr", function() {
    //	addOK.disabled=false;
    //	document.getElementById("snr").style.background="white";
    //})
    //$("#addModal1").on('blur',"#snr", function() {
	 //   var text=document.getElementById("snr").value;
	 //   var regExp =/^([1-9]\d*|[1-9]\d*\.\d*[1-9]\d*|0\.\d*[1-9]\d*)$/;
	 //   if(!regExp.test(text)){
	 //       document.getElementById("snr").style.background="orangered";
		//	document.getElementById("snrcheck").style.visibility="hidden";
	 //   }
	 //   else{
		//	document.getElementById("snr").style.background="white";
		//	document.getElementById("snrcheck").style.visibility="visible";
		//	addOK.disabled=false;
		//}
    //});
	 var $snr = $("#snr");
    $("#addModal1").on('focus',"#snr", function() {
    	addOK.disabled=false;
    	document.getElementById("snr").style.background="white";
    })
    $("#addModal1").on('blur',"#snr", function() {
	    blurValidate("snr","snrCheck",/^([1-9]\d*|[1-9]\d*\.\d*[1-9]\d*|0\.\d*[1-9]\d*)$/);
    });
      ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //校验lat字段是否提交
    function validateFormlat(){
    	var flag = true;
    	var regExp = /^-?([1-9]\d*|[1-9]\d*\.\d*[1-9]\d*|0\.\d*[1-9]\d*|0?\.0+|0)$/;
    	var text=document.getElementById("lat").value;
		if((!regExp.test(text))||text>90||text<-90){
	        document.getElementById("lat").style.background="orangered";
	        flag = false;
	        addOK.disabled=true;
	    } 
	    else{
			document.getElementById("lat").style.background="white";	
			addOK.disabled=false;
		}
	    return flag;
    }
    //校验lon字段 是否提交
    function validateFormlon(){
    	var flag = true;
    	var regExp = /^-?([1-9]\d*|[1-9]\d*\.\d*[1-9]\d*|0\.\d*[1-9]\d*|0?\.0+|0)$/;
    	var text=document.getElementById("lon").value;
		if((!regExp.test(text))||text>180||text<-180){
	        document.getElementById("lon").style.background="orangered";
	        flag = false;
	        addOK.disabled=true;
	    } 
	    else{
			document.getElementById("lon").style.background="white";	
			addOK.disabled=false;
		}
	    return flag;
    }
    //校验filename字段是否提交
    function validateFormfilename(){
    	var flag = true;
		var text=document.getElementById("filename").value;
	    if(text.length>20||text==null||text==""){
	        document.getElementById("filename").style.background="orangered";
	        flag = false;
	        $addOK.attr("disabled",true);
	    }
	    else{
			document.getElementById("filename").style.background="white";
			$addOK.attr("disabled",false);
		}
	    return flag;
    }
    //校验height字段是否提交
    function validateFormheight(){
    	var flag = true;
    	var text=document.getElementById("height").value; 
	    var regExp = /^([1-9]\d*|[1-9]\d*\.\d*[1-9]\d*|0\.\d*[1-9]\d*)$/;
		if(!regExp.test(text)){
	        document.getElementById("height").style.background="orangered";
	        flag = false;
	        addOK.disabled=true;
	    }
	    else{
			document.getElementById("height").style.background="white";
			addOK.disabled=false;
		}
	    return flag;
    }
    //校验vesnum字段是否提交
    function validateFormvesnum(){
    	var flag = true;
    	var text=document.getElementById("vesnum").value; 
	    var regExp = /^([1-9]\d*)$/;
		if(!regExp.test(text)){
	        document.getElementById("vesnum").style.background="orangered";
	        flag = false;
	        addOK.disabled=true;
	    }
	    else{
			document.getElementById("vesnum").style.background="white";
			addOK.disabled=false;
		}
	    return flag;
    }
    //校验obtime字段是否提交
    function validateFormobtime(){
    	var flag = true;
    	var text=document.getElementById("obtime").value; 
	    var regExp = /^([1-9]\d*|[1-9]\d*\.\d*[1-9]\d*|0\.\d*[1-9]\d*)$/;
		if(!regExp.test(text)){
	        document.getElementById("obtime").style.background="orangered";
	        flag = false;
	        addOK.disabled=true;
	    }
	    else{
			document.getElementById("obtime").style.background="white";
			addOK.disabled=false;
		}
	    return flag;
    }
    //校验ant_pitch字段是否提交
    function validateFormant_pitch(){
    	var flag = true;
    	var text=document.getElementById("ant_pitch").value; 
	    var regExp = /^-?([1-9]\d*|[1-9]\d*\.\d*[1-9]\d*|0\.\d*[1-9]\d*|0?\.0+|0)$/;
		if((!regExp.test(text))||text>180||text<-180){
	        document.getElementById("ant_pitch").style.background="orangered";
	        flag = false;
            addOK.disabled=true;
	    }
	    else{
			document.getElementById("ant_pitch").style.background="white";
			addOK.disabled=false;
		}
	    return flag;
    }
    //校验ant_azimuth字段是否提交
    function validateFormant_azimuth(){
    	var flag = true;
		var text=document.getElementById("ant_azimuth").value;
	    var regExp = /^-?([1-9]\d*|[1-9]\d*\.\d*[1-9]\d*|0\.\d*[1-9]\d*|0?\.0+|0)$/;
		if((!regExp.test(text))||text>360||text<0){
	        document.getElementById("ant_azimuth").style.background="orangered";
	        flag = false;
	        addOK.disabled=true;
	    }
	    else{
			document.getElementById("ant_azimuth").style.background="white";
			addOK.disabled=false;
		}
	    return flag;
    }
	//校验snr字段是否提交
    function validateFormsnr(){
    	var flag = true;
		var text=document.getElementById("snr").value;
	    var regExp =/^([1-9]\d*|[1-9]\d*\.\d*[1-9]\d*|0\.\d*[1-9]\d*)$/;
		if((!regExp.test(text))){
	        document.getElementById("snr").style.background="orangered";
	        flag = false;
	        addOK.disabled=true;
	    }
	    else{
			document.getElementById("snr").style.background="white";
			addOK.disabled=false;
		}
	    return flag;
    }
    //校验是否提交
    function validateForm(){
    	var flag = false;
    	var flag3 = validateFormfilename();
    	var flag4 = validateFormlat();
    	var flag5 = validateFormlon();
    	var flag6 = validateFormheight();
    	var flag7 = validateFormvesnum();
    	var flag8 = validateFormobtime();
    	var flag9 = validateFormant_pitch();
    	var flag10 = validateFormant_azimuth();
		var flag11 = validateFormsnr();
    	if(flag3&&flag4&&flag5&&flag6&&flag7&&flag8&&flag9&&flag10&&flag11){
    		flag=true;
    		addOK.disabled=false;
            //document.getElementById("latcheck").style.visibility="hidden";
            //document.getElementById("loncheck").style.visibility="hidden";
            //document.getElementById("filenamecheck").style.visibility="hidden";
            //document.getElementById("heightcheck").style.visibility="hidden";
            //document.getElementById("vesnumcheck").style.visibility="hidden";
            //document.getElementById("obtimecheck").style.visibility="hidden";
            //document.getElementById("ant_pitchcheck").style.visibility="hidden";
            //document.getElementById("ant_azimuthcheck").style.visibility="hidden";
			//document.getElementById("snrcheck").style.visibility="hidden";
			//document.getElement("snrcheck").style.visibility="hidden";
// 			$("table span > span").removeClass("checkV").addClass('check');
    		
    	}
    	else{
    		addOK.disabled=true;
    	}
    	return flag;
    }

    $('#addModal1').on('click','#addOK',function(){
        var flag = validateForm();
        if(flag){
            ajCreateSignal();
            $("#addClose").click();
        }
    });

    function ajCreateSignal(){
        var param={
        "name_signal":$("#filename").val(),
        "lat":$("#lat").val(),
        "lon":$("#lon").val(),
        "height":$("#height").val(),
        "vesnum":$("#vesnum").val(),
        "obtime":$("#obtime").val(),
        "ant_pitch":$("#ant_pitch").val(),
        "ant_azimuth":$("#ant_azimuth").val(),
        "ant-type":$("#ant_type").val(),
        "channel_type":$("#channel_type").val(),
        "channel_num":$("#channel_num").val(),
        "protocol":$("#protocol").val(),
        "snr":$("#snr").val(),
        "packagenum":$("#packagenum").val(),
        "distri_mode":$("#distri_mode").val(),
        }
        $.ajax({
            type: 'POST',
            dataType: 'JSON',
            url: '/modu/createsignal',
            success:function(res) {
                if(res.ret_code==0){
                    location.reload();
                    //if(res.total_count==1){
                    //    var signal_id = res.ret_set;
                    //    var signal_name =$("#filename").val();
                    //    var $showTableTh = $("#showTable").find("th");
                    //    var addString={};
                    //    for(var i=0; i<$showTableTh.length; i++){
                    //        addString[i] = 0;
                    //        addString[1] = signal_id;
                    //        addString[0] = signal_name+"<br>"+"_signal";
                    //    }
                    //    var strTip;
                    //    strTip = "<tr><td class='table-time'><input type='checkbox'>"+addString[0]+
                    //             "</td><td class='table-time'>"+addString[1]+
                    //             "</td><td class='table-time'>"+addString[2]+
                    //             "</td><td class='table-time'>"+addString[3]+
                    //             "</td><td class='table-time'>"+addString[4]+
                    //             "</td><td class='table-time'>"+addString[5]+
                    //             "</td></tr>"
                    //    $(strTip).appendTo($showTable);
                    //}
                    //else{
                    //    var total_count = res.total_count;
                    //    var signal_id = res.ret_set[0];
                    //    var signal_name =$("#filename").val();
                    //    var $showTableTh = $("#showTable").find("th");
                    //    var addString={};
                    //    for(var j=0;j<total_count;j++){
                    //        for(var i=0; i<$showTableTh.length;i++){
                    //            addString[i] = 0;
                    //            addString[1] = signal_id[j];
                    //            addString[0] = signal_name+"_"+j;
                    //        }
                    //        var strTip;
                    //        strTip = "<tr><td class='table-time'><input type='checkbox'>"+addString[0]+
                    //                 "</td><td class='table-time'>"+addString[1]+
                    //                 "</td><td class='table-time'>"+addString[2]+
                    //                 "</td><td class='table-time'>"+addString[3]+
                    //                 "</td><td class='table-time'>"+addString[4]+
                    //                 "</td><td class='table-time'>"+addString[5]+
                    //                 "</td></tr>"
                    //        $(strTip).appendTo($showTable);
                    //    }
                    //}
                }
                else{
                    alert("创建信号不成功！")
                }
            },
            data: JSON.stringify(param),
            headers: {
                'Content-Type': 'application/json'
            }
	    });
	//var successFun = function(res) {
	//		if(res.ret_code==0){
	//		    alert("sucess!")
	//		}
	//		else{
	//			alert("创建信号不成功！")
	//		}
	//	};
    }

    $('#addModalType').on('click','#addOK',function(){
        var val=$(':radio[name="type"]:checked').val();
        if(val){
            ajDemodul();
            $("#addClose").click();
        }
    });

    function ajDemodul() {
        var elem= $('input:radio[name="type"]:checked').parent().next().next().next().next().html()
        var signal=$('input:checkbox:checked').parent().next().children();
                    //$('input:checkbox:checked').parent().next()[0].children;
        var length =signal.length;
        if(length==1){
            var param = {
            "signal_id":signal.html(),
			"demod_type_id": elem,
            }
        }
        else{
            var signal_id = new Array();
            for(var i=0; i<length; i++){
                 signal_id[i]=signal[i].innerHTML;
            }
            var param = {
                "signal_id":signal_id,
                "demod_type_id": elem,
            }
        }

        $.ajax({
            type: 'POST',
            dataType: 'JSON',
            url: '/demod/demodsignal',
            success: function (res) {
                if (res.ret_code == 0) {
                    alert("信号开始解调！")
                }
                else {
                    alert("信号不能解调！")
                }
                $('input:checkbox').removeAttr("checked");
                //location.reload();
            },
            data: JSON.stringify(param),
            headers: {
                'Content-Type': 'application/json',
            }
        });
    }
    function check1(){
        var val=$(':checkbox:checked').val();
        //var val=$(':checkbox').is(":checked");
        if(val) {
            $("#delete").attr("disabled",false);
            $("#demodul").attr("disabled",false);
            $("#deleteDemodul").attr("disabled",false);
        }
        else{
            $("#demodul").attr("disabled",true);
            $("#delete").attr("disabled",true);
            $("#deleteDemodul").attr("disabled",true);
        }
    }
    $(":checkbox").on('mouseout',check1);
    $("#demodul").bind('mouseover',check1);
    $("#allchioce").on('mouseout',check1);
    $("#quitchioce").bind('mouseout',check1);
    function addmodalType(){
        var val=$(':checkbox:checked').val();
        var antnumArrey=$('input:checkbox:checked').parent().next().next().next().next().next().next();
        var antnum=new Array();
        $.each(antnumArrey,function(i,item){
            antnum[i]=item.innerHTML;
        });
        var minAntNum=Math.min.apply(Math,antnum);
        if(val){
            $('#addModalType').load('/addModalType.html?minAntNum='+minAntNum);
        }
    }
    $("#demodul").bind('click',addmodalType);

    $("#allchioce").on("click",function(){
        $('input:checkbox').prop("checked",true);
    });
    $("#quitchioce").on("click",function(){
        $('input:checkbox').prop("checked",false);
    });

     function ajDeleteSignal() {
         var signal=$('input:checkbox:checked').parent().next().children();
                    //$('input:checkbox:checked').parent().next()[0].children;
         var length=signal.length;
         if(length == 1){
             var param = {"signal_id":signal.html(),}
         }
         else{
             var signal_id = new Array();
             for(var i=0; i<length; i++){
                 signal_id[i]=signal[i].innerHTML;
             }
             var param = {"signal_id":signal_id}
         }
         $.ajax({
            type: 'post',
            dataType: 'JSON',
            url: '/modu/delete',
            success: function (res) {
                if (res.ret_code == 0) {
                    alert("删除信号成功！")
                }
                else {
                    alert("删除信号不成功！")
                }
                $('input:checkbox').removeAttr("checked");
                location.reload();
            },
            data: JSON.stringify(param),
            headers: {
                //'X-CSRFToken': 'qUgKcDvT6UcljCIfYvTyHNMMIGtGuqXu',
                'Content-Type': 'application/json',
            }
         });
    }
    $("#delete").bind("click",function(){
        var val=$(':checkbox:checked').val();
        if(val) {
            ajDeleteSignal();
        }
    });


});



function addmodal(){
	$('#addModal1').load('/addmodal.html');
}
function addmodalDemodul(){
	$('#addModalDemodul').load('/addModalDemodul.html');
}


//post发送前加入cookie
$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
     //console.log("ajax send")
});
//$(document).ajaxStart(function() {
//    $("#load").show();
//
//});
//$(document).ajaxStop(function() {
//    $("#load").hide();
//
//});
//function myrefresh()
//{
//       parent.location.reload();
//}
//setTimeout('myrefresh()',10000);


