function validar_form_registrar_usuario(){
    var usuario = document.getElementById("usuario");
    var correo = document.getElementById("email");
    var clave = document.getElementById("password");

    var usuario_len = usuario.value.length;
    if(usuario_len == 0 || usuario_len < 8)
    {
        alert("Debes ingresar un usuario con mínimo 8 caracteres");
        usuario.focus();
        return false;
    }

    var formatoCorreo = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if(!correo.value.match(formatoCorreo))
    {
        alert("Debes ingresar un correo electronico valido!");
        correo.focus();
        return false;
    }

    var passid_len = clave.value.length;
    if (passid_len == 0 || passid_len < 8)
    {
        alert("Debes ingresar una clave con mas de 8 caracteres");
        clave.focus();
        return false;
    }
}

function validar_form_login(){
    var usuario = document.getElementById("usuario");
    var clave = document.getElementById("clave");

    var usuario_len = usuario.value.length;
    if(usuario_len == 0 || usuario_len < 8)
    {
        alert("Debes ingresar un usuario con mínimo 8 caracteres");
        usuario.focus();
        return false;
    }

    var passid_len = clave.value.length;
    if (passid_len == 0 || passid_len < 8)
    {
        alert("Debes ingresar una clave con mas de 8 caracteres");
        clave.focus();
        return false;
    }
}

function mostrarPassword() {
    var obj = document.getElementById('password');
    obj.type = "text";
}

function ocultarPassword() {
    var obj = document.getElementById('password');
    obj.type = "password";
}