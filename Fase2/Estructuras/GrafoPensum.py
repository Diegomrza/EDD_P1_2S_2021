
import json
class nodoGrafo:
    def __init__(self, codigo, nombre, creditos, prerequisitos, obligatorio):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.prerequisitos = prerequisitos
        self.obligatorio = obligatorio

class grafoPensum:
    def __init__(self):
        self.nodos = []

    def insertar(self, codigo, nombre, creditos, prerequisitos, obligatorio):
        #print(codigo, nombre, creditos, prerequisitos, obligatorio)
        nuevo = nodoGrafo(codigo, nombre, creditos, prerequisitos, obligatorio)
        self.nodos.append(nuevo)
    
    def obtenerPonderacion(self, codigo):
        for x in self.nodos:
            if x.codigo == codigo:
                return x.creditos
        return 

def cargar():
    archivo = open(r'C:\Users\Squery\Documents\GitHub\EDD_SmartClass_201901429\Fase2\CursosPensum.json')
    contenido = archivo.read()
    contenido = json.loads(contenido)
    gf = grafoPensum()
    for x in contenido['Cursos']:
        codigo = x['Codigo']
        nombre = x['Nombre']
        creditos = x['Creditos']
        prerequisitos = x['Prerequisitos'].split(',')
        obligatorio = x['Obligatorio']

        gf.insertar(codigo, nombre, creditos, prerequisitos, obligatorio)
    
    