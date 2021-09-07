from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin":"*"}})

lista = []

@app.route('/')
def index():
    return '<h1>El servidor está corriendo!</h1>'

@app.route('/estudiantes')
def metodoEstudiantes():
    return '<h1>Metodo de estudiantes</h1>'

if __name__ == '__main__':
    app.run(threaded = True,port = 3000, debug = True)