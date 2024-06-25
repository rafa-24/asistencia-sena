from flask import Flask, request, jsonify
from main import connect_database
from consultas import create_tables, create_relationships

app = Flask(__name__)
conn = connect_database()
create_tables(conn)
create_relationships(conn)

# Ruta de prueba
@app.route('/')
def home():
    return "¡Hola, Mundo!"

# Ruta GET
@app.route('/api/get', methods=['GET'])
def get_example():
    data = {
        "message": "Esta es una respuesta GET",
        "status": "success"
    }
    return jsonify(data)

# Ruta POST
@app.route('/api/post', methods=['POST'])
def post_example():
    # Obtener datos del cuerpo de la solicitud POST
    data = request.get_json()
    response = {
        "message": "Esta es una respuesta POST",
        "received_data": data,
        "status": "success"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)