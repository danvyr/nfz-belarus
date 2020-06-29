

// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     maxZoom: 18,
//     attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
// }).addTo(mymap);


var mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
    '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
    'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    mbUrl = 'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw';

var osmAttr = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';

var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { tileSize: 512, zoomOffset: -1, attribution: osmAttr }),
    grayscale = L.tileLayer(mbUrl, { id: 'mapbox/light-v9', tileSize: 512, zoomOffset: -1, attribution: mbAttr }),
    streets = L.tileLayer(mbUrl, { id: 'mapbox/streets-v11', tileSize: 512, zoomOffset: -1, attribution: mbAttr });

var baseMaps = {   
    "Grayscale": grayscale,
    "Streets": streets,
    "OpenStreetMAp": osm,
};

var mymap = L.map('mapid', {
    center: [53.9035, 27.5410],
    zoom: 11,
    layers: [ grayscale, streets, osm]
})
var pointsTextArea = document.getElementById('pointsTextArea');

// в запретную зону [1, 2, 3, 4, 5, 6, 7,118, 164]
// в опасную зоны 43, 41(оставить и в запретных для дрона), 49 [41,43, 49]

var zakon = L.layerGroup()
var kadasrDanger = L.layerGroup()
var kadasrForbidden = L.layerGroup()
var kadasrForbiddenAero = L.layerGroup()


borderItem = L.geoJSON(border, {
    color: 'red'
})

var borderLayer = L.layerGroup([borderItem])


for (var i = 0; i < circles.length; ++i )
{
    var circle = circles[i];    
    c = L.circle([circle.coordinates.lat, circle.coordinates.lng], 
        circle.radius*1000, {
            color: 'FUCHSIA',
            fillColor: '#FF00FF',
        fillOpacity: 0.5
        }).bindPopup('Номер зоны=' + circle.id);
        
    zakon.addLayer(c);
}
for (var i = 0; i < polys.length; ++i) {
    var poly = polys[i];
    p = L.polygon(poly.coordinates, {
        color: 'FUCHSIA',
        fillColor: '#FF00FF',
        fillOpacity: 0.5
    }).bindPopup('Номер зоны=' + poly.id);
    zakon.addLayer(p);
}


for (var i = 0; i < circlesDanger.length; ++i )
{
    var circle = circlesDanger[i];
    c = L.circle([circle.coordinates.lat, circle.coordinates.lng], 
        circle.radius*1000, {
            color: 'gold',
            fillColor: '#FFD700',
        fillOpacity: 0.5
        }).bindPopup('Номер зоны=' + circle.id);
    kadasrDanger.addLayer(c);
}
for (var i = 0; i < polysDanger.length; ++i) {
    var poly = polysDanger[i];
    p = L.polygon(poly.coordinates, {
        color: 'gold',
        fillColor: '#FFD700',
        fillOpacity: 0.5
    }).bindPopup('Номер зоны=' + poly.id);
    kadasrDanger.addLayer(p);
}

for (var i = 0; i < circlesForbidden.length; ++i )
{
    var circle = circlesForbidden[i];
    c = L.circle([circle.coordinates.lat, circle.coordinates.lng], 
        circle.radius*1000, {
            color: '#cb1a00',
            fillColor: '#cb1a00',
        fillOpacity: 0.5
        }).bindPopup('Номер зоны=' + circle.id);
    kadasrForbidden.addLayer(c);
}

for (var i = 0; i < polysForbidden.length; ++i) {
    var poly = polysForbidden[i];
    p = L.polygon(poly.coordinates, {
        color: '#cb1a00',
        fillColor: '#cb1a00',
        fillOpacity: 0.5
    }).bindPopup('Номер зоны=' + poly.id);
    kadasrForbidden.addLayer(p);
}



for (var i = 0; i < polysForbiddenAero.length; ++i) {
    var poly = polysForbiddenAero[i];
    p = L.polygon(poly.coordinates, {
        color: '#0000FF',
        fillColor: '#0000FF',
        fillOpacity: 0.5
    }).bindPopup('Номер зоны=' + poly.id);
    kadasrForbiddenAero.addLayer(p);
}





mymap.addLayer(zakon);
mymap.addLayer(kadasrDanger);
mymap.addLayer(kadasrForbidden);
mymap.addLayer(borderLayer);
mymap.addLayer(kadasrForbiddenAero);

var overlayMaps = {
    "Запретные зоны из закона": zakon,
    "Приграничная территория": borderLayer,
    "Опасные зоны из кадастра ": kadasrDanger,
    "Запретные зоны из кадастра": kadasrForbidden,
    "Запретные зоны для полёта из кадастра": kadasrForbiddenAero,
};



L.control.layers(baseMaps,overlayMaps).addTo(mymap);



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

