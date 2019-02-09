
const mapStyle = [
  {
    "featureType": "administrative",
    "elementType": "all",
    "stylers": [
      {
        "visibility": "on"
      },
      {
        "lightness": 33
      }
    ]
  },
  {
    "featureType": "landscape",
    "elementType": "all",
    "stylers": [
      {
        "color": "#f2e5d4"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#c5dac6"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "labels",
    "stylers": [
      {
        "visibility": "on"
      },
      {
        "lightness": 20
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "all",
    "stylers": [
      {
        "lightness": 20
      }
    ]
  },
  {
    "featureType": "road.highway",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#c5c6c6"
      }
    ]
  },
  {
    "featureType": "road.arterial",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#e4d7c6"
      }
    ]
  },
  {
    "featureType": "road.local",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#fbfaf7"
      }
    ]
  },
  {
    "featureType": "water",
    "elementType": "all",
    "stylers": [
      {
        "visibility": "on"
      },
      {
        "color": "#acbcc9"
      }
    ]
  }
];

// Escapes HTML characters in a template literal string, to prevent XSS.
// See https://www.owasp.org/index.php/XSS_%28Cross_Site_Scripting%29_Prevention_Cheat_Sheet#RULE_.231_-_HTML_Escape_Before_Inserting_Untrusted_Data_into_HTML_Element_Content
function sanitizeHTML(strings) {
  const entities = {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'};
  let result = strings[0];
  for (let i = 1; i < arguments.length; i++) {
    result += String(arguments[i]).replace(/[&<>'"]/g, (char) => {
      return entities[char];
    });
    result += strings[i];
  }
  return result;
}
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 15
  });
  // var infoWindow = new google.maps.InfoWindow();
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
              draggable:true,
              icon: `assets/img/GreenMarkerSeeThrough.png`,
              title:'Drag me!',
          });

infoWindow.setPosition(pos);
infoWindow.setContent('Location found.');
// infoWindow.open(map);
map.setCenter(pos);
}, function () {
    handleLocationError(true, infoWindow, map.getCenter());
});
} else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, map.getCenter());
}
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



  //Declaring apiKey constant for later use in program
  const apiKey = 'AIzaSyCGEIJiz7_1X6o4rve4r_mxxKefkkoOwYc';
  //Declares constant infowindow size for when user
  //clicks on GreenCircle
  const infoWindow = new google.maps.InfoWindow();
  infoWindow.setOptions({pixelOffset: new google.maps.Size(0, -30)});

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
