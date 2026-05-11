let x = 50;
let y = 10;

console.log("Сума 50 + 10 =", x + y);

let d = x * y;
console.log("Значення d (x * y) =", d);

let firstName = "Віктор";
let lastName = "Сатановський";
let age = 19;

d /= y;   
x -= d;   
age += x; 

console.log(firstName + " " + lastName + " " + age);

if (age >= 18) {
    console.log("студент повнолітній");
} else {
    console.log("студент неповнолітній");
}

age = "18";
console.log("Результат нестрогої рівності (==):", age == 18);
console.log("Результат строгої рівності (===):", age === 18);

let N = 16;
let maxLimit = 10 * N; // 160

console.log(`Непарні числа від 1 до ${maxLimit}:`);
for (let i = 1; i <= maxLimit; i += 2) {
    console.log(i);
}