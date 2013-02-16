$(document).ready(function() {
	var theQuery = window.location.pathname.match(/\/p\/([^\/]*?)($|\/)/);
	loadImage(theQuery[1]);
	$('#searchBox').keyup(function(event) {
		if (event.keyCode == 13) {
			query = $('#searchBox').val();
			loadImage(query);
		}
	});
});


function loadImage(query) {
	$('#theImageWrapper').css('background-image', 'url(/css/ajaxload.gif)');
	window.history.pushState('', 'FUCK YEAH ' + query.toUpperCase(), '/p/' + encodeURIComponent(query));
	$('#searchBox').val('');
	$.ajax({
		url:'/scr/FYnouns.py?query=' + encodeURIComponent(query),
		type:'post',
		datatype:'text',
		success:function(data, textStatus, jqXHR) {
			//$('#theImageWrapper').css('background-image', 'url(' + data + ')');
		}
	});
}
