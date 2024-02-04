//Declare the body as a variable:
const forest = document.getElementById("forest");
//Create a function that makes an image after the body loads:
function loadBigFoot() {
    //Creating the image and decalring it is as a let variable so it's attributes can be changed:
    let bigFoot = document.createElement("img");
    bigFoot.setAttribute("src", "https://raw.githubusercontent.com/pr1735h/Justitbootcamp/main/Project1/images/bigfoot.png");
    bigFoot.setAttribute("width", "44");
    bigFoot.setAttribute("height", "50");
    bigFoot.setAttribute("alt", "Big Foot");
    bigFoot.setAttribute("class", "bigFoot1");
    bigFoot.setAttribute("position", "relative");
    bigFoot.setAttribute("id", "monkeyMan");
    //Appending image in the body:
    forest.appendChild(bigFoot);
}
//Calling the function so it executes:
loadBigFoot();

//Create a function that makes the Big Foot image randomly move around the window:
function moveBigFoot() {
    let bigFoot = document.getElementById("monkeyMan");
    //Declare window size in variables:
    let w = visualViewport.width;
    let x = visualViewport.height;
    //Declare rng based on window size minus image size so it never leaves the screen:
    let y = Math.random() * w - 100;
    let z = Math.random() * x - 300;
    //Change style attributes using rng:
    bigFoot.style.top = y + "px";
    bigFoot.style.left = z + "px";
}
//Call the function:
moveBigFoot();

//Create a function that creates an alert box:
function youWin() {
    window.alert("YOU FOUND BIGFOOT!");
}
//Create function that records score:
let score = document.getElementById("p1");
let recordScore = function () {
    if (score.innerText == "") {
        var value = 1;
    }
    else {
        let prevScore = Number(score.innerText);
        var value = prevScore + 1;
    }
    return value;
};
//Combine previouse functions under one function:
function winCondition() {
    moveBigFoot();
    youWin();
    bigFootImage.style.border = "none";
    score.innerText = `${recordScore()}`;
}

//Event when Big Foot image is clicked:
const bigFootImage = document.getElementById("monkeyMan");
bigFootImage.addEventListener("click", winCondition);

//Declare button as a variable:
const hint = document.getElementById("hint");

//Added a hint feature in  v1.1:
function hintAndReset(original) {
    return function () {
        const originalResult = original.apply(this, value);
        return originalResult = 0;
    }
}
hint.addEventListener("click", function () {
    score.innerText = "0";
    bigFootImage.style.border = "5px solid yellow";
    bigFootImage.style.borderRadius = "10px";
});
