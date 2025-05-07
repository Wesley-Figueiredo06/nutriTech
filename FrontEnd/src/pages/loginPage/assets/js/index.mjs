

const form = document.getElementById("form");
const userInput = document.getElementById("userInput");
const passwordInput = document.getElementById("passwordInput");
const btnSubmit = document.getElementById("btnSubmit");


form.addEventListener("submit", (e) => {
    e.preventDefault();

    if (userInput.value === "1" && passwordInput.value === "1") {
        form.submit(alert("Login efetuado!"));
    } else {
        alert("usuario e senha errados!")
    }
});


