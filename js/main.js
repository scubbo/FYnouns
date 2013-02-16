$(document).ready(function() {
	console.log('hello there!');
	$('#go').click(function() {
		window.location.href="/p/" + encodeURIComponent($('#searchBox').val());
	});
});
