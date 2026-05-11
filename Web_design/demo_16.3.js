// 1. Створюємо об'єкт person з властивостями та методами
let person = {
    'name': '',
    'lastName': '',
    
    // Метод, який просто виводить текст у консоль
    'sayHello': function(otherName) {
        console.log("Привіт, " + otherName + "! Мене звуть " + this.name);
    },
    
    // Метод, який ПОВЕРТАЄ склеєне ім'я та прізвище (але не виводить його)
    'getFullName': function() {
        return this.name + ' ' + this.lastName;
    }
};

// 2. Ініціалізуємо об'єкт твоїми власними даними
person.name = "Віктор";
person.lastName = "Сатановський";

console.log("--- Виклик методу sayHello ---");
person.sayHello("Орест");

console.log("\n--- Виклик методу getFullName ---");
console.log("Повне ім'я: " + person.getFullName());