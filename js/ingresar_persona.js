function guardar() {
    let nombre_ingresado = document.getElementById("nombre").value

    console.log(nombre_ingresado );

    let enviar_nombre = {
        nombre: nombre_ingresado,
        
    }
    console.log(enviar_nombre);
    
    let url = "http://localhost:5000/registro"
    var options = {
        body: JSON.stringify(enviar_nombre),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
            // Devuelve el href (URL) de la página actual
            window.location.href = "./personas.html";  
            
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}