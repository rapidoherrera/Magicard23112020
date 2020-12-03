(function(){
	if (navigator.geolocation)
	{
		navigator.geolocation.getCurrentPosition(function(objPosition)
		{
			var lon = objPosition.coords.longitude;
			var lat = objPosition.coords.latitude;
            mapboxgl.accessToken = 'pk.eyJ1Ijoic2t1bGxmb3JjZTMiLCJhIjoiY2pvNzVlMnpkMGtqZjNwbWQ1b2ptcGkxcSJ9.CUYihkpbfsd8nTbDLN_FhA';
            var map = new mapboxgl.Map({
            container: 'map',
            style: 'mapbox://styles/mapbox/streets-v10',
            center: [lon, lat],
            zoom: 10,
            hash:true
            });
		}, function(objPositionError)
		{
			switch (objPositionError.code)
			{
				case objPositionError.PERMISSION_DENIED:
					content.innerHTML = "No se ha permitido el acceso a la posición del usuario.";
				break;
				case objPositionError.POSITION_UNAVAILABLE:
					content.innerHTML = "No se ha podido acceder a la información de su posición.";
				break;
				case objPositionError.TIMEOUT:
					content.innerHTML = "El servicio ha tardado demasiado tiempo en responder.";
				break;
				default:
					content.innerHTML = "Error desconocido.";
			}
		}, {
			maximumAge: 75000,
			timeout: 15000
		});
	}
	else
	{
		content.innerHTML = "Su navegador no soporta la API de geolocalización.";
	}
})();
