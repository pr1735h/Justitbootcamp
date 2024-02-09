const password = document.getElementById("password");
const genBtn = document.getElementById("genBtn");
const copyBtn = document.getElementById("copyBtn");

function generatePassword() {
    let characters = "0123456789!£$%^&*().,/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYYZ";
    let passwordLength = 12;
    let passwordString = "";
    event.preventDefault();
    for (let i = 0; i < passwordLength; i++) {
        let randomNumber = Math.floor(Math.random() * characters.length);
        passwordString += characters.substring(randomNumber, randomNumber + 1);
        console.log(passwordString);
    }
    password.value = passwordString;
}

function copyPassword() {
    event.preventDefault();
    navigator.clipboard.writeText(password.value);
    alert("Password has been copied to clipboard!");
}

genBtn.addEventListener("click", generatePassword);
copyBtn.addEventListener("click", copyPassword);