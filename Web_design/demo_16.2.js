console.log("--- Тестування простих функцій ---");

// 1. Функція з параметрами, яка повертає результат 
function sum(x, y, z) {
    return x + y + z;
}
console.log("Результат sum: ", 10 + sum(2, 3, 4) + sum(1, 1, 1)); 

// 2. Функція з одним параметром, яка просто виводить текст
function sayHello(name) {
    console.log("Привіт, " + name + "!");
}
sayHello("Віктор"); 

// 3. Функція без параметрів
function printSomeNumber() {
    console.log(42);
}
printSomeNumber();


console.log("\n--- Підрахунок вартості товарів ---");

// Універсальна функція для підрахунку суми будь-якого масиву товарів
function getTotalCost(products) {
    let result = 0;
    for (let product of products) {
        result += product.price;
    }
    return result;
}

// Масив усіх товарів на складі
let storeProducts = [
    { name: "Samsung J5 2017", price: 5400 },
    { name: "iPhone X", price: 25000 },
    { name: "Xiaomi Mi 4", price: 4999 },
    { name: "Чохол для iPhone X", price: 500 }
];

// Викликаємо функцію для складу
let totalCost = getTotalCost(storeProducts);
console.log("На складі товарів на " + totalCost + " грн.");

let orderProducts = [
    { name: "iPhone X", price: 25000 },
    { name: "Чохол для iPhone X", price: 500 }
];

// Знову викликаємо ТУ САМУ функцію, але передаємо інший масив 
totalCost = getTotalCost(orderProducts);
console.log("Сума замовлення: " + totalCost + " грн.");