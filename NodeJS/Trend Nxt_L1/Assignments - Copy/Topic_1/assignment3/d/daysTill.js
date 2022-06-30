// One day Time in milliseconds
let one_day = 1000 * 60 * 60 * 24;

let present_date = new Date();

// 0-11 is Month in JavaScript
let christmas_day = new Date(present_date.getFullYear(), 11, 25);
let mothers_day = new Date(present_date.getFullYear(), 04, 10);
let birth_day = new Date(present_date.getFullYear(), 11, 05);

// To Calculate next year's Christmas
if (present_date.getMonth() == 11 && present_date.getdate() > 25)
  christmas_day.setFullYear(christmas_day.getFullYear() + 1);

if (present_date.getMonth() == 04 && present_date.getdate() > 10)
  mothers_day.setFullYear(mothers_day.getFullYear() + 1);

if (present_date.getMonth() == 11 && present_date.getdate() > 05)
  birth_day.setFullYear(birth_day.getFullYear() + 1);

// result in milliseconds converted to days
let Result_christmas =
  Math.round(christmas_day.getTime() - present_date.getTime()) / one_day;
let Final_Result_christmas = Result_christmas.toFixed(0);

//mothers day result
let Result_mothers =
  Math.round(mothers_day.getTime() - present_date.getTime()) / one_day;
let Final_Result_mothers = Result_mothers.toFixed(0);

//birthday result
let Result_birth =
  Math.round(birth_day.getTime() - present_date.getTime()) / one_day;
let Final_Result_birth = Result_birth.toFixed(0);

console.log(
  "\nNumber of days remaining till christmas from\n" +
    present_date +
    "\nto " +
    christmas_day +
    "\nis :  " +
    Final_Result_christmas +
    " days.\n"
);
console.log(
  "Number of days remaining till Mothers day from\n" +
    present_date +
    "\nto " +
    mothers_day +
    "\nis :  " +
    Final_Result_mothers +
    " days.\n"
);
//-ve value means the day has passed
console.log(
  "Number of days remaining till Birthday from\n" +
    present_date +
    "\nto " +
    birth_day +
    "\nis :  " +
    Final_Result_birth +
    " days."
);
