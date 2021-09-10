#from ArbolAVL import ArbolAVL


class NodoAVL: #Nodo del arbol de estudiantes
    def __init__(self,carnet,dpi,nombre,carrera,correo,password,creditos,edad, lista_anios):
        self.carnet = carnet #Id
        self.dpi = dpi
        self.nombre = nombre
        self.carrera = carrera
        self.correo = correo
        self.password = password
        self.creditos = creditos
        self.edad = edad
        self.lista_anios = lista_anios #Lista de años

        self.altura = 1
        self.izquierda = None
        self.derecha = None



class NodoAnios: #Nodo de todos los años posibles
    def __init__(self, id):
        self.id = id
        self.meses = None #Lista de meses
        self.semestre = None #Lista de semestres



class NodoMeses: #Nodo de los doce meses posibles en un año
    def __init__(self):
        self.actividades = None #Matriz dispersa



class NodoSemestre: #Nodo de la lista de dos semestres posibles
    def __init__(self):
        self.cursos = None #Arbol B



class NodoDispersa: #Nodo de la matriz dispersa de tareas
    def __init__(self):
        self.filas = None
        self.columnas = None
        self.celdas = None #lista simple de tareas



class NodoTarea:
    def __init__(self, carnet, nombre, descripcion, materia, fecha, hora, estado):
        self.carnet = carnet
        self.nombre = nombre
        self.descripcion = descripcion
        self.materia = materia
        self.fecha = fecha
        self.hora = hora
        self.estado = estado



class NodoCursos: #Temporal hasta nuevos cambios
    def __init__(self):
        pass