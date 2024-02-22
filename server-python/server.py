from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

@app.route('/check')
def check():
    return jsonify({'Estado': 'Check endpoint status: OK!!'})

@app.route('/')
def index():
    return jsonify({
        'Instancia': 'Instancia #2 - API #2',
        'Curso': 'Seminario de Sistemas 1',
        'Estudiante': 'Henrry David Bran Velasquez - 201314439'
    })

if __name__ == '__main__':
    # Ejecuta la aplicación en la dirección IP pública de la instancia EC2 y el puerto 3000
    app.run(debug=True, host='0.0.0.0', port=3000)
