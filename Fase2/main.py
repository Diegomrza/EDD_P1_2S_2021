#Importaciones nodos estructuras
from Estructuras.Nodos.NodoMeses import NodoMeses
from Estructuras.Nodos.NodoAnios import NodoAnios
from Estructuras.Nodos.NodoAVL import NodoAVL
from Estructuras.Nodos.NodoCursos import NodoCurso
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

estudiantes = ArbolAVL() #Arbol AVL de estudiantes
pensum = ArbolCursos(5) #Arbol B de cursos

@app.route('/')
def index():
    return '<h1>El servidor está corriendo!</h1>'

@app.route('/carga', methods=['POST'])
def carga():
    tipo = request.json['tipo']
    ruta = request.json['path']

    if tipo.lower() == 'estudiante':
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
    global estudiantes #Arbol AVL
    global pensum #Arbol B

    tipo = request.args.get('tipo','None')
    carnet = request.args.get('carnet','None')
    anio = request.args.get('anio','None')
    mes = request.args.get('mes','None')
    dia = request.args.get('dia','None')
    hora = request.args.get('hora','None')
    semestre = request.args.get('semestre','None')
    
    g = grafo()
    if int(tipo) == 0:
        g.grafoArbolAVL(estudiantes)
    elif int(tipo) == 1 and carnet != 'None' and anio != 'None' and mes != 'None': 
        estudiantes.mostrar_solo_un_nodo0(int(carnet), int(anio), int(mes))
    elif int(tipo) == 2 and carnet != 'None' and anio != 'None' and mes != 'None' and dia != 'None' and hora != 'None':
        estudiantes.mostrar_tareas0(int(carnet), int(anio), int(mes), int(dia), int(hora))
    elif int(tipo) == 3:
        g.arbolB_cursosGeneral(pensum)
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
    global estudiantes

    if request.method == 'GET': #Mostrar un estudiante
        carnet = int(request.json['carnet'])
        estudiantes.mostrar_estudiante0(carnet)

        return jsonify({
            'Método':'get'
        })
    elif request.method == 'POST': #Crear un estudiante
        carnet = int(request.json['carnet'])
        dpi = request.json['dpi']
        nombre = request.json['nombre']
        carrera = request.json['carrera']
        correo = request.json['correo']
        password = request.json['password']
        creditos = int(request.json['creditos'])
        edad = int(request.json['edad'])
        nuevo = NodoAVL(carnet, dpi, nombre, carrera, correo, password, creditos, edad)
        estudiantes.insertar0(nuevo)

        return jsonify({
            'message':'post'
        })
    elif request.method == 'PUT': #Cambiar un estudiante
        carnet = int(request.json['carnet'])
        dpi = request.json['dpi']
        nombre = request.json['nombre']
        carrera = request.json['carrera']
        correo = request.json['correo']
        password = request.json['password']
        creditos = int(request.json['creditos'])
        edad = int(request.json['edad'])
        arr = [carnet, dpi, nombre, carrera, correo, password, creditos, edad]
        estudiantes.modificar0(arr)

        return jsonify({
            'message':'put'
        })
    elif request.method == 'DELETE': #Eliminar un estudiante
        carnet = int(request.json['carnet'])
        estudiantes.eliminar0(carnet)
        return({
            'message':'delete'
        })

@app.route('/recordatorios', methods=['GET','POST','PUT','DELETE'])
def recordatorios():
    global estudiantes

    if request.method == 'GET':
        return jsonify({
            'message':'get'
        })
    elif request.method == 'POST':
        carnet = request.json['Carnet']
        nombre = request.json['Nombre']
        descripcion = request.json['Descripcion']
        materia = request.json['Materia'] 
        fecha = request.json['Fecha'].split('/') #split
        hora = request.json['Hora'] 
        estado = request.json['Estado']

        datos = [nombre, descripcion, materia, estado]

        estudiantes.get_(estudiantes.root, int(carnet), int(fecha[2]), int(fecha[1]), int(fecha[0]), int(hora), datos)

        return jsonify({
            'message':'post'
        })
    elif request.method == 'PUT':
        return jsonify({
            'message':'put'
        })
    elif request.method == 'DELETE':
        return({
            'message':'delete'
        })

@app.route('/cursosEstudiante', methods=['POST'])
def cursosEstudiante():
    return jsonify({

    })

@app.route('/cursosPensum', methods=['POST'])
def cursosPensum():
    global pensum

    cursos = request.json['Cursos']
    for x in cursos:
        codigo = int(x['Codigo'])
        nombre = x['Nombre']
        prerrequisito = ['Prerequisitos']
        tipo = x['Obligatorio']
        pensum.insertar(codigo, nombre, prerrequisito, tipo)
    return jsonify({
        "message":"Success"
    })   

@app.route('/ply',methods=['POST'])
def ply(ru):
    global estudiantes

    ruta = r'C:\Users\Squery\Documents\GitHub\EDD_SmartClass_201901429'
    ruta += "\\" + ru #request.json['ruta']
    archivo = open(ruta, "r", encoding='utf-8')
    contenido = archivo.read()
    parser.parse(contenido)

    lista_users = []
    lista_task = []

    for x in objetos:
        if type(x) == type(ob):  #Tipo user
            #print('Usuario: ',vars(x))
            lista_users.append(x)
        elif type(x) == type(obj): #Tipo task
            #print('Task: ',vars(x))
            lista_task.append(x)

    for y in lista_users:
        nuevo = y
        carnet = (y.carnet.rstrip('"')).lstrip('"')
        dpi = (y.dpi.rstrip('"')).lstrip('"')
        nombre = (y.nombre.rstrip('"')).lstrip('"')
        carrera = (y.carrera.rstrip('"')).lstrip('"')
        correo = (y.correo.rstrip('"')).lstrip('"')
        password = (y.password.rstrip('"')).lstrip('"')

        nuevo.carnet = int(carnet)
        nuevo.nombre = nombre
        nuevo.carrera = carrera
        nuevo.dpi = dpi
        nuevo.correo = correo
        nuevo.password = password
        print('Usuario: ',vars(nuevo))
        estudiantes.insertar0(nuevo)

    archivo.close()
    return jsonify({
        'Contenido': contenido
        }) 

if __name__ == '__main__':
    app.run(threaded = True,port = 3000, debug = True)