const events = require("events");
const eventEmitter = new events.EventEmitter();
var one = function FirstEvent() {
  console.log("First Event");
};
eventEmitter.on("one", one);
var two = function SecondEvent() {
  console.log("Second Event");
};
eventEmitter.on("two", two);
var three = function ThirdEvent() {
  console.log("Third Event");
};
eventEmitter.on("three", three);
eventEmitter.emit("one");
eventEmitter.emit("two");
eventEmitter.emit("three");
