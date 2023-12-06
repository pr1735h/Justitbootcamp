document.body.style.backgroundColor = "black";
const bgGradient = "linear-gradient( 0deg, rgba(18,134,155,0.5046393557422969) 0%, rgba(155, 97, 100, 0.799) 50%, rgba(43, 22, 22, 0.527) 100%)";
document.body.style.backgroundImage = bgGradient;

//Task1:
const imgButt = document.getElementById("imgButt");
const puppy = document.getElementById("puppy");
imgButt.style.backgroundImage = bgGradient;
imgButt.style.width = "100px";
imgButt.style.height = "100px";
imgButt.style.margin = "50px";

imgButt.addEventListener("click", function () {
    if (puppy.style.display === "none") {
        puppy.style.display = "inline-block";
        imgButt.style.backgroundColor = "white";
        imgButt.style.position = "relative";
        imgButt.style.top = "100px";
    }
    else {
        puppy.style.display = "none";
        imgButt.style.backgroundColor = "lightblue";
        imgButt.style.position = "relative";
        imgButt.style.top = "250px";
    }
});

//Task2:
const form1 = document.getElementById("form1");
const input1 = document.getElementById("input1");
const submit = document.getElementById("submit");
submit.style.backgroundImage = bgGradient;
submit.style.width = "100px";
submit.style.height = "100px";
form1.style.marginTop = "200px";

submit.addEventListener("click", function () {
    event.preventDefault();
    const input1Val = input1.value;
    const writeInput = document.createElement("input1");
    writeInput.textContent = input1Val;
    writeInput.style.display = "flex";
    document.body.append(writeInput);
    input1.value = " ";
});