import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar la solicitud de IA
@app.route('/IA', methods=['POST'])
def IA():
    data = request.get_json()
    texto = data["Mensaje"].lower


    if "fiebre" in texto:
        respuesta =  {
            "causas": "Gripe o infección",
            "info": "La fiebre es una respuesta del cuerpo a infecciones",
            "recomendaciones": "Descansa e hidrátate",
            "nivel": "Consulta médico si empeora"
        }
    elif "dolor de cabeza" in texto:
        respuesta =   {
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



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    