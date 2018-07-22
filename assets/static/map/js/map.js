const containerWidth = document.getElementById('containerMap').clientWidth;

document.getElementById("mapid").style["width"] = containerWidth + 'px';
document.getElementById("mapid").style["height"] = window.innerHeight + 'px';

const map = L.map('mapid', {
  minZoom: 6
}).setView([6.852374, -74.297333], 6);
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
  maxZoom: 18,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

const meetupsList = meetups();

let marker = ''
// Icons
const LeafIcon = L.Icon.extend({
  options: {
    iconSize: [30, 30]
  }
});

for (i in meetupsList) {
  let icon =
    marker = L.marker(meetupsList[i].coord, ).bindPopup(transformInfo(i, meetupsList[i].meetups)).addTo(map);
}