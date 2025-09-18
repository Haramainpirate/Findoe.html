function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      document.getElementById('user-location').textContent =
        "Latitude: " + position.coords.latitude +
        ", Longitude: " + position.coords.longitude;
    }, function() {
      document.getElementById('user-location').textContent = "Unable to retrieve location.";
    });
  } else {
    document.getElementById('user-location').textContent = "Geolocation is not supported.";
  }
}
