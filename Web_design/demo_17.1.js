function toggleDescription() {
    // Знаходимо блок за його ID
    let description = document.getElementById("productDescription");
    
    // Перевіряємо поточний стан: якщо він прихований ("none"), то показуємо ("block")
    if (description.style.display === "none") {
        description.style.display = "block";
    } else {
        // Якщо ж він уже видимий, то ховаємо ("none")
        description.style.display = "none";
    }
}