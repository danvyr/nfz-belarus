var mymap = L.map('mapid').setView([53.9035, 27.5410], 11);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);

var pointsTextArea = document.getElementById('pointsTextArea');

for (var i = 0; i < circles.length; ++i )
{
    var circle = circles[i];
    // console.log(zone.name);

    // console.log(zone.coordinates[0][0]);
    L.circle([circle.coordinates.lat, circle.coordinates.lng], 
        circle.radius*1000, {
            color: 'FUCHSIA',
            fillColor: '#FF00FF',
        fillOpacity: 0.5
        }).bindPopup('Номер зоны=' + circle.id).addTo(mymap);
    // L.marker([circle.coordinates.lat, circle.coordinates.lng])
    // .addTo(mymap)
    // .bindPopup(circle.id);
}


for (var i = 0; i < polys.length; ++i )
{   
    var poly = polys[i];

    L.polygon(poly.coordinates, {
        color: 'FUCHSIA',
        fillColor: '#FF00FF',
        fillOpacity: 0.5
    }).bindPopup('Номер зоны=' + poly.id).addTo(mymap);

}

L.geoJSON(border, {
    color: 'red'
}).addTo(mymap);


// navigator.geolocation.getCurrentPosition(function(location) {
//     var latlng = new L.LatLng(location.coords.latitude, location.coords.longitude);
  
//     var mymap = L.map('mapid').setView(latlng, 13)
//     L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
//       attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://mapbox.com">Mapbox</a>',
//       maxZoom: 18,
//       id: 'mapbox.streets',
//       accessToken: 'pk.eyJ1IjoiYmJyb29rMTU0IiwiYSI6ImNpcXN3dnJrdDAwMGNmd250bjhvZXpnbWsifQ.Nf9Zkfchos577IanoKMoYQ'
//     }).addTo(mymap);
  
//     var marker = L.marker(latlng).addTo(mymap);
//   });

//   L.easyButton('<i class="material-icons" style="font-size:18px;">gps_fixed</i>', function(){
//     locateMe();
// }, {position: 'bottomright'}).addTo(mymap);

mymap.locate({setView: true, maxZoom: 16});
function onLocationFound(e) {
    var radius = e.accuracy;

    L.marker(e.latlng).addTo(mymap)
        .bindPopup("You are within " + radius + " meters from this point").openPopup();

    L.circle(e.latlng, radius).addTo(mymap);
}

mymap.on('locationfound', onLocationFound);

function onLocationError(e) {
    alert(e.message);
}

mymap.on('locationerror', onLocationError);

