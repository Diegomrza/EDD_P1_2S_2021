from Estructuras.ListaTareas import ListaTareas

class NodoDispersa: #Nodo de la matriz dispersa de tareas
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None
        
        self.celdas = ListaTareas() #lista simple de tareas