const num = [
]

while (true){
    let lisa = parseInt(prompt("Anna numero"))

    if (num.includes(lisa)){
        alert("Numero on jo annettu")
        break;
    }
    num.push(lisa)
}

num.sort((a,b) => a-b);

console.log(num)