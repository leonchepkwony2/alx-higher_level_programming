$(function(){
	$.ajax({
		type:'GET',
		url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
		success: function(data){
			var helloTranslation = data.hello;
			$('DIV#hello').text(helloTranslation);
		},
		error: function(error) {
       		console.error('Error fetching  data:', error);
      	}
		
	});
});
