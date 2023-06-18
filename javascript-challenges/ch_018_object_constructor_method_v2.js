/*
You are working on a Contact Manager app.

You have created the contact object constructor, which has two arguments, name and number.

You need to add a print() method to the object, which will output the contact data to the console in the following format: name: number

The given code declares two objects and calls their print() methods. Complete the code by defining the print() method for the objects.
*/

function contact(name, number) {
  this.name = name;
  this.number = number;
}

function print() {
  console.log(`${this.name}: ${this.number}`);
}

contact.prototype.print = print;
var a = new contact('David', 12345);
var b = new contact('Amy', 987654321);
a.print();
b.print();
