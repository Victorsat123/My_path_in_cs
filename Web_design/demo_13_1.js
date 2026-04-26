let currentDate = new Date();

let day = currentDate.getDate();
let month = currentDate.getMonth() + 1; // Додаємо 1, бо місяці з 0
let year = currentDate.getFullYear();

if (day < 10) day = '0' + day;
if (month < 10) month = '0' + month;

console.log("Добрий день! Сьогодні " + day + "." + month + "." + year);
