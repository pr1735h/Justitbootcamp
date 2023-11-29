/* Data types in JavaScript:
1 - String, defined by single or double quotations. (let = "dataType";)
2 - Number, (let = 30;) max value is 999999999999999
3 - BigInt, for numbers bigger than 15 digits (9999999999999999)
4 - Boolean, binary values such as true or false, yes or no and on or off (<,> and == can be used with boolean types, useful for if and then statements)
5 - Undefined, a variable without a value has an undefined data type (let car;) (let bike = undefined;)
6 - Null, variables can have blank or empty values which are still valid as string type (let car = "";)
7 - Symbol, Used to add unique proerty keys to an object that doesn't collide with other object keys. (can be used to encompass or hide data)
8 - Object, Can be an object, array (a string of values seperated by commas) or date. (const person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};)

The typeof operator returns the type of a variable or an expression:
typeof "text" would display as "string"
typeof 8 would display as "number"
typeof false would display as "boolean"
*/


//Converting Strings and Numbers:
let a = "10";  //The datatype of a is string.
let b = 10;    //The datatype of b is number.
let c = 10;    //The datatype of c is number.
let d = "text"; //The datatype is string.
console.log(Number(a) + c + " " + String(b) + " " + Number(d) ); //In this example a is converted from string to number datatype. b from number to string. d from string to number but it has a text value so it displays as 'NaN'

//Converting Binary to numbers:
console.log("Binary to Number:");
console.log(Number(true + true));
console.log(Number(false));

//Converting String to Boolean:
console.log("String to Boolean:");
var Strings = "String always convert to True"
console.log(Boolean(Strings));
console.log(Boolean("False")); // Converts to true because it is a string value.

//Converting Number to Boolean:
console.log("Number to Boolean:")
var num1 = 0;
var num2 = 1;
var num3 = 3;
console.log(Boolean(num1)); //Converts to false because 0 = false and 0 = no as a Boolean type.
console.log(Boolean(num2)); //Convert to true because 1 = true and 1 = yes in Boolean type.
console.log(Boolean(num3)); //Numbers greater than 0 are always true in Boolean type.

//Converting Boolean to Number:
console.log("Boolean to Number:");
var boo1 = true;
var boo2 = false;
var boo3 = true + true + true +true;
console.log(Number(boo1));
console.log(Number(boo2));
console.log(Number(boo3));
console.log(Number(boo3 + 40))
console.log(Number(boo3 * boo3));

//Type Coercion:
//Similar to type conversion but type coercion is performed automatically.
//Number Coercion:
console.log("Number Coercion:");
console.log(true + true + 20); //The value of true is 1 so the operation here is actually 1+1+20
console.log(10 + 1 + "11" + 1 + 10); //The first 2 values are added together but then a string interupts so the rest of the operation is printed as a string.
console.log(true + 10 + 10 + 10 + "22");

console.log(3+4+true+'2'+10+true+11+'2'+1);