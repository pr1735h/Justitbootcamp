//Javascript is case sensitive
//camelCasing isWhen the firstWord of a fileNames startsWith lowerCase andThe secondWord startsWith an upperCase letter, it is reccommended.
/*
For multi line
Comments */
//Inspect elements console is the best way to troubleshoot JS errors.
// console.log('This prints a message in the browsers console');
// console.log(60+5);
// console.error('This message prints as an error in the console which can be used to describe errors')
// console.warn('This prints a warning message in the console')

console.log('Welcome to Javascript');
console.error('Error in the code bruh');
console.warn('Dont do it')
console.clear
console.log("Pressing the button clears the console");
function myFunction() {
  console.clear();
}

// JS Variables //
/*
Variables are custom words which are used to store data or asign values to.
Variables can be undeclared.
x = 5;  <--------------------------¬
y = 6;  <---[these are declarations]
z = x + y;  <----[This is another declaration within an initialisation]
console.log(z) <----[this is a declaration that would print the instructions set by the variables]

Var is the first type of variable and should only be used when writing code for old browsers.
Var does not have block scope.
var x = 5;
var y = 6;
var z = x + y;

Let must be declared before use, cannot be redeclared and have block scope [let x=10;{let x=40;}] works because the second let is in a new block.
Let is used when const can not be used.
let x;
let y;
let x;
x = 5;
y = 6;
z = x + y;

Const cannot be redeclared, have block scope, cannot be reassigned and should be initialised in the declaration.
Const is used when the value or type should not change.
Const should be the most used variable.
const x = 5;
const y = 6;
const z = x + y;

Const and let can be used together.
const x = 5;
const y = 6;
let z = x + y;
*/

const a = 2;
const b = 22;
const c = a + b;
console.log(c);

let x;
let y;
let z;
x= 1;
y= x + 10;
z= y + 100;
console.log(z+1000);

console.log(c,z)

//I have used let for the first variable because its value needs to be changed, the rest are const because they are constantly the same value.
let fastFood = "Pizza";
const favColour = "Red";
const favDrink = "Lemonade";
const bday = "14/01/1994"
fastFood = "Pasta"
console.log(favDrink, fastFood, favColour, bday)