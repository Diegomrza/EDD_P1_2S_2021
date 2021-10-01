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

    def modificar(self, pos, datos):
        aux = self.primero
        while aux != None:
            if aux.pos == pos:
                aux.carnet = datos[0]
                aux.nombre = datos[1]
                aux.descripcion = datos[2]
                aux.materia = datos[3]
                aux.fecha = datos[4]
                aux.hora = datos[5]
                aux.estado = datos[6]
                return True
            aux = aux.siguiente
        return False
        
    def eliminar(self, pos):
        aux = self.primero
        while aux != None:
            if pos == self.primero.pos:
                self.primero = aux.siguiente
                aux = None
                self.contadorTareas-=1
                break
            elif aux.siguiente.pos == pos:
                #temp = aux.siguiente
                aux.siguiente = aux.siguiente.siguiente
                self.contadorTareas-=1
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