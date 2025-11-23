const vaaliJäbät =[
]
const maara = parseInt(prompt("anna ehdokkaiden määrä"))
let i = 0
while (maara > i){
    const nimi = prompt(`Anna ehdokkaan ${i+1} nimi`)
    vaaliJäbät.push({nimi: nimi, äänet: 0 });
    i ++
}
console.log(vaaliJäbät)

const ääniMaara = parseInt(prompt("Anna äänestäjien määrä"))
let it = 0

while(it<ääniMaara){
    let ääni = prompt("ketä haluat äänestää ")
    for (let a = 0; a < vaaliJäbät.length; a++) {
        if (ääni === vaaliJäbät[a].nimi) {
            vaaliJäbät[a].äänet +=1;
        }
    }
    it++;

}
vaaliJäbät.sort((a, b) => b.äänet - a.äänet);
const vin = vaaliJäbät[0]
console.log("Voittaja on,", vin.nimi, vin.äänet, "ääntä")
console.log("Tulokset")
for (let i = 0; i < vaaliJäbät.length; i++) {
    console.log("Nimi:" ,vaaliJäbät[i].nimi, "Äänet:", vaaliJäbät[i].äänet);
}