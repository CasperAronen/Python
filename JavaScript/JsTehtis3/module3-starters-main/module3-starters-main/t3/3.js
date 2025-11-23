'use strict';
const names = ['John', 'Paul', 'Jones'];
const lista = document.getElementById("target");

names.forEach(name => {
    lista.innerHTML += `<li>${name}</li>`
})

