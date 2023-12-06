const title = document.getElementById("title");
const addBtn = document.getElementById("addBtn");
const rmvBtn = document.getElementById("rmvBtn");

// title.addEventListener("click", () => {
//     console.log("The <h1> element as been clicked")
// })
let greeting = () => {
    console.log("hello");
}
title.addEventListener("click", greeting);

title.addEventListener("click", (e) => {
    console.log(e);
});

window.addEventListener("keypress", (e) => {
    console.log(e.key);
});

window.addEventListener("click", (e) => {
    console.log(e.x, e.y);
});

//
addBtn.addEventListener("click", () => {
    let newElement = document.createElement("h2");
    newElement.innerText = "New Element";
    container.append(newElement);
});

rmvBtn.addEventListener("click", () => {
    container.lastElementChild.remove();
});