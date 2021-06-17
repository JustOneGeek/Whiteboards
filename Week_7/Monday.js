// Create a function that takes a number as an argument. 
// Add up all the numbers from 1 to the number you passed to the function. 
// For example, if the input is 4 then your function should 
// return 10 because 1 + 2 + 3 + 4 = 10.

// Input:
let num1 = 4
// Output:
// 10

// Input:
let num2 = 13
// Output:
// 91

// Input:
let num3 = 500

// Output:
// 125250


// Looping
function addUp(num) {
	let total=0
	for (let i=1;i<=num; i++){
		total+=i
	}
	return total
}
console.log(addUp(num1))
console.log(addUp(num2))
console.log(addUp(num3))

// Recursion
function sumUp(n) {
    if (n == 1) return 1;
    return n + sumTo(n - 1);
  }
  
  console.log(sumUp(num1))
  console.log(sumUp(num2))
  console.log(sumUp(num3))

  
//Math way: https://en.wikipedia.org/wiki/Arithmetic_progression
function sumTo(n) {
    return n * (n + 1) / 2;
  }
  
  
  console.log(sumTo(num1))
  console.log(sumTo(num2))
  console.log(sumTo(num3))
  