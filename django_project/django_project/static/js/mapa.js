// Crear un mapa
var myMap = L.map('map').setView([0, 0], 15); // Nivel de zoom moderado

// Agregar una capa de mapa (OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

// Agregar un marcador inicial en [0, 0]
var marker = L.marker([0, 0]).addTo(myMap);

// Función para obtener la ubicación del dispositivo móvil y actualizar el mapa
function updateLocation() {
    if ("geolocation" in navigator) {
        navigator.geolocation.watchPosition(function (position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            marker.setLatLng([latitude, longitude]);
            myMap.setView([latitude, longitude], myMap.getZoom());
        }, function(error) {
            alert("Error obteniendo la ubicación: " + error.message);
        });
    } else {
        alert("Geolocalización no está disponible en tu navegador.");
    }
}

// Llamar a la función para actualizar la ubicación al cargar la página
updateLocation();
