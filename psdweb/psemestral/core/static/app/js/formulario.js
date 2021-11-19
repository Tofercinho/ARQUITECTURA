const formulario_l = document.getElementById('login');
const input_l = document.querySelectorAll('#login input');

const formulario_r = document.getElementById('registro');
const input_r = document.querySelectorAll('#registro input');

const formulario_c = document.getElementById('formulario_contacto');
const input_c = document.querySelectorAll('#formulario_contacto input');

const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar tildes.
	password: /^.{4,12}$/, // 4 a 12 digitos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{7,14}$/ // 7 a 14 numeros.
}

const validarFormulario_c = (e) => {
    switch (e.target.name) {
        case "nombre_contacto":
            console.log('nombre funciona');
            if (expresiones.nombre.test(e.target.value)) {
                document.getElementById('nombre_contacto').classList.remove('my-campo-incorrecto');
                document.querySelector('#error_nombre_c').classList.remove('error_nombre_c-activo');
            }
            else {
                document.getElementById('nombre_contacto').classList.add('my-campo-incorrecto');
                document.querySelector('#error_nombre_c').classList.add('error_nombre_c-activo');
            };
        break;

        case "email_contacto":
            console.log('correo funciona');
            if (expresiones.correo.test(e.target.value)) {
                document.getElementById('email_contacto').classList.remove('my-campo-incorrecto');
                document.querySelector('#error_email_c').classList.remove('error_email_c-activo');
            }
            else {
                document.getElementById('email_contacto').classList.add('my-campo-incorrecto');
                document.querySelector('#error_email_c').classList.add('error_email_c-activo');
            };
        break;
    };
};

const validarFormulario_l = (e) => {
    switch (e.target.name) {
        case "email_login":
            if (expresiones.correo.test(e.target.value)) {
                document.getElementById('email_login').classList.remove('my-campo-incorrecto');
                document.querySelector('#error_email_l').classList.remove('error_email_l-activo');
            }
            else {
                document.getElementById('email_login').classList.add('my-campo-incorrecto');
                document.querySelector('#error_email_l').classList.add('error_email_l-activo');
            };
        break;
    };
};

const validarFormulario_r = (e) => {
    switch (e.target.name) {
        case "nombre_registro":
            if (expresiones.nombre.test(e.target.value)) {
                document.getElementById('nombre_registro').classList.remove('my-campo-incorrecto');
                document.querySelector('#error_nombre_r').classList.remove('error_nombre_r-activo');
            }
            else {
                document.getElementById('nombre_registro').classList.add('my-campo-incorrecto');
                document.querySelector('#error_nombre_r').classList.add('error_nombre_r-activo');
            };
        break;

        case "apellido_registro":
            if (expresiones.nombre.test(e.target.value)) {
                document.getElementById('apellido_registro').classList.remove('my-campo-incorrecto');
                document.querySelector('#error_apellido_r').classList.remove('error_apellido_r-activo');
            }
            else {
                document.getElementById('apellido_registro').classList.add('my-campo-incorrecto');
                document.querySelector('#error_apellido_r').classList.add('error_apellido_r-activo');
            };
        break;

        case "email_registro":
            if (expresiones.correo.test(e.target.value)) {
                document.getElementById('email_registro').classList.remove('my-campo-incorrecto');
                document.querySelector('#error_email_r').classList.remove('error_email_r-activo');
            }
            else {
                document.getElementById('email_registro').classList.add('my-campo-incorrecto');
                document.querySelector('#error_email_r').classList.add('error_email_r-activo');
            };
        break;

        case "pass_registro":
            if (expresiones.password.test(e.target.value)) {
                document.getElementById('pass_registro').classList.remove('my-campo-incorrecto');
            }
            else {
                document.getElementById('pass_registro').classList.add('my-campo-incorrecto');
            };
        break;

        case "pass_registro2":
            if (expresiones.password.test(e.target.value)) {
                document.getElementById('pass_registro2').classList.remove('my-campo-incorrecto');
            }
            else {
                document.getElementById('pass_registro2').classList.add('my-campo-incorrecto');
            };
        break;
    };
};

input_l.forEach((input) => {
    input.addEventListener('keyup', validarFormulario_l);
    input.addEventListener('blur', validarFormulario_l);
});

formulario_l.addEventListener('submit', (e) => {
    e.preventDefault();
});

formulario_r.addEventListener('submit', (e) => {
    e.preventDefault();
});

input_r.forEach((input) => {
    input.addEventListener('keyup', validarFormulario_r);
    input.addEventListener('blur', validarFormulario_r);
});

formulario_c.addEventListener('submit', (e) => {
    e.preventDefault();
});

input_c.forEach((input) => {
    input.addEventListener('keyup', validarFormulario_c);
    input.addEventListener('blur', validarFormulario_c);
});