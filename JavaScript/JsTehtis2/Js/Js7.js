let sat = 0
const num = [

]
const sivut = parseInt(prompt("Anna nopan sivujen määrä"))
const ul = document.getElementById("sivut")

function noppa (sivut){
    sat = Math.floor(Math.random() * sivut) + 1;
    num.push(sat)
}
while(sat !== sivut ){
    noppa(sivut)
}

num.forEach((numero)=> {
    const li = document.createElement("li")
    li.textContent = numero
    ul.appendChild(li)
});