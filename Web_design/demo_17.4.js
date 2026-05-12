function toggleDescription(blockId, storageKey) {
    let description = document.getElementById(blockId);

    // Якщо блок прихований — показуємо, анімуємо і ЗБЕРІГАЄМО стан
    if (description.style.display === "none" || description.style.display === "") {
        description.style.display = "block";
        localStorage.setItem(storageKey, "open"); 
        let pos = 0; 
        
        let id = setInterval(function() {
            if (pos >= 100) {
                clearInterval(id); 
            } else {
                pos += 2; 
                description.style.marginLeft = pos + "px"; 
            }
        }, 2);
        
    } else {
        // Якщо блок видимий — ховаємо його, скидаємо відступ і ЗБЕРІГАЄМО стан
        description.style.display = "none";
        description.style.marginLeft = "0px";
        localStorage.setItem(storageKey, "closed"); 
    }
}

// Функція, яка спрацьовує при оновленні сторінки
window.onload = function() {
    const blocks = [
        { id: 'desc1', key: 'state1' },
        { id: 'desc2', key: 'state2' },
        { id: 'desc3', key: 'state3' }
    ];

    // Проходимось по кожному блоку
    blocks.forEach(function(block) {
        let state = localStorage.getItem(block.key);
        let description = document.getElementById(block.id);

        if (state === "open") {
            description.style.display = "block";
            description.style.marginLeft = "100px"; 
        } else {
            description.style.display = "none";
            description.style.marginLeft = "0px";
        }
    });
}