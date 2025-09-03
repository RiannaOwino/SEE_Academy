const birthYear = 2005
console.log('I was born in ' + birthYear);

const firstName = "Rianna"
console.log(firstName)

//arithmetic operators//
console.log(7 + 7)
console.log(7 * 7)
console.log(7 / 7)
console.log(7 % 7)

//comparison operators(true/false)//
console.log(5 == "5") //true because it compares only the numbers with two equal signs
console.log(5 === "5") //false because it compares both the numbers and one equal sign, so they are not the same

// functions

function greetUser(firstName) {
  return `hello, ${firstName}`;
}
console.log(greetUser("Rianna")); // should print hello, Rianna

//example of a function that turns farenheit to celsius

function toCelsius(f) {
  return (5/9) * (f-32);
}
console.log(toCelsius(104));

//loops

//while loop counting from 7 to 10

let num = 7;
while (num <= 10) {
  console.log(`Number: ${num}`);
  num++; // Increment num to avoid infinite loop
}

//for loop
const characters = ["Saiki", "Gojo", "PBG", "Haruhi", "Hachi", "Yuji"];

let text = "";
for (let i = 0; i < characters.length; i++) {
  text += characters[i] + "<br>";
}
console.log(text);

// DOM (document object model)

// selecting elements by id

