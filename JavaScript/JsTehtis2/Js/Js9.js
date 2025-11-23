const lista = [
    2,3,7,5,4,8,12,43,5,68,100
]

function even(lista){
    let i = 0
    const tasaLista =[]
    while(i < lista.length){
        if (lista[i] % 2 === 0 ){
            tasaLista.push(lista[i])
        }
        i++
    }
    return tasaLista;
}
console.log(lista)
console.log(even(lista))