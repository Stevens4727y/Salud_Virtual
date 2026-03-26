from flask import Flask, render_template

app = Flask(__name__)

# Definición de las tablas
diagrama = {

    "SolicitudCompra":
    [
        "numero_solicitud (PK)",
        "fecha",
        "estado",
        "id_contacto (FK)"
    ],

    "ItemsSolicitud":[
        "id_item_solicitud (PK)",
        "numero_solicitud (FK)",
        "codigo_siem",
        "cantidad"
    ],

    "OrdenContractual":[
        "numero_orden (PK)",
        "numero_solicitud (FK)",
        "rut_proveedor",
        "fecha_orden",
        "fecha_entrega",
        "monto_total"
    ],

    "ItemOrden":
    [
        "id_item_orden (PK)",
        "numero_orden (FK)",
        "codigo_siem",
        "cantidad"
    ],
        "EntradasAlmacen":
        [
            "numero_entrada (PK)",
            "numero_orden (FK)",
            "rut_responsable"
        ]
 }


@app.route("/")
def home():
    return render_template("index.html", tables=diagrama)

if __name__ == "__main__":
    app.run(debug=True)