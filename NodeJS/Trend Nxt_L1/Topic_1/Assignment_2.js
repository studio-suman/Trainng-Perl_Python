/* Assignment 2: 
a) Create a NodeJS based script file, that provides implementation for ‘pwd’ command from ‘Node’ shell. 
b) Create a NodeJS based script file, that reads the name of the directory from the command line arguments and displays the list of directory contents (using fs module) 
c) Create a Node JS script that reads the file name from console and displays the contents of the file 
	i. Synchronous mode 
	ii. Asynchronous mode 
d) Create a NodeJS based script file, that reads the names of the 2 files from the user (Use process module; On stdin “data” event by using call-back accept the input from the user) and reads the content of first file 
by using Read Stream API and writes in into second file by using Write Stream API. 
If second file is available it should append the content. 
If not it should create a new file and add the content to it.*/

var fs = require('fs');
const readline = require('readline-sync');

//******************************************************** */

console.log(`Current directory: ${process.cwd()}`);  

//******************************************************* */

fs.readdir('C:\\Users\\HSASS\\OneDrive - Wipro\\Desktop\\Trainng-Perl_Python\\NodeJS\\NodeExample',function(refError,objFiles){
    if (refError)
       console.log(' Error in Accessing the directory ' );
    objFiles.forEach(function(refFile){
        console.log(refFile);
    });
});

//******************************************************* */
 
let name = readline.question("Please enter the file Name: ");

// Asynchronous read 

fs.readFile(name, function (err, data) {  
   if (err) {  
       return console.error(err); 
   }  
   console.log("Asynchronous read: " + data.toString());  
});  
// Synchronous read  
var data = fs.readFileSync(name);  
console.log("Synchronous read: " + data.toString());  
console.log("Program Ended");  