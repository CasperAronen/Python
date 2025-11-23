
const ImgHover = document.getElementById("target");

ImgHover.addEventListener("mouseenter", () => {
    ImgHover.src = "img/picB.jpg"
})
ImgHover.addEventListener("mouseleave", () =>{
    ImgHover.src = "img/picA.jpg"
} )