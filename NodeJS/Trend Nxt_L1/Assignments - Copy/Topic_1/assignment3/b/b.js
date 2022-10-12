let date_object = new Date();

// current date
// adjusting 0 before single digit date
let date = ("0" + date_object.getDate()).slice(-2);

// current month and year
let month = ("0" + (date_object.getMonth() + 1)).slice(-2);
let year = date_object.getFullYear();

// current minutes,seconds,hours
let min = ("0" + date_object.getMinutes()).slice(-2);
let sec = ("0" + date_object.getSeconds()).slice(-2);
let hours = date_object.getHours();
console.log("Current time : " + hours + ":" + min + ":" + sec);
console.log();
console.log("Current date : " + date + "/" + month + "/" + year);
