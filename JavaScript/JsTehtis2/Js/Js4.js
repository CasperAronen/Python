let nolla = parseInt(prompt("Anna numero 0"))
const numerot = [

]
numerot.push(nolla)
while (nolla !== 0){
    nolla = parseInt(prompt("Anna numero 0")) || 0;
    numerot.push(nolla)
    console.log(nolla)
}
numerot.sort(function (a,b){
    return b-a
})

console.log( numerot.join(", "))