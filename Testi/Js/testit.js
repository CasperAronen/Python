const nuolet = ["←", "↑", "↓", "→"]
const nuoliKuvat = {
    "←": "./kuvat/vasen.jpg",
    "↑": "./kuvat/ylos.png",
    "↓": "./kuvat/alas.jpg",
    "→": "./kuvat/oikea.jpg"
}
const app = document.getElementById("app");

app.innerHTML = `
<button id="start">Aloita peli</button>
    <div class="testi">
        <div id="tulos">Pisteet: 0</div>
        <div id="aika">Aika: 30</div>

        <div id="kuvat">
            <img id="nuoliKuvat" src="./kuvat/alku.jpg" alt="alkukuva">
        </div>

        <div id="napit"></div>
    </div>
    <div id="loppu" style="display:none;">Nyt loppu lmao</div>
    
<button id="start2">Aloita peli 2 (W)</button>

    <div id="game2" class="testi">
        <div id="piste2">Pisteet: 0</div>
        <div id="aika2">Aika: 30</div>
        <img id="kuva2" src="./kuvat/ylos.png">
    </div>
`;

let nuoli = []
let pisteet = 0
let aika = 30
let active = false
const voitto = 30


const nuoliDiv = document.getElementById("napit")
const pisteDiv = document.getElementById("tulos")
const aikaDiv = document.getElementById("aika")
const loppuDiv = document.getElementById("loppu")
const nuoliKuva = document.getElementById("nuoliKuvat")
document.getElementById("start").addEventListener("click", startGame);

function startGame(){
    pisteet = 0
    aika = 30
    active = true

    luoNuoli()
    taulu()
    nuoliKuva.src = "./kuvat/alku.jpg"

    if(timer) clearInterval(timer)

    timer = setInterval(ajastin, 1000)
}
function luoNuoli() {
    nuoli = []
    for (let i = 0; i < 5; i++){
        nuoli.push(randNuoli());
    }
    taulu()
}
function luoNuoliKuva(nappi){
    nuoliKuva.src = nuoliKuvat[nappi];
}

function randNuoli() {
    return nuolet[Math.floor(Math.random() * nuolet.length )]
}

function taulu() {
    nuoliDiv.textContent = nuoli.join(" ")
    pisteDiv.textContent = "Pisteet: " + pisteet;
    aikaDiv.textContent = "aika: "+aika
}

document.addEventListener("keydown", (e) => {
    if (!active) return;
    const eka = nuoli[0];

    let näppäin = "";
    if(e.key === "ArrowLeft") näppäin = "←"
    if(e.key === "ArrowUp") näppäin = "↑"
    if(e.key === "ArrowDown") näppäin = "↓"
    if(e.key === "ArrowRight") näppäin = "→"

    if(!näppäin) return;

    if (näppäin === eka){
        nuoli.shift()
        pisteet++;
        nuoli.push(randNuoli())
        taulu()
        luoNuoliKuva(näppäin)
        voittoTarkistus()
    }else {
        lopeta()
    }
})
function voittoTarkistus(){
    if(pisteet >= voitto) {
        active = false;
        const testiDiv = document.querySelector(".testi");
        testiDiv.innerHTML = "<div id='voitto'>Voitit</div>";
    }
}
function lopeta(){
    active = false;
    const testiDiv = document.querySelector(".testi");
    testiDiv.innerHTML = "<div id='loppu'>Nyt loppu lmao</div>";
}

function ajastin(){
    if (!active) return;
    aika--;
    taulu()
    if (aika <= 0) {
        lopeta()
    }
}

//MINIPELI2
let piste2 = 0;
let aika2 = 30;
let active2 = false;
let timer2 = null;
let drop = null;

const piste2Div = document.getElementById("piste2");
const aika2Div = document.getElementById("aika2");
const kuva2 = document.getElementById("kuva2");

const kuvatTasot = [
    "./kuvat/alas.jpg",
    "./kuvat/oikea.jpg",
    "./kuvat/vasen.jpg",
    "./kuvat/alas.jpg",
];

document.getElementById("start2").addEventListener("click", startGame2);

function startGame2(){
    piste2 = 0;
    aika2 = 30;
    active2 = true;


    updateGame2()

    if(timer2) clearInterval(timer2)
    if(drop) clearInterval(drop)

    timer2 = setInterval(aikaTick2,1000)
    drop = setInterval(pisteReduce,200)
}

function updateGame2(){
    piste2Div.textContent = "Pisteet: " + piste2
    aika2Div.textContent = "Aika: " + aika2

    if(piste2 < 5) kuva2.src = kuvatTasot[0]
    else if(piste2 < 10) kuva2.src = kuvatTasot[1]
    else if(piste2 < 20) kuva2.src = kuvatTasot[2]
    else kuva2.src = kuvatTasot[3]
}

document.addEventListener("keydown", (e)=>{
    if(!active2) return;
    if(e.key === "w" || e.key === "W"){
        piste2++
        updateGame2()
        if(piste2 >= 30) win2();
    }
})

function pisteReduce(){
    if(!active2) return;
    if(piste2 > 0){
        piste2--
        updateGame2()
    }
}

function aikaTick2(){
    if(!active2) return;
    aika2--
    updateGame2()
    if(aika2 <= 0){
        end2();
    }
}

function win2(){
    active2 = false;
    alert("Voitit pelin 2!");
}

function end2(){
    active2 = false;
    alert("Loppu!");
}


luoNuoli()
taulu()

nuoliKuva.src = "./kuvat/alku.jpg";
setInterval(ajastin, 1000)