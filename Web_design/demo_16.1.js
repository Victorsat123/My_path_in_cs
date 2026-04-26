// 1. Створюємо масив об'єктів (міста для подорожей)
let trips = [
    { city: "Київ", duration: 2, price: 2000, food: false, guide: true },
    { city: "Харків", duration: 1, price: 3000, food: false, guide: false },
    { city: "Одеса", duration: 2, price: 6000, food: true, guide: true },
    { city: "Дніпро", duration: 1, price: 4500, food: false, guide: true },
    { city: "Полтава", duration: 1, price: 2000, food: false, guide: false }
];

// 2. Вибірка 1: одноденні подорожі без харчування
let oneDayNoFood = [];
for (let trip of trips) {
    if (trip.duration === 1 && trip.food === false) {
        oneDayNoFood.push(trip);
    }
}

// 3. Вибірка 2: подорожі не дорожчі за 3000
let cheapTrips = [];
for (let trip of trips) {
    if (trip.price <= 3000) {
        cheapTrips.push(trip);
    }
}

// 4. Виводимо результати у консоль
console.log("1) Одноденні подорожі без харчування:");
console.log(oneDayNoFood);

console.log("2) Подорожі не дорожчі на 3000:");
console.log(cheapTrips);