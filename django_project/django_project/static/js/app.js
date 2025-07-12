var marker;

function initMap() {
    // Inicializar el mapa
    var map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 0, lng: 0 },
        zoom: 7
    });

    // Inicializar la base de datos de Firebase
    var database = firebase.database();

    // Referencia a la ubicación en la base de datos
    var locationRef = database.ref('ubicacion');

    // Escuchar cambios en los datos de ubicación
    locationRef.on('value', function (snapshot) {
        // Limpiar el marcador existente en el mapa
        clearMarker();

        // Obtener datos de ubicación desde Firebase
        var locations = snapshot.val();

        // Obtener la última ubicación
        var keys = Object.keys(locations);
        var lastKey = keys[keys.length - 1];
        var lastLocation = locations[lastKey];

        // Mostrar marcador en el mapa para la última ubicación
        if (lastLocation) {
            addMarker(map, lastLocation.latitude, lastLocation.longitude, 'Última ubicación: ' + lastLocation.timestamp, 'Usuario prueba');
        }
    });
}

function addMarker(map, lat, lng, title, label) {
    // Verificar si lat y lng son números
    if (!isNaN(lat) && !isNaN(lng)) {
        marker = new google.maps.Marker({
            position: { lat: parseFloat(lat), lng: parseFloat(lng) },
            map: map,
            title: title,
            label: label // Agregar el nombre al marcador
        });
    } else {
        console.error('Coordenadas no válidas:', lat, lng);
    }
}

function clearMarker() {
    // Limpiar el marcador existente
    if (marker) {
        marker.setMap(null);
    }
}
