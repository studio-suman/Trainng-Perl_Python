var refModule = require('./LiteralDemo.js');
var funModule = require('./Functions.js');
iDuration = 12;
console.log(refModule.iDuration);
console.log(' iDuration = ' + iDuration);

console.log(' sTraining = ' + refModule.sTraining);
console.log(' Employee Info. = ' + refModule.objEmployee.sName);

refModule.addNumbers(12,18);

funModule();