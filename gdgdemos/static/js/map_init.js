var map;

$(document).ready(function(){	
	var mapOptions = {
		zoom: 14,
		center: new google.maps.LatLng(20.674346933909842,-103.38696956634521),
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
});