#Importaciones nodos estructuras
import re
from Estructuras.Nodos.NodoMeses import NodoMeses
from Estructuras.Nodos.NodoAnios import NodoAnios
from Estructuras.Nodos.NodoAVL import NodoAVL
from Estructuras.Nodos.NodoCursos import NodoCursos
from Estructuras.Nodos.NodoDispersa import NodoDispersa
from Estructuras.Nodos.NodoTarea import NodoTarea

#Importaciones estructuras
from Estructuras.ArbolAVL import ArbolAVL
from Estructuras.ArbolCursos import ArbolCursos
from Estructuras.Dispersa import Dispersa
from Estructuras.ListaAnios import ListaAnios
from Estructuras.ListaMeses import ListaMeses
from Estructuras.ListaSemestres import ListaSemestres
from Estructuras.ListaTareas import ListaTareas
from Estructuras.grafo import grafo

#importaciones flask
from flask import Flask, request, jsonify
from flask_cors import CORS
from Analizadores.sintactico import parser, objetos

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin":"*"}})

ob = NodoAVL(0,'','','','','',0,0)
obj = NodoTarea(0,'','','','',0,'')
estudiantes = ArbolAVL()
#lista = []

#Para usar Arbol AVL: arbol.root = arbol.insertar(arbol.root, nuevo)

@app.route('/')
def index():
    return '<h1>El servidor está corriendo!</h1>'

@app.route('/carga', methods=['POST'])
def carga():
    tipo = request.json['tipo']
    ruta = request.json['path']

    if tipo.lower() == 'estudiante':
        #print('Tipo estudiante: ',end='') print(tipo + ' - ' + ruta)
        ply(ruta)
    elif tipo.lower() == 'recordatorio':
        print('Tipo recordatorio: ',end='')
        print(tipo + ' - ' + ruta)
    elif tipo.lower() == 'curso':
        print('Tipo curso: ',end='')
        print(tipo + ' - ' + ruta)
    else:
        #Si la petición no cumple
        return jsonify({
            'message':'Parámetros inválidos, ingrese los parámetros de manera correcta'
        })
    #Si la petición fue correcta
    return jsonify({
        'message' : 'Success'
    })

@app.route('/reporte', methods=['GET'])
def reporte():
    tipo = request.args.get('tipo','None')
    carnet = request.args.get('carnet','None')
    anio = request.args.get('anio','None')
    mes = request.args.get('mes','None')
    dia = request.args.get('dia','None')
    hora = request.args.get('hora','None')
    semestre = request.args.get('semestre','None')
    
    if int(tipo) == 0:
        arbol = ArbolAVL()
        g = grafo()
        for x in range(10):
            print(x)
            nodo = NodoAVL(10+x,'2993323220101','Diego Robles'+str(x),'Sistemas','diego@gmail.com','123',85,23)
            nodoAnio = NodoAnios(2021)
            nodoMes = NodoMeses(6)
            for i in range(10):
                for j in range(10):
                    nodoMes.actividades.insertar(i,j,'Hi')

            #g.matrizDispersa(nodoMes.actividades)
            nodoAnio.meses.insertar(nodoMes)
            nodo.lista_anios.insertar(nodoAnio)
            arbol.insertar0(nodo)
        
        g.grafoArbolAVL(arbol)
    elif int(tipo) == 1 and carnet != 'None' and anio != 'None' and mes != 'None': 
        print('Tipo 1: ',end='')
        print(carnet, anio, mes)
    elif int(tipo) == 2 and carnet != 'None' and anio != 'None' and mes != 'None' and dia != 'None' and hora != 'None':
        print('Tipo 2: ',end='')
        print(carnet, anio, mes, hora)
    elif int(tipo) == 3:
        print('Tipo 3: ')
        arbolB = ArbolCursos(5)
        for x in range(21):
            nuevo = NodoCursos(5)
            nuevo.codigo_curso = 5+x
            nuevo.codigos_prerrequisito == 10+x
            nuevo.creditos = 50+x
            nuevo.nombre = 'Nombre Curso'+str(x)
            arbolB.insertar(x)
        g = grafo()
        g.arbolB_cursosGeneral(arbolB)
    elif int(tipo) == 4 and carnet != 'None' and anio != 'None' and semestre != 'None':
        print('Tipo 4: ',end='')
        print(carnet, anio, semestre)
    else:
        return jsonify({
            'message':'No se ingresaron los parámetros indicados'
            })

    return jsonify({
        'message':'Success'
        })

@app.route('/estudiante', methods=['GET','POST','PUT','DELETE'])
def estudiante():
    if request.method == 'GET':
        return jsonify({
            'Método':'get'
        })
    elif request.method == 'POST':
        return jsonify({
            'Método':'post'
        })
    elif request.method == 'PUT':
        return jsonify({
            'Método':'put'
        })
    elif request.method == 'DELETE':
        return({
            'Método':'delete'
        })

@app.route('/recordatorios', methods=['GET','POST','PUT','DELETE'])
def recordatorios():
    if request.method == 'GET':
        return jsonify({
            'Método':'get'
        })
    elif request.method == 'POST':
        return jsonify({
            'Método':'post'
        })
    elif request.method == 'PUT':
        return jsonify({
            'Método':'put'
        })
    elif request.method == 'DELETE':
        return({
            'Método':'delete'
        })

@app.route('/cursosEstudiante', methods=['POST'])
def cursosEstudiante():
    return jsonify({

    })

@app.route('/cursosPensum', methods=['POST'])
def cursosPensum():
    return jsonify({
        
    })   


@app.route('/ply',methods=['POST'])
def ply(ru):
    global estudiantes

    ruta = r'C:\Users\Squery\Documents\GitHub\EDD_SmartClass_201901429'
    ruta += "\\" + ru #request.json['ruta']
    archivo = open(ruta, "r", encoding='utf-8')
    contenido = archivo.read()
    parser.parse(contenido)

    print(len(objetos))
    for x in objetos:
        if type(x) == type(ob):  #Tipo user
            #print(vars(x))
            estudiantes.insertar0(x)
        elif type(x) == type(obj): #Tipo task
            #print(vars(x))
            pass
    archivo.close()
    return jsonify({
        'Contenido': contenido
        }) 

if __name__ == '__main__':
    app.run(threaded = True,port = 3000, debug = True)