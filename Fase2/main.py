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
#Creacion de carpeta Reportes
import os
import errno

try:
    os.mkdir(r'C:\Users\Squery\Desktop\Reportes_F2')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin":"*"}})

ob = NodoAVL(0,'','','','','',0,0)
obj = NodoTarea(0,'','','','',0,'')

estudiantes = ArbolAVL() #Arbol AVL de estudiantes
pensum = ArbolCursos(5) #Arbol B de cursos
g = grafo()

@app.route('/')
def index():
    return '<h1>El servidor está corriendo!</h1>'

@app.route('/carga', methods=['POST'])
def carga():
    tipo = request.json['tipo']
    ruta = request.json['path']

    if tipo.lower() == 'estudiante': #Aquí se analiza el archivo para usuarios y tareas
        ply(ruta)
    elif tipo.lower() == 'recordatorio': #Se supone no se usa aquí
        print('Tipo recordatorio: ',end='')
        print(tipo + ' - ' + ruta)
    elif tipo.lower() == 'curso': #Se supone no se usa aquí
        print('Tipo curso: ',end='')
        print(tipo + ' - ' + ruta)
    else:
        #Si la petición no cumple
        return jsonify({
            'message':'Parámetros inválidos, ingrese los parámetros de manera correcta'
        })
    #Si la petición fue correcta
    return jsonify({
        'message' : 'Archivo leído con exito'
    })

@app.route('/reporte', methods=['GET'])
def reporte():
    global estudiantes #Arbol AVL
    global pensum #Arbol B
    global g

    #Obteniendo todos los parámetros necesarios para los reportes solicitados
    tipo = request.args.get('tipo','None')
    carnet = request.args.get('carnet','None')
    anio = request.args.get('anio','None')
    mes = request.args.get('mes','None')
    dia = request.args.get('dia','None')
    hora = request.args.get('hora','None')
    semestre = request.args.get('semestre','None')


    if int(tipo) == 0:
        g.grafoArbolAVL(estudiantes)
        return jsonify({
            "message":"Mostrando árbol de estudiantes"
        })

    elif int(tipo) == 1 and carnet != 'None' and anio != 'None' and mes != 'None': 
        estudiantes.reporteMatrizDispersa0(int(carnet), int(anio), int(mes), g)
        if len(estudiantes.auxiliar) == 0: #No se encontró al estudiante buscado
            return jsonify({
                "message":"El estudiante no existe"
            })
        else:                              #Si se encontró al estudiante
            for x in estudiantes.auxiliar:
                estudiantes.auxiliar.clear() #Se elimina lo que hay en la lista
                return jsonify({
                    "message":x
                })

    elif int(tipo) == 2 and carnet != 'None' and anio != 'None' and mes != 'None' and dia != 'None' and hora != 'None':
        estudiantes.reporteListaTareas0(int(carnet), int(anio), int(mes), int(dia), int(hora))
        if len(estudiantes.auxiliar) == 0:
            return jsonify({
                "message":"No se encontró al estudiante"
            })
        else:
            for y in estudiantes.auxiliar:
                estudiantes.auxiliar.clear()
                return jsonify({
                    'message':y
                })

    elif int(tipo) == 3:
        g.arbolB_cursosGeneral(pensum)
        return jsonify({
            "message":"Mostrando árbol de cursos del pensum"
        })

    elif int(tipo) == 4 and carnet != 'None' and anio != 'None' and semestre != 'None':
        estudiantes.reporteArbolB0(int(carnet), int(anio), int(semestre))
        if estudiantes.auxiliar == 0:
            return jsonify({
                "message":"No se encontró el estudiante"
            })
        else:
            for z in estudiantes.auxiliar:
                estudiantes.auxiliar.clear()
                return jsonify({
                    "message":z
                })

    else:
        return jsonify({
            'message':'No se ingresaron los parámetros indicados'
            })

@app.route('/estudiante', methods=['GET','POST','PUT','DELETE'])
def estudiante():
    global estudiantes

    if request.method == 'GET': #Mostrar un estudiante
        carnet = int(request.json['carnet'])
        estudiantes.mostrar_estudiante0(carnet)

        if len(estudiantes.auxiliar) == 0:
            return jsonify({
                "message":"Estudiante no encontrado"
            })
        else:
            for x in estudiantes.auxiliar:
                estudiantes.auxiliar.clear()
                return jsonify({
                    "Dpi":x.dpi,
                    "Nombre":x.nombre,
                    "Carrera":x.carrera,
                    "Correo":x.correo,
                    "Password":x.password,
                    "Creditos":x.creditos,
                    "Edad":x.edad
                })
                
    elif request.method == 'POST': #Crear un estudiante

        #Parseando los datos para poder analizarlos correctamente
        carnet = int(request.json['carnet'])
        dpi = request.json['dpi']
        nombre = request.json['nombre']
        carrera = request.json['carrera']
        correo = request.json['correo']
        password = request.json['password']
        creditos = int(request.json['creditos'])
        edad = int(request.json['edad'])

        #Se crea un nodo de tipo estudiante con los datos parseados
        nuevo = NodoAVL(carnet, dpi, nombre, carrera, correo, password, creditos, edad)

        #Se intenta insertar el estudiante
        estudiantes.insertar0(nuevo, 1)

        if len(estudiantes.auxiliar) == 0:
            return jsonify({
                "message":"Estudiante creado con exito"
            })
        else:
            for x in estudiantes.auxiliar:
                if x == True:
                    estudiantes.auxiliar.clear()
                    return jsonify({
                        "message":"El estudiante ya está ingresado"
                    })

    elif request.method == 'PUT': #Cambiar un estudiante

        #Se parsean los datos para poder analizarlos correctamente
        carnet = int(request.json['carnet'])
        dpi = request.json['dpi']
        nombre = request.json['nombre']
        carrera = request.json['carrera']
        correo = request.json['correo']
        password = request.json['password']
        creditos = int(request.json['creditos'])
        edad = int(request.json['edad'])

        #Arreglo con los datos a analizar ya parseados
        arr = [carnet, dpi, nombre, carrera, correo, password, creditos, edad]
        estudiantes.modificar0(arr)

        if len(estudiantes.auxiliar) == 0:
            return jsonify({
                "message":"Estudiante no encontrado"
            })
        else:
            for x in estudiantes.auxiliar:
                estudiantes.auxiliar.clear()
                return({
                    'message': 'Datos de ' + str(x.carnet) +' cambiados'
                })

    elif request.method == 'DELETE': #Eliminar un estudiante
        carnet = int(request.json['carnet'])
        estudiantes.eliminar0(carnet)

        if len(estudiantes.auxiliar) == 0:
            return ({
                "message":"No se encontró al estudiante"
            })
        else:
            for x in estudiantes.auxiliar:
                if x == True:
                    estudiantes.auxiliar.clear()
                    return jsonify({
                        "message": "Estudiante con carnet " + str(carnet) + " eliminado" 
                    })

@app.route('/recordatorios', methods=['GET','POST','PUT','DELETE'])
def recordatorios():
    global estudiantes

    if request.method == 'GET':
        carnetG = ''
        fechaG = '' #Dia/Mes/Año
        horaG = ''
        posicionG = ''
        try:
            carnetG = request.json['Carnet']
            fechaG = request.json['Fecha'].split('/')
            horaG = request.json['Hora'].split(':')
            posicionG = request.json['Posicion']
        except:
            return jsonify({
                "message":"No se ingresaron los datos requeridos"
            })

        estudiantes.obtener_recordatorio0(int(carnetG),int(fechaG[0]),int(fechaG[1]),int(fechaG[2]),int(horaG[0]), int(posicionG))
        if len(estudiantes.auxiliar) == 0:
            return jsonify({
            'message':'No se encontró la tarea buscada'
        })
        else:
            for x in estudiantes.auxiliar:
                if x.pos == int(posicionG):
                    estudiantes.auxiliar.clear()
                    return jsonify({
                        "Nombre":x.nombre,
                        "Descripcion":x.descripcion,
                        "Materia":x.materia,
                        "Fecha":x.fecha,
                        "Hora":x.hora,
                        "Estado":x.estado
                    })

    elif request.method == 'POST':
        carnet = request.json['Carnet']
        fecha = request.json['Fecha'].split('/')
        hora = request.json['Hora'].split(':')

        nombre = request.json['Nombre']
        descripcion = request.json['Descripcion']
        materia = request.json['Materia'] 
        estado = request.json['Estado']
        #
        datos = [nombre, descripcion, materia, estado]

        estudiantes.crearRecordatorio0(int(carnet), int(fecha[2]), int(fecha[1]), int(fecha[0]), int(hora[0]), datos)

        if len(estudiantes.auxiliar) == 0:
            return jsonify({
                "message":"No se encontró al alumno"
            })
        else:
            estudiantes.auxiliar.clear()
            return jsonify({
                "message":"Recordatorio creado con exito"
            })

    elif request.method == 'PUT':
        carnetP = int(request.json['Carnet'])
        nombreP = request.json['Nombre']
        descripcionP = request.json['Descripcion']
        materiaP = request.json['Materia']
        fechaP = request.json['Fecha']
        horaP = request.json['Hora']
        estadoP = request.json['Estado']
        posicionP = int(request.json['Posicion'])

        datosP = [carnetP,nombreP,descripcionP,materiaP,fechaP,horaP,estadoP,posicionP]
        estudiantes.modificarRecordatorio0(carnetP, datosP)

        if len(estudiantes.auxiliar) == 0:
            return jsonify({
                'message':'No se encontró al alumno'
            })
        else:
            for x in estudiantes.auxiliar:
                estudiantes.auxiliar.clear()
                return jsonify({
                    "message":x
                })

    elif request.method == 'DELETE':
        carnetD = request.json['Carnet']
        fechaD = request.json['Fecha']
        horaD = request.json['Hora']
        posicionD = int(request.json['Posicion'])

        datosD = [fechaD, horaD, posicionD]
        estudiantes.eliminarRecordatorio0(int(carnetD),datosD)
        if len(estudiantes.auxiliar) == 0:
            return jsonify({
                "message":"No se encontró el alumno"
            })
        else:
            for x in estudiantes.auxiliar:
                estudiantes.auxiliar.clear()
                return jsonify({
                    "message":x
                })

@app.route('/cursosEstudiante', methods=['POST'])
def cursosEstudiante():

    dictEstudiantes = request.json['Estudiantes']
    for x in dictEstudiantes:
        #print('\nCarnet: ',x['Carnet'])
        for y in x['Años']:
            #print('Año: ',y['Año'])
            for z in y['Semestres']:
                #print('Semestre: ',z['Semestre'])
                listaCursos = []
                for w in z['Cursos']:
                    codigo = w['Codigo']
                    nombre = w['Nombre']
                    creditos = w['Creditos']
                    prerrequisitos = w['Prerequisitos']
                    obligatorio = w['Obligatorio']
                    curso = NodoCurso(int(codigo),nombre,prerrequisitos,obligatorio,int(creditos))
                    listaCursos.append(curso)

                estudiantes.cursosEstudiante0(int(x['Carnet']),int(y['Año']),int(z['Semestre']),listaCursos)
                listaCursos.clear()
    return jsonify({
        'message':'Cursos ingresados'
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
        creditos = int(x['Creditos'])
        pensum.insertar(codigo, nombre, prerrequisito, tipo,creditos)
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
    archivo.close()

    lista_users = []
    lista_task = []
    #print(len(objetos))
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
        #print('Usuario: ',vars(nuevo))
        estudiantes.insertar0(nuevo, 0)

    for z in lista_task:
        #Quitando las comillas dobles a todos los datos para analizarlos correctamente
        carnetT = int((z.carnet.rstrip('"')).lstrip('"'))
        nombreT = (z.nombre.rstrip('"')).lstrip('"')
        descripcionT = (z.descripcion.rstrip('"')).lstrip('"')
        materiaT = (z.materia.rstrip('"')).lstrip('"')
        fechaT = (z.fecha.rstrip('"')).lstrip('"')
        horaT = (z.hora.rstrip('"')).lstrip('"')
        estadoT = (z.estado.rstrip('"')).lstrip('"')

        datos = [carnetT,nombreT,descripcionT,materiaT,fechaT,horaT,estadoT]
        estudiantes.ingresarTask0(datos)
    
    return jsonify({
        'Contenido': contenido
        }) 

if __name__ == '__main__':
    app.run(threaded = True,port = 3000, debug = True)