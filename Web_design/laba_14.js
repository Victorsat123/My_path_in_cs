// 1. Звичайне спливаюче вікно
function showMessage() {
    alert("Це спливаюче вікно.");
}

// 2. Відкриття нового вікна 
function openNewWindow() {
    window.open("https://www.google.com", "_blank", "width=400,height=300");
}

// 3. Вікно з кнопками OK і Cancel 
function confirmMessage() {
    let result = confirm("Ви впевнені?");
    if (result) {
        alert("OK.");
    } else {
        alert("Cancel.");
    }
}

// 4. Вікно із полем для введення тексту
function promptMessage() {
    let name = prompt("Як вас звати?");
    if (name !== null && name !== "") { 
        alert("Вітаю, " + name + "!");
    }
}