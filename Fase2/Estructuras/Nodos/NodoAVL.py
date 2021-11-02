from Estructuras.ListaAnios import ListaAnios

class NodoAVL: #Nodo del arbol de estudiantes
    def __init__(self,carnet,dpi,nombre,carrera,correo,password,creditos,edad):
        self.carnet = carnet #Id
        self.dpi = dpi
        self.nombre = nombre
        self.carrera = carrera
        self.correo = correo
        self.password = password
        self.creditos = creditos
        self.edad = edad
        self.lista_anios = ListaAnios() #Lista de años
        self.tipo = "estudiante"

        self.altura = 1
        self.izquierda = None
        self.derecha = None