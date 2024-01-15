$('DIV#add_item').on('click', function(){
	var new_list = "<li>Item</li>";
	
	$('UL.my_list').append(new_list);

});
