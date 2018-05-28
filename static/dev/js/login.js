//language change
$( "#language_selection" ).change(function() {
	translateLanguage( this.value);
	});

//Login check server side
$("#login_check").submit(function( event ) {
	event.preventDefault();
	if (login_validation()){
		var user_name = $('#username').val();
		var password = $('#password').val();
		var datas = {"data":[{"username":user_name,"password":password}]};
		$.ajax({
			type  : 'POST',
			url   : '/login_check/',
			async : false,
			data: JSON.stringify(datas),
			csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val(),
			timeout : 10000,
			async:false,
		}).done( function(json_data) {
			alert(json_data)
			var data = JSON.parse(json_data);
			if(data['status'] == "M1"){
				window.location.href = 'dashboard/';
			}else if(data['status'] == "M2"){
				alert("User name & Password Missmatch");
			}else{
				alert("Somthing Problem! Try Again");
			}
		});
	}
});

//Login form validation
function login_validation(){
	return $('#login_check').valid();
}

$("#login_check").validate({
	rules: {
		username:{
			required: true,
		},
		password:{
			required: true,
		},
	},
	//For custom messages
	messages: {
		username:{
			required:"Enter a user name",
		},
		password:{
			required:"Enter a user password",
		},
	},
	errorElement: 'div',
	errorPlacement: function(error, element) {
		var placement = $(element).data('error');
		if (placement) {
			$(placement).append(error);
		} else {
			error.insertAfter(element);
		}
	}
});