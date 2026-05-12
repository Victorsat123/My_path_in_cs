function toggleDescription() {
    // Знаходимо блок за його ID
    let description = document.getElementById("productDescription");
    
    if (description.style.display === "none") {
        description.style.display = "block";
    } else {
        description.style.display = "none";
    }
}