let sat = 0
const num = [

]
const ul = document.getElementById("nopan")
function noppa (){
    sat = Math.floor(Math.random() * 7)
    num.push(sat)
}
while(sat !== 6 ){
    noppa()
}

num.forEach((numero)=> {
    const li = document.createElement("li")
    li.textContent = numero
    ul.appendChild(li)
});