var map;
var Boston = {lat: 42.361145, lng: -71.057083}
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: Boston,
        zoom: 8
    });
}