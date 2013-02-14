console.log('hello there!');
$('#go').click(function() {
	console.log('clicked');
	$.ajax('/scr/FYnouns.py', function(data) {console.log(data)});
});
