from Estructuras2.TablaHash import TablaHash
from cryptography.fernet import Fernet
import hashlib
import time, threading, datetime

#Importaciones nodos estructuras
from Estructuras.Nodos.NodoAVL import NodoAVL
from Estructuras.Nodos.NodoCursos import NodoCurso
from Estructuras.Nodos.NodoTarea import NodoTarea

#Importaciones estructuras
from Estructuras.ArbolAVL import ArbolAVL
from Estructuras.ArbolCursos import ArbolCursos
from Estructuras.grafo import grafo
from Estructuras.GrafoPensum import grafoPensum
from Estructuras2.merkleTree import merkleTree, nodoMerkle
from Estructuras2.BlockChain import Block, BlockChain

#importaciones flask
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from Analizadores.sintactico import parser, objetos

#Creacion de carpeta Reportes
import os
import errno

try:
    os.mkdir(r'C:\Users\Squery\Desktop\Reportes_F3')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

ob = NodoAVL(0,'','','','','',0,0)
obj = NodoTarea(0,'','','','',0,'')

estudiantes = ArbolAVL() #Arbol AVL de estudiantes
pensum = ArbolCursos(5) #Arbol B de cursos
g = grafo() #para los reportes
gPensum = grafoPensum() #Grafo nuevo

th1 = TablaHash(7) #Tablas hash

#Las 3 operaciones posibles para el blockchain: crear apunte, crear estudiante, asignar un curso
listaApuntes = [] 
listaEstudiantes = [] 
listaCursos = [] 

merkleEstudiantes = merkleTree() #Arbol de merkle estudiantes
merkleCursos = merkleTree() #Arbol de merkle cursos
merkleApuntes = merkleTree() #Arbol de merkle apuntes

#BlockChain
cadenaDeBloques = BlockChain()

clave = Fernet.generate_key()
encriptador = Fernet(clave)


tiempoCronometro = 1.0

@app.route('/')
def index():
    '''while True:
        time.sleep(300)'''
    return '<h1>El server está corriendo</h1>'
        

    #return '<h1>El servidor está corriendo!</h1>'

@app.route('/carga', methods=['POST'])
def carga():
    estudiante = request.json['estudiantes']
    pensum = request.json['pensum']
    cursos = request.json['cursos']
    apuntes = request.json['apuntes']

    '''if tipo.lower() == 'estudiantes':
        #ply(ruta)'''

    if estudiante != 'None':
        rutaEstudiantes = r'C:\Users\Squery\Documents\GitHub\EDD_SmartClass_201901429\Fase2'+'\\'+estudiante

        archivoEstudiantes = open(rutaEstudiantes, encoding="utf8"); contenidoEstudiantes = archivoEstudiantes.read()
        cargarEstudiantes(json.loads(contenidoEstudiantes))

    if pensum != 'None':
        rutaPensum = r'C:\Users\Squery\Documents\GitHub\EDD_SmartClass_201901429\Fase2'+'\\'+pensum

        archivoPensum = open(rutaPensum, encoding='utf8'); contenidoPensum = archivoPensum.read()
        cargarPensumGeneral(json.loads(contenidoPensum))

    if cursos != 'None':
        rutaCursos = r'C:\Users\Squery\Documents\GitHub\EDD_SmartClass_201901429\Fase2'+'\\'+cursos
        archivoCursos = open(rutaCursos, encoding='utf8'); contenidoCursos = archivoCursos.read()
        cargarPensumEstudiantes(json.loads(contenidoCursos))

    if apuntes != 'None':
        rutaApuntes = r'C:\Users\Squery\Documents\GitHub\EDD_SmartClass_201901429\Fase2'+'\\'+apuntes
        
        archivoApuntes = open(rutaApuntes, encoding="utf8"); contenidoApuntes = archivoApuntes.read()
        cargarApuntes(json.loads(contenidoApuntes))

    #Si la petición fue correcta
    return jsonify({
        'message' : 'Success',
        'reason':"Archivos leídos con exito"
    })

@app.route('/reporte', methods=['GET'])
def reporte():
    global estudiantes #Arbol AVL
    global pensum #Arbol B
    global g, encriptador, th1, gPensum, merkleEstudiantes, merkleCursos, merkleApuntes

    #Obteniendo todos los parámetros necesarios para los reportes solicitados
    tipo = request.args.get('tipo','None')
    carnet = request.args.get('carnet','None')
    anio = request.args.get('anio','None')
    mes = request.args.get('mes','None')
    dia = request.args.get('dia','None')
    hora = request.args.get('hora','None')
    semestre = request.args.get('semestre','None')

    if int(tipo) == 0: #Estudiantes desencriptados
        try:
            nombre = g.grafoArbolAVL(estudiantes, encriptador)

            return jsonify({
                "message" : "Success",
                "reason":"Mostrando árbol de estudiantes",
                "nombre" : nombre
            })
        except:
            return jsonify({
                "message":"Failed",
                "reason":"No se pudo generar la imagen"
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

    elif int(tipo) == 3: #Grafo completo
        #g.arbolB_cursosGeneral(pensum)
        try:
            nombre = g.grafoCompletoPensum(gPensum)
            return jsonify({
                "message":"Success",
                "reason":"Mostrando árbol de cursos del pensum",
                "nombre" : nombre
            })
        except:
            return jsonify({
                "message":"Failed",
                "reason":"No se pudo generar la imagen"
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
                if z[0] == '1':
                    return jsonify({
                        "message":"Success",
                        "nombre":z[1]
                    })
                else :
                    return jsonify({
                        "message":"Failed",
                        "reason":z[1]
                    })

    elif int(tipo) == 5: #Estudiantes encriptados
        try:
            nombre = g.grafoAVLEncriptado(estudiantes)
            return jsonify({
                "message":"Success",
                "reason" : "Mostrando árbol de estudiantes encriptado",
                "nombre" : nombre
            })
        except:
            return jsonify({
                "message":"Failed",
                "reason":"No se pudo generar la imagen"
            })

    elif int(tipo) == 6: #Tabla hash
        try:
            nombre = g.tablaHash(th1)
            return jsonify({
                "message":"Success",
                "reason":"Creación de imagen exitosa",
                "nombre":nombre
            })
        except:
            return jsonify({
                "message":"Failed",
                "reason":"No se pudo generar la imagen"
            })

    elif int(tipo) == 7: #árbol de merkle apuntes
        g.graficarMerkle(merkleEstudiantes)
        return jsonify({
            "message":"Success",
            "reason":"Exito"
        })

    elif int(tipo) == 8: #árbol de merkle cursos
        return jsonify({

        })

    elif int(tipo) == 9: #árbol de merkle estudiantes
        return jsonify({
            
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


#Endpoints nuevos
@app.route('/login', methods=['POST'])
def login():
    global estudiantes, encriptador
    #Toma de datos
    password = request.json['password']

    if request.json['usuario'] == 'admin' and password == 'admin':
        return jsonify({
            "message":"Success",
            "reason":"Credenciales correctas, bienvenid@",
            "nombre":"admin",
            "tipo":"administrador"
        })
    elif request.json['usuario'] == 'admin' and password != 'admin':
        return jsonify({
            "message":"Failed",
            "reason":"Credenciales incorrectas, intente de nuevo"
        })
    
    carnet = int(request.json['usuario'])
    password = hashlib.sha256(password.encode()); #password = cifrarDatos(password.hexdigest())
    #Busqueda en el arbol avl
    estudiantes.mostrar_estudiante0(carnet)

    if len(estudiantes.auxiliar) == 0:
        return jsonify({
            "message":"Failed",
            "reason":"Estudiante no encontrado"
        })
    else:
        for x in estudiantes.auxiliar:
            estudiantes.auxiliar.clear()
            if carnet == x.carnet and password.hexdigest() == encriptador.decrypt(x.password.encode()).decode():
                return jsonify({
                    #"Dpi":x.dpi,
                    "nombre":encriptador.decrypt(x.nombre.encode()).decode(),
                    #"Carrera":x.carrera,
                    #"Correo":x.correo,
                    #"Password":x.password,
                    #"Creditos":x.creditos,
                    #"Edad":x.edad,
                    "message":"Success",
                    "reason":"Credenciales correctas, bienvenid@ ",
                    "tipo":x.tipo
                })
            else:
                return jsonify({
                    "message":"Failed",
                    "reason":"Credenciales incorrectas"
                })

@app.route('/registro', methods = ['POST'])
def registro():

    global estudiantes
    global listaEstudiantes

    carnet = int(request.json['carnet'])

    dpi0 = int(request.json['dpi'])
    dpi = cifrarDatos(dpi0)

    nombre0 = request.json['nombre']
    nombre = cifrarDatos(nombre0)

    carrera0 = request.json['carrera']
    carrera = cifrarDatos(carrera0)

    correo0 = request.json['correo']
    correo = cifrarDatos(correo0)

    password0 = request.json['password']
    password1 = hashlib.sha256(password0.encode())
    password = cifrarDatos(password1.hexdigest())
    
    edad0 = int(request.json['edad'])
    edad = cifrarDatos(edad0)

    tipo = request.json['tipo']
    #tipo = cifrarDatos(tipo)

    creditos0 = int(request.json['creditos'])
    creditos = cifrarDatos(creditos0)

    nuevo = NodoAVL(carnet, dpi, nombre, carrera, correo, password, creditos, edad)
    nuevo.tipo = tipo
    estudiantes.insertar0(nuevo, 1)

    if len(estudiantes.auxiliar) == 0:
        listaEstudiantes.append(nuevo)
        return jsonify({
            "message":"Success",
            "reason":"Estudiante creado con exito"
        })
    else:
        for x in estudiantes.auxiliar:
            if x == True:
                estudiantes.auxiliar.clear()
                return jsonify({
                    "message":"Failed",
                    "reason":"El estudiante ya existe"
                })

@app.route('/recuperarPassword', methods=['GET'])
def recuperarPassword():
    global estudiantes, clave
    carnet = request.args.get('carnet','None')
    estudiantes.mostrar_estudiante0(int(carnet))

    for x in estudiantes.auxiliar:
        if int(carnet) == x.carnet:
            return jsonify({
                "message" : "Success",
                "password" : x.password
            })

    return jsonify({
        "message" : "Failed"
    })

#Obtiene todos los apuntes de un estudiante
@app.route('/obtenerApuntes/<int:usuario>', methods=['GET'])
def obtenerApuntes(usuario):
    global th1

    estudiante = th1.busqueda2(usuario)
    listaAux = []
    listaAux2 = []

    if estudiante != None:
        aux = estudiante.lista_apuntes.primero
        while aux != None:
            listaAux.append(aux)
            aux = aux.siguiente

    for x in listaAux:
        apunte = {"titulo":x.titulo,"contenido":x.contenido,"id":x.id}
        listaAux2.append(apunte)

    return jsonify(listaAux2)

#Obtiene un apunte de un estudiante
@app.route('/apunte/<int:id>/<int:carnet>', methods=['GET'])
def apunte(carnet, id):
    
    global th1
    estudiante = th1.busqueda2(carnet)
    if estudiante != None:
        aux = estudiante.lista_apuntes.primero
        while aux != None:
            if id == aux.id:
                return jsonify({
                    "contenido":aux.contenido,
                    "titulo":aux.titulo,
                    "message":"Success"
                })
            aux = aux.siguiente
    else:
        return jsonify({
            "message":"Failed",
            "contenido":"None"
        })

#Creación de un apunte para un estudiante
@app.route('/crearApunteNuevo', methods=['POST'])
def crearApunteNuevo():
    global th1
    global listaApuntes

    carnet = request.json['carnet']
    titulo = request.json['titulo']
    contenido = request.json['contenido']
    #print(carnet, titulo, contenido)

    th1.insertarHash(int(carnet), titulo, contenido)
    #th1.mostrar()
    #print(th1.tamanio)
    #                    carnet, titulo, contenido
    listaApuntes.append([carnet, titulo, contenido])
    return jsonify({
        "message":"Success",
        "reason":"Apunte creado con exito"
    })

@app.route('/asignarCursos', methods=['POST'])
def asignarCursos():
    global listaCursos
    fecha = datetime.datetime.now()
    contenido = request.json['contenido']
    carnet = request.json['carnet']
    #print(type(contenido))
    try:
        cargarPensumEstudiantes(json.loads(contenido))
        listaCursos.append([carnet, contenido, fecha])
        return jsonify({
        "message" : "Success",
        "reason" : "Cursos asignados"
    })
    except:
        return jsonify({
            "message" : "Failed",
            "reason" : "Error al asignar los cursos"
        })
    

@app.route('/tiempo', methods=['POST'])
def tiempo():
    global tiempoCronometro
    tiempo = request.json['tiempo']
    try:
        tiempoCronometro = float(tiempo)
        return jsonify({
            "message":"Success",
            "reason":"Tiempo cambiado con exito"
        })
    except:
        return jsonify({
            "message":"Failed",
            "reason":"Ocurrió un problema al intentar cambiar el tiempo"
        })
    

@app.route('/PruebaTrabajo', methods=['POST'])
def PruebaTrabajo():
    global cadenaDeBloques

    dificultad = request.json['dificultad']
    print(type(dificultad))
    cadenaDeBloques.dificultad = dificultad

    return jsonify({
        "message":"Success",
        "reason":"Cambiado correctamente"
    })

def cargarEstudiantes(diccionario_estudiantes):
    global estudiantes
    for x in diccionario_estudiantes['estudiantes']:
        carnet = int(x['carnet']); #carnet = cifrarDatos(carnet)
        DPI = int(x['DPI']); DPI = cifrarDatos(DPI)
        nombre = x['nombre']; nombre = cifrarDatos(nombre)
        carrera = x['carrera']; carrera = cifrarDatos(carrera)
        correo = x['correo']; correo = cifrarDatos(correo)
        password = x['password']; password = hashlib.sha256(password.encode()); password = cifrarDatos(password.hexdigest())
        creditos = int('0'); creditos = cifrarDatos(creditos) #x['creditos']
        edad = int(x['edad']); edad = cifrarDatos(edad)
        nuevoESTUDIANTE = NodoAVL(carnet, DPI, nombre, carrera, correo, password, creditos, edad)
        estudiantes.insertar0(nuevoESTUDIANTE, 1)

def cargarApuntes(diccionario_apuntes):
    global th1
    for x in diccionario_apuntes['usuarios']:
        #print('Carnet: ', x['carnet'],'\n')
        for y in x['apuntes']:
            carnet = x['carnet']
            titulo = ''
            contenido = ''
            for z in y:
                if z == 'Título':
                    titulo = y[z]
                if z == 'Contenido':
                    contenido = y[z]
            th1.insertarHash(int(carnet), titulo, contenido)
    print(th1.tamanio)

def cargarPensumGeneral(diccionario_pensum_general):
    global pensum, gPensum
    for x in diccionario_pensum_general['Cursos']:
        codigo = int(x['Codigo'])
        nombre = x['Nombre']
        prerrequisito = ['Prerequisitos']
        tipo = x['Obligatorio']
        creditos = int(x['Creditos'])
        pensum.insertar(codigo, nombre, prerrequisito, tipo, creditos)
    
    for x in diccionario_pensum_general['Cursos']:
        codigo = x['Codigo']
        nombre = x['Nombre']
        creditos = x['Creditos']
        prerequisitos = x['Prerequisitos'].split(',')
        obligatorio = x['Obligatorio']

        gPensum.insertar(codigo, nombre, creditos, prerequisitos, obligatorio)

def cargarPensumEstudiantes(diccionario_pensum_estudiantes):
    global estudiantes
    dictEstudiantes = diccionario_pensum_estudiantes['Estudiantes']
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

def cifrarDatos(dato):
    global encriptador
    if type(dato) != str:
        dato = str(dato)
    token = encriptador.encrypt(dato.encode())
    return token.decode()

def crearHash(dato):
    if type(dato) != str:
            dato = str(dato)
    return hashlib.sha256(dato.encode()).hexdigest()

def merkle_apuntes():
    global merkleApuntes, th1
    aux = th1.primero
    lista = []
    while aux != None:
        aux2 = aux.lista_apuntes.primero
        while aux2 != None:
            lista.append(aux2.titulo+aux2.contenido+str(aux2.carnet))
            aux2 = aux2.siguiente
        aux = aux.siguiente
    lista2 = []
    for x in lista:
        lista2.append(nodoMerkle(None, None, crearHash(x)))
    merkleApuntes.hashing(lista2)

def crearArchivoBloque(merkleRoot):
    global cadenaDeBloques
    cadenaDeBloques.addBloque(merkleRoot)
    
def nuevoBloque():
    global merkleApuntes, merkleCursos, merkleEstudiantes
    global listaApuntes, listaCursos, listaEstudiantes
    global g

    lista0 = []
    lista1 = []
    lista2 = []

    if len(listaApuntes) != 0:
        for x in listaApuntes:
            nuevo0 = nodoMerkle(None, None, crearHash(x[0]+x[1]+x[2]))
            lista0.append(nuevo0)
    else:
        lista0.append(nodoMerkle(None, None, crearHash('-1')))
    
    if len(listaCursos) != 0:
        for y in listaCursos:
            nuevo1 = nodoMerkle(None, None, crearHash(y[0]+y[1]+str(y[2])))
            lista1.append(nuevo1)
    else:
        lista1.append(nodoMerkle(None, None, crearHash('-1')))
    
    if len(listaEstudiantes) != 0:
        for z in listaEstudiantes:
            nuevo2 = nodoMerkle(None, None, crearHash(str(z.carnet)+str(z.dpi)+z.nombre+z.carrera+z.correo+z.password+str(z.edad)))
            lista2.append(nuevo2)
    else:
        lista2.append(nodoMerkle(None, None, crearHash('-1')))

    merkleApuntes.hashing(lista0); g.graficarMerkle(merkleApuntes)
    merkleCursos.hashing(lista1); g.graficarMerkle(merkleCursos)
    merkleEstudiantes.hashing(lista2); g.graficarMerkle(merkleEstudiantes)

    merkleRoot = crearHash(merkleApuntes.root.hash+merkleCursos.root.hash+merkleEstudiantes.root.hash)
    crearArchivoBloque(merkleRoot)

    merkleApuntes.limpiarArbol()
    merkleCursos.limpiarArbol()
    merkleEstudiantes.limpiarArbol()
    
    listaApuntes.clear()
    listaCursos.clear()
    listaEstudiantes.clear()

def temporizador():
    global tiempoCronometro
    while True:
        time.sleep(tiempoCronometro)
        nuevoBloque()

t1 = threading.Thread(target=temporizador)
t1.start()

if __name__ == '__main__':
    app.run(threaded = True,port = 3000, debug = True)

#from Estructuras.Nodos.NodoDispersa import NodoDispersa
#from Estructuras.Dispersa import Dispersa
#from Estructuras.ListaAnios import ListaAnios
#from Estructuras.ListaMeses import ListaMeses
#from Estructuras.ListaSemestres import ListaSemestres
#from Estructuras.ListaTareas import ListaTareas
#from Estructuras.Nodos.NodoMeses import NodoMeses
#from Estructuras.Nodos.NodoAnios import NodoAnios