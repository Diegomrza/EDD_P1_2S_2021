from Estructuras.Nodos.NodoAVL import NodoAVL
from Estructuras.Nodos.NodoTarea import NodoTarea

from flask import Flask, request, jsonify
from flask_cors import CORS
from Analizadores.sintactico import parser, objetos

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin":"*"}})
ob = NodoAVL(0,'','','','','',0,0)
obj = NodoTarea(0,'','','','',0,'')
lista = []

#Para usar Arbol AVL: arbol.root = arbol.insertar(arbol.root, nuevo)

@app.route('/')
def index():
    return '<h1>El servidor está corriendo!</h1>'

@app.route('/estudiantes')
def metodoEstudiantes():
    return '<h1>Metodo de estudiantes</h1>'

@app.route('/Pruebas',methods=['GET','POST'])
def prueba():
    return '<h1><img src="https://upload.wikimedia.org/wikipedia/commons/4/4a/Usac_logo.png"></h1>'

@app.route('/ply',methods=['POST'])
def ply():
    ruta = r'C:\Users\Squery\Documents\GitHub\EDD_SmartClass_-201901429'
    ruta += "\\" + request.json['ruta']
    archivo = open(ruta, "r", encoding='utf-8')
    contenido = archivo.read()
    parser.parse(contenido)

    print(len(objetos))
    for x in objetos:
        if type(x) == type(ob):
            print(vars(x))
            '''print("J: ",x.carnet)
            print("J: ",x.dpi)
            print("J: ",x.nombre)
            print("J: ",x.carrera)
            print("J: ",x.correo)
            print("J: ",x.password)
            print("J: ",x.creditos)
            print("J: ",x.edad)'''
            print('\n')
        elif type(x) == type(obj):
            print(vars(x))
            '''print('K: ', x.carnet)
            print('K: ', x.nombre)
            print('K: ', x.descripcion)
            print('K: ', x.materia)
            print('K: ', x.fecha)
            print('K: ', x.hora)
            print('K: ', x.estado)'''
            print('\n')
    archivo.close()
    return jsonify({
        'Contenido': contenido
        }) 

if __name__ == '__main__':
    app.run(threaded = True,port = 3000, debug = True)