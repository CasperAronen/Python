let i = 0
const ul = document.getElementById("koirat")

while(i < 6) {
    let JasenM = prompt("anna koiran nimi")

    const li = document.createElement("li")
    li.textContent = JasenM
    ul.appendChild(li)
    i ++
}
let liArray = Array.from(ul.getElementsByTagName("li"));

liArray.sort((a, b) => a.textContent.localeCompare(b.textContent));

liArray.reverse()

ul.innerHTML = "";

liArray.forEach(li => ul.appendChild(li));