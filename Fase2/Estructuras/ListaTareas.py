from Estructuras.Nodos.NodoTarea import NodoTarea
#from grafo import grafo

class ListaTareas:
    def __init__(self):
        self.primero = None
        self.contadorTareas = 0

    def insertar(self, nuevo):
        if self.primero == None:
            self.primero = nuevo
            self.contadorTareas += 1
            nuevo.pos = self.contadorTareas
        else:
            aux = self.primero
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = nuevo
            self.contadorTareas += 1
            nuevo.pos = self.contadorTareas

    def modificar(self, id):
        aux = self.primero
        while aux != None:
            if aux.carnet == id:
                print('cambiando')
            aux = aux.siguiente

    def eliminar(self, id):
        aux = self.primero
        while aux != None:
            if id == self.primero.carnet:
                self.primero = aux.siguiente
                aux = None
                break
            elif aux.siguiente.carnet == id:
                #temp = aux.siguiente
                aux.siguiente = aux.siguiente.siguiente
                #temp = None
                break
            aux = aux.siguiente

    #Muestra toda la lista
    def mostrar(self):
        aux = self.primero
        while aux != None:
            print(vars(aux))
            aux = aux.siguiente
    
    def obtener_un_elemento(self, pos):
        aux = self.primero
        while aux != None:
            if pos == aux.pos:
                return aux
            aux = aux.siguiente
        return None