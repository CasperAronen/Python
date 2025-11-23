const maara = parseInt(prompt("Anna jasenien maara"))
let i = 0
const jasenet = [

]
const ol = document.getElementById("Jasen")

while(i < maara) {
    let JasenM = prompt("anna jasenen nimi")
    jasenet.push(JasenM)

    const li = document.createElement("li")
    li.textContent = JasenM
    ol.appendChild(li)
    i ++
}

let liArray = Array.from(ol.getElementsByTagName("li"));

liArray.sort((a, b) => a.textContent.localeCompare(b.textContent));

ol.innerHTML = "";

liArray.forEach(li => ol.appendChild(li));