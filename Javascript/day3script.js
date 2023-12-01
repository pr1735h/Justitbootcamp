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
let userName = "Pritesh";
let passWord = "passwrd";
if(userName == "Pritesh" && passWord == "password")
{console.log("Logged in succesfully");}
else{
    console.log("Username or Password is incorrect!");
}

//
let num1 = 10;
let num2 = 20;
let num3 = 10;
if(num1 > num2)
{console.log(num1);}
else
{console.log(num2);}

if(num1 == num3)
{console.log(String(num1) + " " + String(num3));}

//
console.clear();

//Switch Statements:
//Usefull when you have one condition being checked against multiple classes.
let day = "Moday";
switch(day)
{   
    case "Monday":
        console.log("Today is Monday");
        break; //Used to stop the execution if the condition is met. Without it the rest of the conditions will be checked and potentially executed.
    case "Tuesday":
        console.log("Today is Tuesday");
        break;
    case "Wednesday":
        console.log("Today is Wednesday");
        break;
    case "Thursday":
        console.log("Today is Thursday");
        break;
    case "Friday":
        console.log("Today is Friday");
        break;
    case "Saturday" , "Sunday":
        console.log("It is the Weekend");
        break;
    default: //Set the condition that is executed if none of the pervious conditions were met. If this happens without a default the whole switch won't be executed.
        console.log("That is not a day")
}

//
let score = 42;
switch(true)
{
    case score >=100:
        console.log("Perfect");
    break;
    case score >=80:
        console.log("Excellent");
    break;
    case score >=60:
        console.log("Good");
    break;
    case score >=40:
        console.log("Ok");
    break;
    case score >=20:
        console.log("Bad");
    break;
    default:
        console.log("Fail");
}

let pWord = "Password123123";
let len = pWord.length;
switch(true)
{
    case pWord.length >= 8:
        console.log("The password is " + len + " characters long");
    break;
    case pWord.length >= 1:
        console.log("The password is too short");
    break;
    default:
        console.log("Please enter a password!");
}