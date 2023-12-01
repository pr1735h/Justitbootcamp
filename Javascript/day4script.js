/*function name(parameter1, parameter2, parameter3) 
{
  code to be executed
}
*/
function conClear()
{console.clear();}

function hello(name1, name2)
{console.log(`Hello ${name1}, ${name2} `);} //uses backticks

hello(`FirstName`, `LastName`);
hello(`Pritesh`, `Hirani`);

function sum(num1, num2)
{
    return num1+num2;
}
console.log(sum(30,3));

//
let val1 = 1 + 5;
let val2 = 6;
function greaterThan()
{
    
    if(val1 > val2)
    {console.log(val1);}
    else if (val1 == val2)
    {console.log("The values are equal")}
    else
    {console.log(val2);}
}

greaterThan();

//
function checkNumber(number)
{
    if(isNaN(number))
    {console.log("This is not a number");}
    else
    {console.log("This is a number");}
}

checkNumber();

//
function multiply(num4, num5)
{
    return num4 * num5;
}

console.log(multiply(5, 20));

//
function lessThan(val3, val4)
{
    
    if(val3 < val4)
    {console.log(val3);}
    else if (val3 == val4)
    {console.log("The values are equal")}
    else
    {console.log(val4);}
}

lessThan(10, 1);
//
conClear();

//Objects:
let book = {
    books:
[{
    name: "The Lion The Witch And The Wardrobe",
    author: "C.S.Lewis",
    series: "The Chronicles Of Narnia",
    published: "16/10/1950",
    genre: "Fantasy, Fiction",
    pages: 172,
},
{
    name: "Prince Caspian",
    author: "C.S.Lewis",
    series: "The Chronicles Of Narnia",
    published: "15/10/1951",
    genre: "Fantasy, Fiction",
    pages: 195,
},
{
    name: "The Voyage of the Dawn Treader",
    author: "C.S.Lewis",
    series: "The Chronicles Of Narnia",
    published: "15/09/1952",
    genre: "Fantasy, Fiction",
    pages: 223,
},
]
}

console.log(book); //Displays the whole group array.
console.log(book.books[0]); //Displays the first index from within the array.
console.log(book.books[1].series); //Displays the value of 'series' from the second index.
console.log(book.books[2].name, book.books[2].pages); //Displays the value of 'name' and 'pages' from the third index.

//
conClear();
//

let learner = {
    firstName: "Pritesh",
    lastName: "Hirani",
    age: 29,
    tutor: "Zaki",
    course: "Software Skills"
}

console.log(learner.firstName, learner.lastName)

//
const alarm =
{
    weekDay: "Wake up, it's  7.30am",
    weekEnd: "You're awake when you want to be.",
    checkAlarm: function(day){
        if(day=="Saturday" || day=="Sunday")
        {console.log(this.weekEnd);}
        else
        {console.log(this.weekDay);}
    }
}

alarm.checkAlarm("Friday");
