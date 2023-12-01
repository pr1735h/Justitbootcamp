function conClear()
{ 
    console.clear();
}

//Arrays:
//Used to store multiple values in a single variable.
//Values are seperated by commas, in a [square bracket list].
//Each Value has an index-value starting from 0.
//Specific Values can be called by using the index number, seperating them using commas e.g. myList[3], myList[2]
let myList = ["Item1", "Item2", "Item3", 1000, true];
myList[3] = myList[3] - 200; //Values in an array can be manipulated in various ways.
myList[4] = Number(myList[4]);
console.log(myList[0], myList[4]);
console.log(myList[3]);

myList.splice(5,0,"New Item"); //Syntax for this is (the index to place item in, which item to remove, value of item);
console.log(myList);

//Loops:
//Loops are used in Javascript to peform repeated tasks based on a condition.

for(let a=1; a<=10; a++)
{
    console.log("Test Loop")
}

//
let colours = [
    "Blue",
    "Green",
    "Red",
    "Yellow",
    "Orange",
    "Black",
    "Purple",
    "Pink",
    "Brown",
    "Blue",
    "Green",
    "Red",
    "Yellow",
    "Orange",
    "Black",
    "Purple",
    "Pink",
    "Brown"
]

for(let i=0; i<=colours.length-1; i++)

{
    if(i==5)
    {break;}
    else
    {console.log(colours[i]);}
}

//
let numbers=[10,20,30,40,50,60,70,80,90,100];
for(let n=0; n<=numbers.length-1; n++)
{
    if(numbers[n]==100+10)
    {break;}
    else
    {console.log(numbers[n]);}
}

//
for(i=1; i<=10; i++)
{
    console.log(`2 * ${i} = ${2*i}`);
}

for(let i=10; i>=1; i--)
{console.log(i);}

//
//While Loops:
//While loops are used when the number of iterations is uncertain, but there is a condition to be checked beofre each iteration.
//If the condition is not correct it will not execute.
let num1 = 100;
while(num1<=10)
{
    console.log(num1);
    num1++;
}

//Do-While loops:
//Similar to while loop but it checks the condition after the block of code is executed.
let num2 = 1;
do
{
    console.log(num2);
    num2++;
}
while (num2 <=11)

//
conClear();

//For of loops:
//Iterate through an array.
let list1=["Item1","Item2","Item3","Item4","Item5","Item6","Item7","Item8"];
for(let item of list1)
{console.log(list1)}

//
let hi="Hello";
for (let i=0; i<hi.length; i++) {
    console.log(hi[i]);
}

for (let i=hi.length-1; i>=0; i--) {
    console.log(hi[i]);
}

//
function Palindrome(str) {
    let len = str.length;
    for (let i = 0; i < len / 2; i++) {
      if (str[i].toUpperCase() !== str[len - 1 - i].toUpperCase()) {
        return str +" is not a palindrome";
      }
    }
    return str +" is a palindrome!";
  }
console.log(Palindrome("Racecar"));
console.log(Palindrome("WQ!--#--!qw"));

//Alternate method:
function checkPalindrome(word)
{
let max=word.length-1;
let min=0;
while(max>=min)
{
    if(word[min].toUpperCase()==word[max].toUpperCase())
    {
        min++;
        max--;
    }
    else
    {
        return `${word} is not Palindrome`;
    }
}
return `${word} is Palindrome`
}
console.log(checkPalindrome('Mom'));

