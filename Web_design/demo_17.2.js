function toggleDescription() {
    let description = document.getElementById("productDescription");

    // Якщо блок прихований — показуємо і анімуємо
    if (description.style.display === "none") {
        description.style.display = "block";
        
        let pos = 0; 
        
        // Запускаємо таймер (анімацію)
        let id = setInterval(function() {
            if (pos >= 100) {
                clearInterval(id); 
            } else {
                pos++;
                description.style.marginLeft = pos + "px"; 
            }
        }, 2); 
        
    } else {
        // Якщо блок видимий — ховаємо його і скидаємо відступ
        description.style.display = "none";
        description.style.marginLeft = "0px";
    }
}