var mymap = L.map('mapid').setView([53.9035, 27.5410], 11);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox.streets'
}).addTo(mymap);

var pointsTextArea = document.getElementById('pointsTextArea');

for (var i = 0; i < zones.length; ++i )
{
    var zone = zones[i];
    // console.log(zone.name);

    // console.log(zone.coordinates[0][0]);

    if (zone.type == 'circle'  )
    {
        L.circle([zone.coordinates[0][0], zone.coordinates[0][1]], zone.radius*1000, {
            color: 'red',
            fillColor: '#f03',
            fillOpacity: 0.5
        }).addTo(mymap).bindPopup(zone.name);
        continue;
    }
    else if (zone.type == 'polygon' )
    {
        // console.log('polygon '+ i);
        // console.log(zone.coordinates )

        L.polygon(zone.coordinates, {
            color: 'red',
            fillColor: '#f03',
            fillOpacity: 0.5
        }).addTo(mymap).bindPopup(zone.name);
    }
}

L.geoJSON(border, {
    color: 'red'
}).addTo(mymap);


