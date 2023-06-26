let btnCarrito = document.getElementById("btnCarrito");

btnCarrito.addEventListener('click', function(){
    arrayProducto = [
        {
            sku:11000,
            nombre:"Regadera metalica",
            precio:14990,
            cantidad:2
        },
        {
            sku:12000,
            nombre:"Macetero de barro",
            precio:11990,
            cantidad:5
        },
        {
            sku:13000,
            nombre:"Set de riego con acople",
            precio:10490,
            cantidad:3
        },
        {
            sku:14000,
            nombre:"Set 3 herramietas",
            precio:13990,
            cantidad:1
        },
        {
            sku:15000,
            nombre:"Macetero cuadrado",
            precio:4990,
            cantidad:4
        },
        {
            sku:15000,
            nombre:"Tijeras de pasto",
            precio:12990,
            cantidad:2
        },
        {
            sku:16000,
            nombre:"Planta natural",
            precio:9990,
            cantidad:10
        },
        {
            sku:17000,
            nombre:"Regadera de jardineria",
            precio:7990,
            cantidad:5
        },
    ]

    

    let token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    fetch('/carrito',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':token
        },
        body:JSON.stringify(arrayProducto)
    })

})