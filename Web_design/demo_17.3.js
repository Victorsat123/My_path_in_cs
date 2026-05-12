// 1. Функція, яка спрацьовує ПРИ ЗАВАНТАЖЕННІ сторінки
window.onload = function() {
    let description = document.getElementById("productDescription");
    let state = localStorage.getItem("descriptionState");
    
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
        localStorage.setItem("descriptionState", "open"); 
    } else {
        // Якщо блок був видимий
        description.style.display = "none"; // Ховаємо його
        localStorage.setItem("descriptionState", "closed");
    }
}