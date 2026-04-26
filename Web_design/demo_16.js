// 1. Створюємо масив об'єктів (каталог телефонів)
let products = [
    { name: "Samsung J5 2017", screen: 5.2, price: 5400, weight: 160 },
    { name: "iPhone X", screen: 5.8, price: 25000, weight: 170 },
    { name: "Xiaomi Mi 4", screen: 5.5, price: 4999, weight: 150 },
    { name: "Nokia 3310 2018", screen: 2.4, price: 999, weight: 60 },
    { name: "iPhone 7", screen: 4.7, price: 9999, weight: 140 }
];

// 2. Оголошуємо змінні для задання меж ціни
let minPrice = 2000, maxPrice = 10000;

// 3. Оголошуємо порожній масив для збереження результатів
let result = [];

// 4. Організовуємо перебір елементів за допомогою спрощеного циклу for...of
for (let product of products) {
    // Перевіряємо умову: чи входить ціна товару в задані межі
    if (product.price >= minPrice && product.price <= maxPrice) {
        result.push(product); // Додаємо знайдений об'єкт у масив результатів
    }
}

// 5. Виводимо результати у консоль
console.log("Відфільтровані товари (від 2000 до 10000 грн):");
console.log(result);