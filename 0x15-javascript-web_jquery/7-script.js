$(function(){
	$.ajax({
		type:'GET',
		url:'https://swapi-api.alx-tools.com/api/people/5/?format=json',
		success:function(data){
			var characterName = data.name;
			
			$('DIV#character').text(characterName);
		},
		error: function(error) {
       			 console.error('Error fetching character data:', error);
      		}
		
		
	});

});
