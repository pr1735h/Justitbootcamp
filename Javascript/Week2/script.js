console.log(document);

//Get document by ID:
const title = document.getElementById("title");
console.log(title);

//Get document by Class:
const listItems = document.getElementsByClassName("listItems");
console.log(listItems);

//Get document by Tag:
const liElements = document.getElementsByTagName("li");
console.log(liElements);

//Get document by Selector:
const paragraph = document.querySelector("p");
console.log(paragraph);

//Get document by SelectorAll:
const paragraphs = document.querySelectorAll("p");
console.log(paragraphs);

//Styling elements with JavaScript:
title.style.color = "Red";
title.style.textAlign = "right";
title.style.position = "relative";
title.style.right = "200px";

//Styling multiple elements with JavaScript:
for (i = 0; i < paragraphs.length; i++) {
    paragraphs[i].style.color = "Orange";
}

//Adding new HTML elements with JavaScript:
//Store the "ul" in a variable;
const ul = document.querySelector("ul");
console.log(ul)
//Create the element;
const newListItem = document.createElement("li");
console.log(newListItem);
//Append the created element;
ul.append(newListItem);
//Add Inner text;
newListItem.innerText = "List Item 5";

//Set an ID to an element:
newListItem.setAttribute("id", "itemFive");
//Remove an Element:
newListItem.removeAttribute("id");

//Set a Class to an element:
newListItem.classList.add("newListItems");
//Remove a Class:
newListItem.classList.remove("newListItems");

//Remove an element from DOM:
newListItem.remove();

//
console.clear();

//
