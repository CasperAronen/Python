const eka = prompt("anna ensimmäinen numero")
const toka = prompt("anna toinen numero")
const kolmas = prompt("anna kolmas numero")
const neljas = prompt("anna neljäs numero")
const viides = prompt("anna viides numero")

const num = [
    ]
let kaanteis = ""
num.push(eka, toka, kolmas, neljas, viides)
for (let i = num.length - 1; i >= 0; i--){
    kaanteis += num[i]
    if (i > 0) kaanteis += ", ";
}

document.getElementById("numerot").innerHTML = kaanteis