let computerGuess;
let userGuesses = [];
let attempts = 0;
let maxGuesses;

let low = 1;
let high = 100;

function updateRange() {
    const rangeOutput = document.getElementById("rangeOutput");
    rangeOutput.innerText = `${low} - ${high}`
    rangeOutput.style.marginLeft = low + "%";
    rangeOutput.style.marginRight = 100 - high + "%";
    rangeOutput.classList.add("flash");
    const lowValue = document.getElementById("low");
    lowValue.style.flex = low + "%";
    lowValue.style.background = "#ef7b54";
    const space = document.getElementById("space");
    space.style.flex = high - low + "%";
    space.style.background = "#83e1d0";
    const highValue = document.getElementById("high");
    highValue.style.flex = 100 - high + "%";
    highValue.style.background = "#ef7b54";
}

function gameEnded() {
    document.getElementById("newGameButton").style.display = "inline";
    document.getElementById("inputBox").setAttribute("readonly", "readonly");
}

function newGame() {
    window.location.reload();
}

function init() {
    computerGuess = Math.floor(Math.random() * 100 + 1);
    console.log(computerGuess);
    document.getElementById("newGameButton").style.display = "none";
    document.getElementById("gameArea").style.display = "none";
}

function startGameView() {
    document.getElementById("welcomeScreen").style.display = "none";
    document.getElementById("gameArea").style.display = "block";
}

function easyMode() {
    maxGuesses = 10;
    startGameView()
}

function hardMode() {
    startGameView()
    maxGuesses = 5;
}

function compareGuess() {
    const userGuess = Number(document.getElementById("inputBox").value);
    userGuesses.push(" " + userGuess);
    document.getElementById("guesses").innerHTML = userGuesses;
    attempts++;
    document.getElementById("attempts").innerHTML = attempts;
    if (attempts < maxGuesses) {
        if (userGuess > computerGuess) {
            if (userGuess < high) high = userGuess;
            document.getElementById("textOutput").innerHTML = "Your guess is too high";
            document.getElementById("inputBox").value = "";
        }
        else if (userGuess < computerGuess) {
            if (userGuess > low) low = userGuess;
            document.getElementById("textOutput").innerHTML = "Your guess is too low";
            document.getElementById("inputBox").value = "";
        }
        else {
            document.getElementById("textOutput").innerHTML = "You win! You guessed it in " + attempts + " tries!";
            gameEnded()
        }
    }
    else {
        if (userGuess > computerGuess) {
            document.getElementById("textOutput").innerHTML = "YOU LOSE! <br> The number was " + computerGuess;
            gameEnded()
        }
        else if (userGuess < computerGuess) {
            document.getElementById("textOutput").innerHTML = "YOU LOSE! <br> The number was " + computerGuess;
            gameEnded()
        }
        else {
            document.getElementById("textOutput").innerHTML = "You win! You guessed it in " + attempts + " tries!";
            gameEnded()
        }
    }
    updateRange();
}