const result = document.getElementById("result");
const plus = document.getElementById("plus");
const minus = document.getElementById("minus");
let num = 0;
function increase() {
    num++;
    result.innerHTML = num;
}

function decrease() {
    num--;
    result.innerHTML = num;
}
plus.addEventListener("click", increase);
minus.addEventListener("click", decrease);