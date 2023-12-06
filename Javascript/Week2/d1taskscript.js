const title = document.getElementById("title");
console.log(title);
title.style.color = "red";
title.style.textAlign = "center";
title.style.position = "relative";
title.style.right = "100px";
title.style.textDecoration = "underline solid 3px red";

//
const ul = document.createElement("ul");
for (let i = 1; i <= 3; i++) {
  const li = document.createElement("li");
  ul.append(li);
}
document.body.append(ul);

const liElements = document.querySelectorAll('li');
liElements[0].style.color = 'red';
liElements[0].style.backgroundColor = "lightblue";
liElements[0].innerText = "Changed to this text."
liElements[1].style.color = 'blue';
liElements[1].style.backgroundColor = "crimson";
liElements[1].innerText = "Changed to this text."
liElements[2].style.color = "red";
liElements[2].style.backgroundColor = "lightblue";
liElements[2].innerText = "Changed to this text."

//
title.remove();

//
document.body.style.backgroundColor = "black";
const bgGradient = "linear-gradient( 230deg, rgba(8,134,175,0.5046393557422969) 0%, rgba(5, 97, 202, 0.799) 70%, rgba(243, 22, 22, 0.527) 90%)";
document.body.style.backgroundImage = bgGradient;

//