/*Assignment 1:
a) Create a Node JS Script file that displays hostname & platform details of current system on the console.(Hint : Use OS module)
b) Create a Node JS script file that displays “Hello” text in red color and “Welcome to Node JS” text in rainbow colors on the console. (Hint: Use Colors module)
c) Create a user defined module named “Math” with four functions Addition, Subtraction, Multiplication, Division and export them. Import Math module form other Node JS Script file and invoke all the four functions to perform operations on given input.
d) Create a Node JS Script that displays a message “ Welcome to Node JS” through loop, with delay in between the iterations
    i. Using setTimeOut()*/

// Declarations Below

var os = require('os');
var colors = require('colors');
var calc = require('./Calc_modules');

//***************************************************** */

console.log("os.hostname():\n",os.hostname());
console.log("os.platform():\n",os.platform());

//***************************************************** */

console.log('Hello'.red); // outputs green text
console.log('Welcome to Node JS'.rainbow); // rainbow

//****************************************************** */

var first = 50, second = 20;

console.log("Addition of 50 and 20: " +calc.add(first,second));
console.log("Subtract of 50 and 20: " +calc.sub(first,second));
console.log("Multiplication of 50 and 20: " +calc.mul(first,second));
console.log("Division of 50 and 20: " +calc.div(first,second));

//******************************************************* */

function wlcmmsg(){
   console.log('Welcome to Node JS');
}

setInterval(wlcmmsg,1000);

//***************************************************** */
