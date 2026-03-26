from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Ruta principal
@app.route("/")
def home():
    return render_template("index.html")

# Ruta de IA (simulada)
@app.route("/ia", methods=["POST"])
def ia():
    data = request.json
    texto = data["mensaje"].lower()

    if "fiebre" in texto:
        respuesta = {
            "causas": "Gripe o infección",
            "info": "La fiebre es una respuesta del cuerpo a infecciones",
            "recomendaciones": "Descansa e hidrátate",
            "nivel": "Consulta médico si empeora"
        }
    elif "dolor cabeza" in texto:
        respuesta = {
            "causas": "Estrés o migraña",
            "info": "El dolor de cabeza puede ser causado por tensión",
            "recomendaciones": "Descansa y evita pantallas",
            "nivel": "Consulta si es frecuente"
        }
    else:
        respuesta = {
            "causas": "Varias posibles",
            "info": "No se puede determinar con exactitud",
            "recomendaciones": "Observa síntomas",
            "nivel": "Consulta médico si persiste"
        }

    return jsonify(respuesta)


# 👇 IMPORTANTE: acceso externo
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)