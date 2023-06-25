const formulario = document.getElementById("formAgregarproducto");


formulario.addEventListener('submit', function(evento) {
    evento.preventDefault();

    if (document.getElementById("txtSku").value.length == 0) {
        alert("Debe ingresar el SKU del producto.");
    } else if (document.getElementById("txtNombre").value.length == 0) {
        alert("Debe ingresar el nombre del producto.");
    } else if (document.getElementById("txtPrecio").value.length == 0) {
        alert("Debe ingresar el precio del producto.");
    } else if (document.getElementById("txtImagen").value.length == 0) {
        alert("Debe ingresar una imagen al producto.");
    } else if (document.getElementById("txtDescripcion").value.length == 0) {
        alert("Debe ingresar una descripción al producto.");
    } else if (document.getElementById("txtStock").value.length == 0) {
        alert("Debe ingresar el stock del producto.");
    } else {
        this.submit();
    }
});
