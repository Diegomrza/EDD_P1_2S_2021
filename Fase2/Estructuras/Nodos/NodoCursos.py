#Nodo de Arbol B
from Estructuras.Nodos.NodoAVL import NodoAVL

class NodoCursos: 
    def __init__(self, orden):
        self.cuenta = 0
        self.m = orden
        #               Nodo estudiantes
        self.claves = [ 0 for x in range(orden)]
        self.ramas = [ NodoCursos for x in range(orden)]

        self.codigo_curso = None
        self.nombre = None
        self.creditos = None
        self.codigos_prerrequisito = None
        self.tipo = None #Obligatorio o no

        for i in range(orden):
            self.ramas [i] = None

    def pagina_llena(self):
        return self.cuenta == self.m -1

    def pagina_semillena(self):
        return self.cuenta < self.m/2