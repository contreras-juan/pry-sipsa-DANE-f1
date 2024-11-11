from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import sys
import os

sys.path.append('scripts/')

from Llm_Handler import SIPSA_Analyzer

app = Flask(__name__)
CORS(app)

# Inicializamos el procesador de PQRS con la clave API necesaria
# Cargar las variables del archivo .env
load_dotenv()

# Leer la llave de la API
api_key = os.getenv('OPENAI_API_KEY')
audio_path = 'input/audios'

sipsa = SIPSA_Analyzer(api_key)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message')
    response = sipsa.pandas_query_pipeline(user_input.upper())
    return jsonify({'response': response.message.content})

@app.route('/process_audio', methods=['POST'])
def endpoint_transcribe():
   if 'audio' not in request.files:
      return jsonify({"error": "No audio file provided"}), 400
      
   audio_file = request.files['audio']
   try:
      # save a temporary instance of the file to satisfy the API
      audio_file.seek(0)
      temp_path = "./temp_audio.webm"
      audio_file.save(temp_path)
      with open(temp_path, "rb") as file:
         sipsa.transcribe_audio_openai(file)
      # clean up
      os.remove(temp_path)
      return jsonify({'transcript': sipsa.transcription}) 

   
   except Exception as e:
      print(e)
      return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
    print("running up...")