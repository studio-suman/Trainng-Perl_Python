const implement = require("./Math");

const addition = implement.add(16, 8);
const subtraction = implement.sub(16, 4);
const multiplication = implement.mul(16, 16);
const division = implement.div(16, 2);
console.log(`The Result of addition is ${addition}`);
console.log(`The Result of subtraction is ${subtraction}`);
console.log(`The Result of multiplication is ${multiplication}`);
console.log(`The Result of division is ${division}`);
