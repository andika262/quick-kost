//map
var map = L.map('map').setView([-6.12796, 106.1494842], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var homes
var url = '/homesapi/'

fetch(url)
    .then(response => response.json())
    .then(data => homes = data)
    .then(showhomes => showhome())
    .then(centerrhome => centerhome())

function showhome() {
    homes.forEach(home => {
        pop = L.popup({
            closeOnClick: true
        }).setContent(home.nama)

        coords = [home.coordX, home.coordY]

        marker = L.marker(coords).addTo(map).bindPopup(pop);

        tooltip = L.tooltip({
            permanent: true
        }).setContent('Rp.'+ home.harga)

        marker.bindTooltip(tooltip)
    });
}

hoes = document.querySelectorAll('.home')

function centerhome(){
    homes.forEach((home, index )=>{
        hoes[index].addEventListener("mouseover", (event) => {
            map.flyTo([home.coordX, home.coordY], 14)
        })
    })
}