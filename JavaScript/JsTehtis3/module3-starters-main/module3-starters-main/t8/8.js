
const num1 = document.getElementById("num1")
const num2 = document.getElementById("num2")
const operationSelect = document.getElementById("operation")
const startButton = document.getElementById("start")
const pResult = document.getElementById("result")

startButton.addEventListener("click", () =>{
    const numero1 = parseInt(num1.value)
    const numero2 = parseInt(num2.value)
    const operation = operationSelect.value;
    let result;

    switch (operation) {
        case "add":
            result = numero1 + numero2;
            break;
        case "sub":
            result = numero1 - numero2;
            break
        case "multi":
            result = numero1 * numero2;
            break
        case "div":
            result = numero1 / numero2;
    }
    pResult.textContent = result
})