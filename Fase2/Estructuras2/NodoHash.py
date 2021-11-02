#from Fase2.Estructuras.ListaTareas import ListaTareas
from Estructuras2.ListaSimple import ListaSimple

class NodoHash:
    def __init__(self, llave, carnet, titulo, contenido):
        self.carnet = carnet #Si
        self.lista_apuntes = ListaSimple() #ListaTareas()

        self.llave = llave #Si
        self.siguiente = None #Si