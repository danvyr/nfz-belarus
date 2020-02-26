var mymap = L.map('mapid').setView([53.9035, 27.5410], 11);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);

var pointsTextArea = document.getElementById('pointsTextArea');
// в запретную зону [1, 2, 3, 4, 5, 6, 7,118, 164]
// в опасную зоны 43, 41(оставить и в запретных для дрона), 49 [41,43, 49]

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
}
for (var i = 0; i < circlesDanger.length; ++i )
{
    var circle = circlesDanger[i];
    L.circle([circle.coordinates.lat, circle.coordinates.lng], 
        circle.radius*1000, {
            color: 'gold',
            fillColor: '#FFD700',
        fillOpacity: 0.5
        }).bindPopup('Номер зоны=' + circle.id).addTo(mymap);
}
for (var i = 0; i < circlesForbidden.length; ++i )
{
    var circle = circlesForbidden[i];
    L.circle([circle.coordinates.lat, circle.coordinates.lng], 
        circle.radius*1000, {
            color: 'red',
            fillColor: '#FF0000',
        fillOpacity: 0.5
        }).bindPopup('Номер зоны=' + circle.id).addTo(mymap);
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
for (var i = 0; i < polysDanger.length; ++i )
{   
    var poly = polysDanger[i];
    L.polygon(poly.coordinates, {
        color: 'gold',
        fillColor: '#FFD700',
        fillOpacity: 0.5
    }).bindPopup('Номер зоны=' + poly.id).addTo(mymap);
}
for (var i = 0; i < polysForbidden.length; ++i )
{   
    var poly = polysForbidden[i];
    L.polygon(poly.coordinates, {
        color: 'red',
        fillColor: '#FF0000',
        fillOpacity: 0.5
    }).bindPopup('Номер зоны=' + poly.id).addTo(mymap);
}

L.geoJSON(border, {
    color: 'red'
}).addTo(mymap);





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

