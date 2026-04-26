// 1. Створюємо об'єкт person з властивостями та методами
let person = {
    'name': '',
    'lastName': '',
    
    // Метод, який просто виводить текст у консоль
    'sayHello': function(otherName) {
        // this.name вказує на властивість name САМЕ ЦЬОГО об'єкта
        console.log("Привіт, " + otherName + "! Мене звуть " + this.name);
    },
    
    // Метод, який ПОВЕРТАЄ склеєне ім'я та прізвище (але не виводить його)
    'getFullName': function() {
        return this.name + ' ' + this.lastName;
    }
};

// 2. Ініціалізуємо об'єкт твоїми власними даними
person.name = "Віктор";
person.lastName = "Шевченко";

console.log("--- Виклик методу sayHello ---");
// Викликаємо метод привітання (передаємо ім'я співрозмовника)
person.sayHello("Марія");

console.log("\n--- Виклик методу getFullName ---");
// Оскільки метод getFullName лише повертає рядок, нам потрібно 
// самостійно обгорнути його в console.log(), щоб побачити результат
console.log("Повне ім'я: " + person.getFullName());