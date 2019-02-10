var request = new XMLHttpRequest();
var crimes;

request.open('GET', 'http://localhost:5000/crime_map?lat=42.3506&long=-71.04723&radius=10&days=100', true);
request.onload = function () {

  // Begin accessing JSON data here
  crimes = JSON.parse(this.response);
  console.log(crimes);

  // if (request.status >= 200 && request.status < 400) {
  //   data.forEach(movie => {
  //     console.log(movie.title);
  //   });
  // } else {
  //   console.log('error');
  // }
}

request.send();
