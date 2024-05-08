document.getElementById("ini-se-btn").addEventListener("click", function(event) {
    event.preventDefault(); // Impede o comportamento padrão do link (redirecionamento)
    document.getElementById("formularioRegistro").style.display = "block"; // Exibe o formulário
});