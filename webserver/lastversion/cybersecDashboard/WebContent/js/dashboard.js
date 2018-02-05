var formVisiblity = false;

function showLoader(){ 
	$('.blackWindow').fadeIn(200);
	$(".loader").css("display","block"); 
}
function hideLoader(){ 
	$('.blackWindow').fadeOut(200);
	$(".loader").css("display","none"); 
}

$.ajaxSetup({
    beforeSend: showLoader,
    complete: hideLoader
});

$("#btn_logOut").click(function(){
	$.post("logout");
});

$('#btnHideSelects').click(function(){
	$('form').toggle("slow");
	if(formVisiblity) {
		$('#btnHideSelects').text('Down');
		formVisiblity = false;
		$('.col-xs-12>h3').hide();
		$('#btnHideSelects').css('margin-top',"10px");
	}
	else{
		$('#btnHideSelects').text('Up');
		formVisiblity = true;
		$('.col-xs-12>h3').show();
		$('#btnHideSelects').css('margin-top',"0");
	}
});

function showTopMessage(msg){
	$('.top-message').html(msg);
	$(".top-message").slideToggle("slow");
	setTimeout(function(){ $(".top-message").slideToggle("slow"); }, 4000);
}
$('td').each(function() {
	 var col_val = $(this).text();
	 console.log(col_val);
	                      if (col_val == "Low") {
	                           //console.log(col_val);
								$(this).css('color','#009900'); //the selected class colors the row green//
						} else if (col_val == "Medium") {
	                            console.log(col_val);
								$(this).css('color','#ffff66'); 
							}else if (col_val == "High"){
	                            $(this).css('color','#ff0000')
	                             console.log(col_val);};     
	 });