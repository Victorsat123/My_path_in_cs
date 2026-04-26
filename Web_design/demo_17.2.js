function toggleDescription() {
    let description = document.getElementById("productDescription");

    // Якщо блок прихований — показуємо і анімуємо
    if (description.style.display === "none") {
        description.style.display = "block";
        
        let pos = 0; // Початкова позиція
        
        // Запускаємо таймер (анімацію)
        let id = setInterval(function() {
            // Експериментальне значення: зупиняємось на 100 пікселях (замість 200)
            if (pos >= 100) {
                clearInterval(id); // Зупиняємо таймер, коли досягли межі
            } else {
                pos++;
                // Рухаємо блок вправо, додаючи пікселі до margin-left
                description.style.marginLeft = pos + "px"; 
            }
        }, 2); // Експериментальне значення: швидкість 2 мілісекунди (швидше і плавніше)
        
    } else {
        // Якщо блок видимий — ховаємо його і скидаємо відступ
        description.style.display = "none";
        description.style.marginLeft = "0px";
    }
}