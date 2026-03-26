import os
from flask import Flask, render_template, request, jsonify

Salud_Virtual = Flask(__name__)
@Salud_Virtual.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar la solicitud de IA
@Salud_Virtual.route('/IA', methods=['POST'])
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
    Salud_Virtual.run(host="0.0.0.0", port=port)
    