const mapStyle = [
  {
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#f5f5f5"
      }
    ]
  },
  {
    "elementType": "labels.icon",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#616161"
      }
    ]
  },
  {
    "elementType": "labels.text.stroke",
    "stylers": [
      {
        "color": "#f5f5f5"
      }
    ]
  },
  {
    "featureType": "administrative.land_parcel",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#bdbdbd"
      }
    ]
  },
  {
    "featureType": "poi",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#eeeeee"
      }
    ]
  },
  {
    "featureType": "poi",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#757575"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#e5e5e5"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#9e9e9e"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#ffffff"
      }
    ]
  },
  {
    "featureType": "road.arterial",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#757575"
      }
    ]
  },
  {
    "featureType": "road.highway",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#dadada"
      }
    ]
  },
  {
    "featureType": "road.highway",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#616161"
      }
    ]
  },
  {
    "featureType": "road.local",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#9e9e9e"
      }
    ]
  },
  {
    "featureType": "transit.line",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#e5e5e5"
      }
    ]
  },
  {
    "featureType": "transit.station",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#eeeeee"
      }
    ]
  },
  {
    "featureType": "water",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#c9c9c9"
      }
    ]
  },
  {
    "featureType": "water",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#9e9e9e"
      }
    ]
  }
];

var getStarted = document.getElementById("getStarted");
getStarted.addEventListener("click", function () {
  console.log("clicked");
  var canvas = document.getElementsByClassName("canvas");
  canvas[0].remove();
  placeBlueMarkers();

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      // Creates a draggable marker at the center of the map,
      // centered on the user's location initially.
      var marker = new google.maps.Marker({
        position: pos,
        map: map,
        animation: google.maps.Animation.DROP,
        draggable: true,
        icon: `assets/img/GreenMarkerSeeThrough.png`,
        title: 'Drag me!',
      });

      map.setCenter(pos);
    }, function () {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }
})

// Escapes HTML characters in a template literal string, to prevent XSS.
// See https://www.owasp.org/index.php/XSS_%28Cross_Site_Scripting%29_Prevention_Cheat_Sheet#RULE_.231_-_HTML_Escape_Before_Inserting_Untrusted_Data_into_HTML_Element_Content
function sanitizeHTML(strings) {
  const entities = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };
  let result = strings[0];
  for (let i = 1; i < arguments.length; i++) {
    result += String(arguments[i]).replace(/[&<>'"]/g, (char) => {
      return entities[char];
    });
    result += strings[i];
  }
  return result;
}

function placeBlueMarkers() {
  // Adds the json data file onto the maps
  // Json must be in 'geoJson' format
  map.data.addGeoJson(manualData);
  // Specifies and defines the custom marker images
  // using properties of the
  map.data.setStyle(feature => {
    return {
      icon: {
        url: `assets/img/BlueMarker.png`,
        scaledSize: new google.maps.Size(64, 64)
      }
    };
  });
}

function initMap() {
  var Boston = {lat: 42.361145, lng: -71.057083};

  map = new google.maps.Map(document.getElementById('map'), {
    center: Boston,
    zoom: 15
  });
  // var infoWindow = new google.maps.InfoWindow();
  
  



  //Declaring apiKey constant for later use in program
  const apiKey = 'AIzaSyCGEIJiz7_1X6o4rve4r_mxxKefkkoOwYc';
  //Declares constant infowindow size for when user
  //clicks on GreenCircle
  const infoWindow = new google.maps.InfoWindow();
  infoWindow.setOptions({ pixelOffset: new google.maps.Size(0, -30) });

  // This block of code adds a click event
  // to each icon on the map, which
  // when clicked, displays more information
  // about the crime.
  map.data.addListener('click', event => {

    const category = event.feature.getProperty('category');
    const time = event.feature.getProperty('time');
    const day = event.feature.getProperty('day');
    const street = event.feature.getProperty('street');

    const position = event.feature.getGeometry().get();
    const content = sanitizeHTML`
    <img style="float:left; width:200px; margin-top:30px" src="assets/img/BlueMarker.png">
    <div style="margin-left:220px; margin-bottom:20px;">
      <h2>${category}</h2>
      <p><b>Date and Time of Crime:</b> ${day} ${time}<br/><b></b> ${street}
      <p><img src="https://maps.googleapis.com/maps/api/streetview?size=350x120&location=${position.lat()},${position.lng()}&key=${apiKey}"></p>
    </div>
  `;
    map.data.addListener('click', event)

    infoWindow.setContent(content);
    infoWindow.setPosition(position);
    infoWindow.open(map);
  });
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
    'Error: The Geolocation service failed.' :
    'Error: Your browser doesn\'t support geolocation.');
  infoWindow.open(map);
}

var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value;
}