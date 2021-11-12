from datetime import time
from flask import Flask, request, jsonify
from flask_cors import CORS
import time, threading

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return '<h1>En linea!<h1/>'

def consultar():
    contador = 0
    while True:
        time.sleep(3.0)
        contador = crear(contador)

def crear(c):
    print('Contador: ',c)
    archivo = open(r'C:\Users\Squery\Desktop\Reportes_F3\archivo'+str(c)+'.txt', 'w')
    archivo.write('Nuevo Archivo' + str(c))
    archivo.close()
    return c+1

t1 = threading.Thread(target=consultar)

t1.start()

if __name__ == '__main__':
    app.run(threaded = True,port = 3000, debug = True)