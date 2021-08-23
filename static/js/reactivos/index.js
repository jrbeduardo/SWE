function listaReactivos() {
	$.ajax({
			url: "/quizzes/busqueda/",
			type: "get",
			dataType: 'json',
			data: { busqueda : $('#id_text').val(), tema: $('#id_tema').val() },
			success: function(response){

				console.log(response);
				$('#id_quizzes').html('');

				if(response.length>0){
					$('#id_quizzes').prepend("<ul class='list-group list-group-flush'>");
					for (var i = 0; i < response.length; i++) {
						$('#id_quizzes').prepend(
							"<li class='list-group-item'><p><u>"
							+response[i].tema
							+"</u></p><strong>"
							+(response.length-i)+". "+response[i].pregunta
							+"</strong> <br> <em>R: "
							+response[i].respuesta
							+"</em><br><br><a href='/quizzes/editar_reactivo/"
							+response[i].id
							+"'><img src='https://img.icons8.com/pastel-glyph/36/000000/loop.png'/></a> <a href='/quizzes/eliminar_reactivo/"
							+ response[i].id
							+"'><img src='https://img.icons8.com/ios/36/000000/delete-forever--v2.png'/></a></li>"
						);
					}
					$('#id_quizzes').prepend("</ul>");
					$('#id_quizzes').prepend("<h3> Resultados: "+response.length+"</h3>");
				}else{
					$('#id_quizzes').html('<h3>No hay preguntas</h3>');
				}
			},
			error: function(error){
				console.log(error);
			}
		});
}

$( "#id_busqueda" ).on("submit",function(event) {
  event.preventDefault();
  listaReactivos();
});

/*
document.getElementById('id_text').addEventListener("input", function(event){
	event.preventDefault();
	listaReactivos();
});
*/