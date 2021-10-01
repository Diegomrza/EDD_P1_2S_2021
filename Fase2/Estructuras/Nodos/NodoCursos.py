#Nodo de Arbol B
from Estructuras.Nodos.NodoAVL import NodoAVL

class Pagina: 
    def __init__(self, orden):
        self.cuenta = 0
        self.m = orden
        self.claves = [ NodoCurso(0,"","",False,0) for x in range(orden)]
        self.ramas = [ Pagina for x in range(orden)]

        for i in range(orden):
            self.ramas [i] = None

    def pagina_llena(self):
        return self.cuenta == self.m -1

    def pagina_semillena(self):
        return self.cuenta < self.m/2

class NodoCurso:
    def __init__(self, codigo, nombre, prerrequisito, tipo, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.prerrequisito = prerrequisito
        self.tipo = tipo
        self.creditos = creditos