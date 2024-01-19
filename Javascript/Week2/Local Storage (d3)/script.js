// Access all our relevant elements from the DOM
const keyInput = document.getElementById("keyInput");
const valueInput = document.getElementById("valueInput");
const saveBtn = document.getElementById("saveBtn");
const deleteBtn = document.getElementById("deleteBtn");
const storageOutput = document.getElementById("storageOutput");
const searchInput = document.getElementById('searchInput');
const searchOutput = document.getElementById('searchOutput');
const searchBtn = document.getElementById('searchBtn');

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

// Calling the saveToLocalStorage function on click of the save button
saveBtn.addEventListener('click', saveToLocalStorage);
console.log(localStorage);

// 1: A button that clears local storage
const clearLocalStorage = () => {
    // Clear local storage
    localStorage.clear();
    // Refresh the page after clearing 
    location.reload();
}

// Calling the clear LS function on click of the delete button 
deleteBtn.addEventListener('click', clearLocalStorage);

// 2: Output the items from local storage
for (let i = 0; i < localStorage.length; i++) {
    // Get the key string value by using the .key() method to
    // retrieve the value of the key at the relevant index
    let key = localStorage.key(i);
    // Get the value associated to the key but using the key variable
    // as the argument for our .getItem() method
    let value = localStorage.getItem(key);
    // Create the element to store the data
    let lsItem = document.createElement('h3');
    // Assign the data to the innerText of the element
    lsItem.innerText = `${key}: ${value}`;
    // Add the element to the div for LS output
    storageOutput.append(lsItem);
}

// 3: Search through local storage for a specific key/value pair
const searchResult = document.createElement('h3');
searchOutput.append(searchResult);

const searchLocalStorage = (e) => {
    // Preventing the default page reload when a form is submitted
    e.preventDefault();
    // Assigning the value from the search input to the key variable
    let key = searchInput.value;
    // Using the search term in the key variable as the argument for .getItem()
    let result = localStorage.getItem(key);
    // Using the key and the result of .getItem() as the search result text
    searchResult.innerText = `Search Result: ${key}: ${result}`;
    // resetting the input to empty
    searchInput.value = "";
}

// Calling the search function on click. 
searchBtn.addEventListener('click', searchLocalStorage);

