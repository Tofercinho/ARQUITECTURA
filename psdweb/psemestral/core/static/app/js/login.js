$(document).ready(function () {
    console.log("funcionando el jquery");
});


document.getElementById("btn_registrarse").addEventListener("click", register);
document.getElementById("btn_iniciar_sesion").addEventListener("click", IniciarSesion);
window.addEventListener("resize", anchopagina);


var contenedor_login_register = document.querySelector(".contenedor_login_register")
var formulario_login = document.querySelector(".formulario_login");
var formulario_register = document.querySelector(".formulario_register");
var detras_login = document.querySelector(".detras_login");
var detras_registro = document.querySelector(".detras_registro");


function anchopagina() {
    if (window.innerWidth > 850) {
        detras_login.style.display = "block";
        detras_registro.style.display = "block";
    } else {
        detras_registro.style.display = "block";
        detras_registro.style.opacity = "1";
        detras_login.style.display= "none";
        formulario_login.style.display="block";
        formulario_register.style.display="none";
        contenedor_login_register.style.left="0px";
    }
}

anchopagina();


function IniciarSesion() {
    if (window.innerWidth > 850) {
        formulario_register.style.display = "none";
        contenedor_login_register.style.left = "10px";
        formulario_login.style.display = "block";
        detras_registro.style.opacity = "1";
        detras_login.style.opacity = "0";
    } else {
        formulario_register.style.display = "none";
        contenedor_login_register.style.left = "0px";
        formulario_login.style.display = "block";
        detras_registro.style.display = "block";
        detras_login.style.display = "none";
    }
}
function register() {

    if (window.innerWidth > 850) {
        formulario_register.style.display = "block";
        contenedor_login_register.style.left = "410px";
        formulario_login.style.display = "none";
        detras_registro.style.opacity = "0";
        detras_login.style.opacity = "1";
    } else {
        formulario_register.style.display = "block";
        contenedor_login_register.style.left = "0px";
        formulario_login.style.display = "none";
        detras_registro.style.display = "none";
        detras_login.style.display = "block";
        detras_login.style.opacity = "1";
    }
}
