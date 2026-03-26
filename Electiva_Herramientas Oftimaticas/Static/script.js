function enviar() {
    let mensaje = document.getElementById("mensaje").value;

    fetch("/ia", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ mensaje: mensaje })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("respuesta").innerHTML = `
            <p><b>Posibles causas:</b> ${data.causas}</p>
            <p><b>Información:</b> ${data.info}</p>
            <p><b>Recomendaciones:</b> ${data.recomendaciones}</p>
            <p><b>Nivel:</b> ${data.nivel}</p>
        `;
    });
}