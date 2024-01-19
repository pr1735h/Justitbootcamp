//Task1:
const name1 = document.getElementById("name1");
const nameBtn = document.getElementById("nameBtn");
const nameGreet = document.getElementById("nameGreet");

function greetName() {
    event.preventDefault();
    const name1Val = name1.value;
    const text = document.createElement("p");
    text.innerHTML = "Hello, " + name1Val + "!";
    nameGreet.appendChild(text);
}
nameBtn.addEventListener("click", greetName);

//Task2:
const val1 = document.getElementById("val1");
const val2 = document.getElementById("val2");
const sumOfBtn = document.getElementById("sumOfBtn");
const sumOf = document.getElementById("sumOf");

function addition() {
    event.preventDefault();
    const value1 = parseInt(val1.value);
    const value2 = parseInt(val2.value);
    const result = value1 + value2;
    const resultElement = document.createElement("p");
    resultElement.innerHTML = "The sum of " + value1 + " and " + value2 + " is " + result;
    sumOf.appendChild(resultElement);
}

sumOfBtn.addEventListener("click", addition);

//Task3:
const colIn = document.getElementById("colIn");
const colBtn = document.getElementById("colBtn");

function textToColour(event) {
    event.preventDefault();
    const colOut = document.getElementById("colOut");
    const colVal = colIn.value;
    const text = document.createElement("p");
    text.style.color = colVal;
    text.style.textDecoration = "underline 2px";
    text.style.textDecorationColor = colVal;
    text.innerHTML = "This colour is " + colVal + "!";
    colOut.appendChild(text);
}

colBtn.addEventListener("click", textToColour);