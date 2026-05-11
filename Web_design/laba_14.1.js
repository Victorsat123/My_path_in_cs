function greetUser() {
    let name = document.getElementById("userName").value;
    alert("Вітаю, " + name + "!");
}

function showInput() {
    let text = document.getElementById("inputField").value;
    console.log("Ви ввели: " + text);
}

function handleSubmit(event) {
    event.preventDefault(); 
    let value = document.getElementById("dataInput").value;
    alert("Введено: " + value);
}