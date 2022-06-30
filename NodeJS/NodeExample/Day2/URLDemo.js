var objURL = require('url');
var sStrURL = 'http://localhost:8080/Demo.html?Trng=Node JS&Mode=WebEx';

/* Used to parse an Address and return a URL object with each part of the address properties */
 var sQuery = objURL.parse(sStrURL, true);

/* Displays the HostName  or  Domain Name*/
 console.log(' Domain Name = ' + sQuery.host); 

/* Displays the Name of the File */
 console.log(' File Name = ' + sQuery.pathname); 
/* Display the Query Parameters */
console.log(' Parameters = ' + sQuery.search); 

console.log(' Query Parameters ');
/* Returns the Query Parameter as an Object */
 var objQryPrm = sQuery.query; 
for(var sKeys in objQryPrm){
   console.log(sKeys + ":" + objQryPrm[sKeys]);
}
