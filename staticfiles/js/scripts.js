/*!
* Start Bootstrap - Clean Blog v6.0.8 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function () {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if (currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})

var alamat = document.querySelector("#address")
var addresses = document.querySelector("#addresses")
var address = document.querySelector("#id_alamat")
var coordX = document.querySelector("#id_coordX")
var coordY = document.querySelector("#id_coordY")
var results = document.querySelector("#results")

function showAddresses() {
    addresses.innerHTML = ''
    if (addressData.length > 0) {
        addressData.forEach(address => {
            addressName = address.display_name.replace("'", " ")
            addresses.innerHTML += "<div class='results' onclick='selectAddress("
                + address.lat + "," + address.lon + "," + '"' + addressName + '"' + ")'>"
                + address.display_name + "</div>"
        });
    }
}

function selectAddress(x, y, adr) {
    address.value = adr
    coordX.value = x
    coordY.value = y
    map.flyTo([x,y],16)
    marker.closePopup()
    marker.closePopup()
    marker.setLatLng([x,y])
}

function findAddresses() {
    var url = "https://nominatim.openstreetmap.org/search?format=json&limit=3&q=" + alamat.value
    fetch(url)
        .then(response => response.json())
        .then(data => addressData = data)
        .then(showAddress => showAddresses())
        .catch(err => console.log(err))
}

