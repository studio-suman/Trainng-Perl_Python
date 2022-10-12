function f() {
  console.log("Welcome to Node JS");
}
//here we wil print the message for 10 times with an interval of 10 seconds
for (let i = 1; i <= 10; i++) {
  setTimeout(() => f(), i * 1000);
}
