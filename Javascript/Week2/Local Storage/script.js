// Access all our relevant elements from the DOM
const keyInput = document.getElementById("keyInput");
const valueInput = document.getElementById("valueInput");
const saveBtn = document.getElementById("saveBtn");
const clear = document.getElementById("clear");
// Function that will save input data to localStorage
const saveToLocalStorage = () => {
    // Store the data from the key and value inputs
    // inside varaibles named "key" and "value"
    let key = keyInput.value;
    let value = valueInput.value;

    // Check if the inputs have value when the button is clicked
    // If they do, add the key:value pair to localStorage
    if (key && value) {
        localStorage.setItem(key, value);
    }
}

const clearLocStore = () => {
    localStorage.clear();
}
// Calling the saveToLocalStorage function on click of the save button
saveBtn.addEventListener("click", saveToLocalStorage);
clear.addEventListener("click", clearLocStore);
console.log(localStorage);

for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    const value = localStorage.getItem(key);
    console.log(`${key}: ${value}`);
}

//
const searchBar = document.getElementById("searchBar");
const searchValue = searchBar.value;
const localStorageValue = localStorage.getItem("key");
const searchButt = document.getElementById("searchButt");
const storageOutput = document.getElementById("storageOutput");
const searchInput = searchBar;
for (let i = 0; i < localStorage.length; i++) {
    let key = localStorage.key(i);
    let value = localStorage.getItem(key);
    let lsItem = document.createElement("h3");
    lsItem.innerText = `${key}: ${value}`;
    storageOutput.append(lsItem);
}

const searchResult = document.createElement("h3");
searchOutput.append(searchResult);
const searchLocalStorage = (e) => {
    e.preventDefault();
    let key = searchInput.value;
    let result = localStorage.getItem(key);
    searchResult.innerText = `Search Result: ${key}: ${result}`;
    searchInput.value = "";
}
searchButt.addEventListener("click", searchLocalStorage);