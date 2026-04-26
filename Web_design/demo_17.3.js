// 1. Функція, яка спрацьовує ПРИ ЗАВАНТАЖЕННІ сторінки
window.onload = function() {
    let description = document.getElementById("productDescription");
    // Зчитуємо збережений стан з пам'яті браузера
    let state = localStorage.getItem("descriptionState");
    
    // Перевіряємо, що було збережено минулого разу
    if (state === "open") {
        description.style.display = "block";
    } else {
        description.style.display = "none";
    }
}

// 2. Функція, яка спрацьовує ПРИ НАТИСКАННІ на кнопку
function toggleDescription() {
    let description = document.getElementById("productDescription");
    
    // Якщо блок був прихований
    if (description.style.display === "none") {
        description.style.display = "block"; // Показуємо його
        // Зберігаємо в LocalStorage інформацію, що він "відкритий"
        localStorage.setItem("descriptionState", "open"); 
    } else {
        // Якщо блок був видимий
        description.style.display = "none"; // Ховаємо його
        // Зберігаємо в LocalStorage інформацію, що він "закритий"
        localStorage.setItem("descriptionState", "closed");
    }
}