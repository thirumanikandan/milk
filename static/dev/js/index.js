$(document).ready(function () {
	product_list_get();
});

//server side api call to get product list
function product_list_get(){
	$.ajax({
		type  : 'GET',
		url   : '/product_details/',
		async : false,
		timeout : 10000,
		async:false,
	}).done( function(json_data) {
		var data = JSON.parse(json_data);
		if(data['status'] == "M1"){
			product_list(data['data'])
		}else{
			$('#product_list').html("<p>Data found in server...</p>");
		}
	});
} 

//product list form to index page
function product_list(data){
	productList = '';
	for(var i=0;i<data.length;i++){
		productList += '<div class="col-md-3">';
		productList += '<div class="cart-img-des"> <img class="el-hght" src="'+data[i].image_path+'">';
		productList += '<p>'+data[i].name+'</p> <a href="#" class="btn btn-info navbar-btn hvr-rectangle-out" onclick="product_order_modal_show('+data[i].id+',\''+data[i].name+'\',\''+data[i].image_path+'\',\''+data[i].price+'\')">Add to Cart</a> </div>';
		productList += '</div>';
	}
	$('#product_list').html(productList);
}

//product order show
function product_order_modal_show(pro_id,pro_name,img,price){
	$('#pro_order_quantity_id').val(0);
	$('#tot_order_product_price').html(0);
	$('#pro_order_modal_form')[0].reset();
	$('#order_product_price').html(price);
	$('#product_order_img').attr('src',img);
	$('#product_order_title').html(pro_name);
	$('#product_order_title').attr("class",pro_id)
	$('#product_order_modal').modal('show');
}

//product order quantity select
$('#pro_order_quantity_id').change(function() {
	var price = parseFloat(this.value) * parseFloat($('#order_product_price').text()) ;
	$('#tot_order_product_price').html(price);
});

//product1 check box status
$('#dontwant_status').change(function() {
    if(this.checked) {
    	$('.dontwant_status').show();  
    	$('.quantity_status').hide();  
    }
});
//product2 check box status
$('#quantity_status').change(function() {
    if(this.checked) {
    	$('.dontwant_status').hide();  
    	$('.quantity_status').show();
    }
});

//product order conform
function product_order_conform(){
	var login_user_id = $('.current_user').attr('id');
	var product_id = $('#product_order_title').attr('class');
	var from_date = $('#pro_from_date').val() != undefined ? $('#pro_from_date').val() : null;
	var to_date = $('#pro_to_date').val() != undefined ? $('#pro_to_date').val() : null ;
	var quantity = $('#pro_order_quantity_id option:selected').val();
	var pro_from_date = from_date.split('/')[2]+'-'+from_date.split('/')[0]+'-'+from_date.split('/')[1];
	var pro_to_date = to_date.split('/')[2]+'-'+to_date.split('/')[0]+'-'+to_date.split('/')[1];
	var area = 1
	var route = 1
	var company = 1
	var today = new Date();           
    var formattedtoday =  today.getFullYear() + '-'+ + (today.getMonth() + 1) +'-'+ today.getDate();
	var order_date = formattedtoday;
	var price = $('#tot_order_product_price').text();
	data = {'data':[
	                {
	                	'quantity':quantity,
	                	'order_date':order_date,
	                	'from_date':pro_from_date,
	                	'to_date':pro_to_date,
	                	'price':price,
	                	'product':product_id,
	                	'customer':login_user_id,
	                	'area':area,
	                	'route':route,
	                	'company':company,
	                }
	               ]}
	
	product_order(data)
}

//product order function here
function product_order(datas){
	console.log("===========================data------------------",data)
	$.ajax({
		type  : 'POST',
		url   : '/order_details/',
		data: JSON.stringify(datas),
		csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val(),
		async : false,
		timeout : 10000,
		async:false,
	}).done( function(json_data) {
		var data = JSON.parse(json_data);
		if(data['status'] == "M1"){
			$('#product_order_modal').modal('hide');
			alert("Your order is successfully added !!!")
		}else{
			$('#product_list').html("<p>Data found in server...</p>");
		}
	});
}

//dontwant order conform
function product_order_dontwant(){
	alert("---------Inprogress Mode---------")
}