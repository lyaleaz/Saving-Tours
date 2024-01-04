var date=new Date(new Date().getTime() + (3600 * 1000 *3));
c=0
function initMap() {
var deptime=document.querySelector('input[type="datetime-local"]').value;
console.log(date.toISOString().split('.')[0]);
document.querySelector('input[type="datetime-local"]').value=date.toISOString().split('.')[0];
  const directionsRenderer = new google.maps.DirectionsRenderer();
  const directionsService = new google.maps.DirectionsService();
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: { lat: 37.77, lng: -122.447 },
  });

  directionsRenderer.setMap(map);
  calculateAndDisplayRoute(directionsService, directionsRenderer);
}

function updatefunc(){
  var deptime=document.querySelector('input[type="datetime-local"]').value;
  date=new Date(deptime);
  date=date.setSeconds(0, 0)
  console.log(deptime)
  const directionsRenderer = new google.maps.DirectionsRenderer();
  const directionsService = new google.maps.DirectionsService();
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: { lat: 37.77, lng: -122.447 },
  });

  directionsRenderer.setMap(map);
  calculateAndDisplayRoute(directionsService, directionsRenderer);
}

function calculateAndDisplayRoute(directionsService, directionsRenderer) {
  origin=document.getElementById("frfr").value.toString();
  dest=document.getElementById("toto").value.toString();
  console.log(origin)
  console.log(dest)
  directionsService
    .route({
      origin:origin,
      destination:dest,
      travelMode:"TRANSIT",
      region:"israel",
      transitOptions:{departureTime:date},
    })
    .then((response) => {
      directionsRenderer.setDirections(response);
    })
    .catch((e) => window.alert("Directions request failed due to " + status));
}
function stcheck(val)
{
  kku=document.getElementById(val).textContent
  console.log(kku)
  if (c==-1)
  {
    var checkboxes = document.getElementsByName('sta');
    for (var checkbox of checkboxes) {
      checkbox.checked = false;
    c=0;
  }
  document.getElementById("fromst").value = '';
  document.getElementById("tost").value = '';

  return;
  }

  if (c==0){
    document.getElementById("fromst").value = kku;
    c=1;
    return;

  }
  if( c==1)
  {
  document.getElementById("tost").value = kku;
  c=-1;
  return;
  }

}
