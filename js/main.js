$(document).ready(function() {
	$('#searchBox').keyup(function(event) {
		if (event.keyCode == 13) {
			window.location.href="/p/" + encodeURIComponent($('#searchBox').val());
		}
	});
});
