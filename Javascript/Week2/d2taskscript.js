//Task1:
const imgButt = document.getElementById("imgButt");
const puppy = document.getElementById("puppy");
imgButt.style.backgroundColor = "green";
imgButt.style.width = "100px";
imgButt.style.height = "100px";

imgButt.addEventListener("click", function () {
    if (puppy.style.display === "none") {
        puppy.style.display = "block";
        imgButt.style.backgroundColor = "crimson";
    }
    else {
        puppy.style.display = "none";
        imgButt.style.backgroundColor = "lightblue";
    }
});

//Task2:
const form1 = document.getElementById("form1");
const input1 = document.getElementById("input1");
const submit = document.getElementById("submit");
submit.style.width = "100px";
submit.style.height = "100px";

submit.addEventListener("click", function () {
    event.preventDefault();
    const input1Val = input1.value;
    const writeInput = document.createElement("input1");
    writeInput.textContent = input1Val;
    writeInput.style.display = "flex";
    document.body.append(writeInput);
    input1.value = " ";
});