// Функція для Підзавдання 1
function greetUser() {
    let name = document.getElementById("userName").value;
    alert("Вітаю, " + name + "!");
}

// Функція для Підзавдання 2
function showInput() {
    let text = document.getElementById("inputField").value;
    console.log("Ви ввели: " + text);
}

// Функція для Підзавдання 3
function handleSubmit(event) {
    // Зупиняємо стандартну поведінку форми (щоб сторінка не перезавантажувалась)
    event.preventDefault(); 
    let value = document.getElementById("dataInput").value;
    alert("Введено: " + value);
}