var osmAttr = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
var cartoAttr = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>';
var topoAttr = 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)';

var translations = {
    ru: {
        title: "Бесполетные зоны Беларуси",
        layers: "Слои",
        zoomIn: "Увеличить масштаб",
        zoomOut: "Уменьшить масштаб",
        minimal: "Минимальная",
        natural: "Природная / Рельеф",
        border: "Приграничная территория",
        legacyLaw: "Запретные зоны из закона (2016)",
        legacyDanger: "Опасные зоны из кадастра (2016)",
        legacyForbidden: "Запретные зоны из кадастра (2016)",
        prohibited: "Запретные зоны (2020)",
        danger: "Опасные зоны (2020)",
        restricted: "Зоны ограничений (2020)",
        aerobatic: "Пилотажные зоны (2020)",
        takeoff_landing: "Зоны взлета и посадки (2020)",
        aerodrome_area: "Районы аэродромов (2020)",
        aerohub_area: "Районы аэроузлов (2020)",
        drone_prohibited: "Запретные зоны БЛА (2020)",
        amended_appendix_5_zone: "Измененная зона приложения 5 (2020)",
        minskAerohub: "Минский аэроузел",
        zone: "Зона",
        zoneNumber: "Номер зоны",
        source2020: "Источник: постановление 2020 г.",
        radius: "Радиус",
        kilometers: "км",
        airspaceExclusion: "Имеет исключение воздушного пространства",
        stateBorder: "Часть границы проходит по государственной границе",
        locationAccuracy: "Точность определения местоположения",
        meters: "м",
        dataMissing: "Не найдены данные для"
    },
    be: {
        title: "Беспалётныя зоны Беларусі",
        layers: "Слоі",
        zoomIn: "Павялічыць маштаб",
        zoomOut: "Паменшыць маштаб",
        minimal: "Мінімальная",
        natural: "Прыродная / Рэльеф",
        border: "Прыгранічная тэрыторыя",
        legacyLaw: "Забароненыя зоны паводле закона (2016)",
        legacyDanger: "Небяспечныя зоны з кадастру (2016)",
        legacyForbidden: "Забароненыя зоны з кадастру (2016)",
        prohibited: "Забароненыя зоны (2020)",
        danger: "Небяспечныя зоны (2020)",
        restricted: "Зоны абмежаванняў (2020)",
        aerobatic: "Пілатажныя зоны (2020)",
        takeoff_landing: "Зоны ўзлёту і пасадкі (2020)",
        aerodrome_area: "Раёны аэрадромаў (2020)",
        aerohub_area: "Раёны аэравузлоў (2020)",
        drone_prohibited: "Забароненыя зоны БПЛА (2020)",
        amended_appendix_5_zone: "Змененая зона дадатку 5 (2020)",
        minskAerohub: "Мінскі аэравузел",
        zone: "Зона",
        zoneNumber: "Нумар зоны",
        source2020: "Крыніца: пастанова 2020 г.",
        radius: "Радыус",
        kilometers: "км",
        airspaceExclusion: "Мае выключэнне паветранай прасторы",
        stateBorder: "Частка мяжы праходзіць па дзяржаўнай мяжы",
        locationAccuracy: "Дакладнасць вызначэння месцазнаходжання",
        meters: "м",
        dataMissing: "Не знойдзены даныя для"
    },
    en: {
        title: "Belarus No-Flight Zones",
        layers: "Layers",
        zoomIn: "Zoom in",
        zoomOut: "Zoom out",
        minimal: "Minimal",
        natural: "Natural / Topographic",
        border: "Border area",
        legacyLaw: "Prohibited zones from law (2016)",
        legacyDanger: "Danger zones from cadastre (2016)",
        legacyForbidden: "Prohibited zones from cadastre (2016)",
        prohibited: "Prohibited zones (2020)",
        danger: "Danger zones (2020)",
        restricted: "Restricted zones (2020)",
        aerobatic: "Aerobatic zones (2020)",
        takeoff_landing: "Takeoff and landing zones (2020)",
        aerodrome_area: "Aerodrome areas (2020)",
        aerohub_area: "Aerohub areas (2020)",
        drone_prohibited: "Drone prohibited zones (2020)",
        amended_appendix_5_zone: "Amended appendix 5 zone (2020)",
        minskAerohub: "Minsk aerohub",
        zone: "Zone",
        zoneNumber: "Zone number",
        source2020: "Source: 2020 regulation",
        radius: "Radius",
        kilometers: "km",
        airspaceExclusion: "Contains an airspace exclusion",
        stateBorder: "Part of the boundary follows the state border",
        locationAccuracy: "Location accuracy",
        meters: "m",
        dataMissing: "No data found for"
    }
};

function detectLanguage() {
    var browserLanguages = navigator.languages || [navigator.language || "en"];
    for (var index = 0; index < browserLanguages.length; ++index) {
        var language = browserLanguages[index].toLowerCase().split("-")[0];
        if (translations[language]) {
            return language;
        }
    }
    return "en";
}

var currentLanguage = detectLanguage();

function t(key) {
    return translations[currentLanguage][key] || translations.en[key] || key;
}

var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19, attribution: osmAttr });
var minimal = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', { maxZoom: 19, attribution: cartoAttr });
var natural = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', { maxZoom: 17, attribution: topoAttr });

var mymap = L.map('mapid', {
    center: [53.9035, 27.5410],
    zoom: 11,
    layers: [osm]
})
var pointsTextArea = document.getElementById('pointsTextArea');

// в запретную зону [1, 2, 3, 4, 5, 6, 7,118, 164]
// в опасную зоны 43, 41(оставить и в запретных для дрона), 49 [41,43, 49]

var zakon = L.layerGroup()
var kadasrDanger = L.layerGroup()
var kadasrForbidden = L.layerGroup()

var zones2020 = [
    {
        dataKey: "prohibited",
        color: "#d7191c",
        fillOpacity: 0.35
    },
    {
        dataKey: "danger",
        color: "#fdae61",
        fillOpacity: 0.3
    },
    {
        dataKey: "restricted",
        color: "#984ea3",
        fillOpacity: 0.3
    },
    {
        dataKey: "aerobatic",
        color: "#377eb8",
        fillOpacity: 0.15
    },
    {
        dataKey: "takeoff_landing",
        color: "#4daf4a",
        fillOpacity: 0.15
    },
    {
        dataKey: "aerodrome_area",
        color: "#00a6a6",
        fillOpacity: 0.1
    },
    {
        dataKey: "aerohub_area",
        color: "#006d77",
        fillOpacity: 0.08
    },
    {
        dataKey: "drone_prohibited",
        color: "#e41a1c",
        fillOpacity: 0.25
    },
    {
        dataKey: "amended_appendix_5_zone",
        color: "#ff00ff",
        fillOpacity: 0.3
    }
];

for (var zoneIndex = 0; zoneIndex < zones2020.length; ++zoneIndex) {
    zones2020[zoneIndex].layer = L.layerGroup();
}
var zones2020Bounds = L.latLngBounds();


borderItem = L.geoJSON(border, {
    color: 'red'
})

var borderLayer = L.layerGroup([borderItem])

function legacyPopup(zoneId) {
    return function() {
        return t("zoneNumber") + "=" + zoneId;
    };
}

for (var i = 0; i < circles.length; ++i )
{
    var circle = circles[i];    
    c = L.circle([circle.coordinates.lat, circle.coordinates.lng], 
        circle.radius*1000, {
            color: 'FUCHSIA',
            fillColor: '#FF00FF',
        fillOpacity: 0.5
        }).bindPopup(legacyPopup(circle.id));
        
    zakon.addLayer(c);
}
for (var i = 0; i < polys.length; ++i) {
    var poly = polys[i];
    p = L.polygon(poly.coordinates, {
        color: 'FUCHSIA',
        fillColor: '#FF00FF',
        fillOpacity: 0.5
    }).bindPopup(legacyPopup(poly.id));
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
        }).bindPopup(legacyPopup(circle.id));
    kadasrDanger.addLayer(c);
}
for (var i = 0; i < polysDanger.length; ++i) {
    var poly = polysDanger[i];
    p = L.polygon(poly.coordinates, {
        color: 'gold',
        fillColor: '#FFD700',
        fillOpacity: 0.5
    }).bindPopup(legacyPopup(poly.id));
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
        }).bindPopup(legacyPopup(circle.id));
    kadasrForbidden.addLayer(c);
}

for (var i = 0; i < polysForbidden.length; ++i) {
    var poly = polysForbidden[i];
    p = L.polygon(poly.coordinates, {
        color: '#cb1a00',
        fillColor: '#cb1a00',
        fillOpacity: 0.5
    }).bindPopup(legacyPopup(poly.id));
    kadasrForbidden.addLayer(p);
}





mymap.addLayer(borderLayer);

for (var zoneIndex = 0; zoneIndex < zones2020.length; ++zoneIndex) {
    var zone2020 = zones2020[zoneIndex];
    mymap.addLayer(zone2020.layer);
}

function escapeHtml(value) {
    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

function translatedGroupName(groupName) {
    if (currentLanguage === "ru") {
        return groupName;
    }

    var prefixes = {
        be: [
            ["Зона взлета и посадки посадочной площадки ", "Зона ўзлёту і пасадкі пасадачнай пляцоўкі "],
            ["Зона взлета и посадки аэродрома ", "Зона ўзлёту і пасадкі аэрадрома "],
            ["Пилотажные зоны аэродрома ", "Пілатажныя зоны аэрадрома "],
            ["Пилотажная зона аэродрома ", "Пілатажная зона аэрадрома "],
            ["Район аэродрома ", "Раён аэрадрома "]
        ],
        en: [
            ["Зона взлета и посадки посадочной площадки ", "Takeoff and landing zone of landing site "],
            ["Зона взлета и посадки аэродрома ", "Takeoff and landing zone of aerodrome "],
            ["Пилотажные зоны аэродрома ", "Aerobatic zones of aerodrome "],
            ["Пилотажная зона аэродрома ", "Aerobatic zone of aerodrome "],
            ["Район аэродрома ", "Aerodrome area: "]
        ]
    };

    var languagePrefixes = prefixes[currentLanguage] || [];
    for (var index = 0; index < languagePrefixes.length; ++index) {
        var source = languagePrefixes[index][0];
        if (groupName.indexOf(source) === 0) {
            return languagePrefixes[index][1] + groupName.slice(source.length);
        }
    }
    return groupName;
}

function zonePopup(feature) {
    var properties = feature.properties || {};
    var designation = properties.category === "aerohub_area"
        ? t("minskAerohub")
        : properties.designation || t("zone");
    var lines = [
        "<strong>" + escapeHtml(designation) + "</strong>",
        escapeHtml(t(properties.category)),
        t("source2020")
    ];

    if (properties.group_name) {
        lines.push(escapeHtml(translatedGroupName(properties.group_name)));
    }
    if (properties.radius_km) {
        lines.push(t("radius") + ": " + escapeHtml(properties.radius_km) + " " + t("kilometers"));
    }
    if (properties.has_airspace_exclusion) {
        lines.push(t("airspaceExclusion"));
    }
    if (properties.follows_state_border) {
        lines.push(t("stateBorder"));
    }

    return lines.join("<br>");
}

function loadZone2020(zone) {
    var data = zones2020Data[zone.dataKey];
    if (!data) {
        console.error(t("dataMissing") + " " + t(zone.dataKey));
        return;
    }

    var geoJsonLayer = L.geoJSON(data, {
        style: {
            color: zone.color,
            fillColor: zone.color,
            fillOpacity: zone.fillOpacity,
            weight: 1.5
        },
        onEachFeature: function(feature, layer) {
            layer.bindPopup(function() {
                return zonePopup(feature);
            });
        }
    });
    geoJsonLayer.addTo(zone.layer);
    zones2020Bounds.extend(geoJsonLayer.getBounds());
}

for (var zoneIndex = 0; zoneIndex < zones2020.length; ++zoneIndex) {
    loadZone2020(zones2020[zoneIndex]);
}

function getBaseMaps() {
    var maps = {
        "OpenStreetMap": osm
    };
    maps[t("minimal")] = minimal;
    maps[t("natural")] = natural;
    return maps;
}

function getOverlayMaps() {
    var overlays = {};
    overlays[t("border")] = borderLayer;
    overlays[t("legacyLaw")] = zakon;
    overlays[t("legacyDanger")] = kadasrDanger;
    overlays[t("legacyForbidden")] = kadasrForbidden;

    for (var zoneIndex = 0; zoneIndex < zones2020.length; ++zoneIndex) {
        var zone = zones2020[zoneIndex];
        overlays[t(zone.dataKey)] = zone.layer;
    }
    return overlays;
}

var layerControl;
var languageButtons = {};

function rebuildLayerControl() {
    if (layerControl) {
        mymap.removeControl(layerControl);
    }
    layerControl = L.control.layers(getBaseMaps(), getOverlayMaps()).addTo(mymap);
    if (layerControl._layersLink) {
        layerControl._layersLink.title = t("layers");
        layerControl._layersLink.setAttribute("aria-label", t("layers"));
    }
}

function setLanguage(language) {
    if (!translations[language]) {
        language = "en";
    }
    currentLanguage = language;
    document.documentElement.lang = language;
    document.title = t("title");
    if (mymap.zoomControl) {
        mymap.zoomControl._zoomInButton.title = t("zoomIn");
        mymap.zoomControl._zoomOutButton.title = t("zoomOut");
    }

    Object.keys(languageButtons).forEach(function(buttonLanguage) {
        var isActive = buttonLanguage === language;
        languageButtons[buttonLanguage].classList.toggle("active", isActive);
        languageButtons[buttonLanguage].setAttribute("aria-pressed", isActive);
    });

    rebuildLayerControl();
}

var LanguageControl = L.Control.extend({
    options: {
        position: "topright"
    },

    onAdd: function() {
        var container = L.DomUtil.create("div", "language-control");
        var labels = {
            ru: "RU",
            be: "BE",
            en: "EN"
        };
        var languageNames = {
            ru: "Русский",
            be: "Беларуская",
            en: "English"
        };

        L.DomEvent.disableClickPropagation(container);
        L.DomEvent.disableScrollPropagation(container);

        Object.keys(labels).forEach(function(language) {
            var button = L.DomUtil.create("button", "", container);
            button.type = "button";
            button.textContent = labels[language];
            button.title = languageNames[language];
            button.setAttribute("aria-label", languageNames[language]);
            L.DomEvent.on(button, "click", function() {
                setLanguage(language);
            });
            languageButtons[language] = button;
        });

        return container;
    }
});

new LanguageControl().addTo(mymap);
setLanguage(currentLanguage);

if (zones2020Bounds.isValid()) {
    mymap.fitBounds(zones2020Bounds, {padding: [20, 20]});
}

mymap.locate({setView: false, maxZoom: 16});
function onLocationFound(e) {
    var radius = e.accuracy;

    L.marker(e.latlng).addTo(mymap)
        .bindPopup(t("locationAccuracy") + ": " + Math.round(radius) + " " + t("meters"))
        .openPopup();

    L.circle(e.latlng, radius).addTo(mymap);
}

mymap.on('locationfound', onLocationFound);

function onLocationError(e) {
    alert(e.message);
}

mymap.on('locationerror', onLocationError);
