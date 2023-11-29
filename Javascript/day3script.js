//Conditional Statements:
let weather = "Rain"
if(weather=="Sunny")
{
    console.log("Wear a hat and sunglasses")
}
else if(weather=="Rainy")
{console.log("Take an umbrella with you")}
else{
    console.log("The weather is temperate")
}
//Operators:
/*Can be of the following types;
Arithmetic Operators
Assignment Operators
Comparison Operators
Logical Operators
Conditional Operators
Type Operators
https://www.w3schools.com/jsref/jsref_operators.asp */

// = Does not mean equal to, it means that something 'has the value of'.
let v1 = 20; //The variable 'v1' has the value of '20'.
let v2 = 30; //The variable 'v2' has the value of '30'.
v1 = v2; //The new value of the variable 'v1' is now the value of the variable 'v2'.
console.log(v1); //The original value of 'v1' was changed to the value of 'v2' so it correctly prints as '30'.

// == Checks whether the value is equal.
let a = 5;
let b = 4;
console.log(a==5) //The value is equal so it prints as 'true'.
console.log(a - 1 == b) //This value is also true.
console.log(a==6) //The value is not equal so it prints as 'false'.

if(b + 1 == a)
{console.log(5);}
else
{console.log("Incorrect maths");}

// === Checks whether the value and type are the same.
let c = 6;
let d = "6";
let e = 6;

if(c === e)
{console.log("Same");}
else{console.log("Not Same");}

if(c === d)
{console.log("Same");}
else
{console.log("Not Same");}

// != Means not equal to.
if(a != b)
{console.log("Not equal");}

// ++ Increment:
if(v1 = v2)
{console.log(v1 = ++ v1);}

// -- Decrement:
if(a > b)
{console.log(a = -- b);}

// && And:
let num12 = 12;
if(num12 >10 && num12 <5) //This line is checking if the variable 'num12' has a value greater than 10 AND less than 5.
{console.log(true);}
else{console.log(false);}

// % Remainder:
if(num12 % 2 == 0) //Checks if the value of the variable 'num12' has a remainder after being divided by 2.
console.log("Even"); //The value does not have a remainder so it prints as 'Even'.
else{console.log("Odd");} 

let num13 = 13;
if(num13 % 2 != 0) //Checks if the value of the variable 'num13' has a remainder after being divided by 2.
console.log("Not Even"); //The value does not divide by 2 so it prints as 'Not Even'.
else(console.log("Not Odd"))

//