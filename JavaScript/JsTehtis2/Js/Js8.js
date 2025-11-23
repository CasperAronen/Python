const lista = ["Juhani, Lebron, Gambling, horoskooppi"]

function concat(lista){
    let yhdistys = "";
    for (let i = lista.length - 1; i >= 0; i--){
    yhdistys += lista[i]
    if (i > 0) yhdistys += ", ";
}
    return yhdistys
}

console.log(concat(lista))

