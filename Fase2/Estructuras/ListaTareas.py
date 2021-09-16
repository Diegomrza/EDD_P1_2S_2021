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
        else:
            aux = self.primero
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = nuevo
            self.contadorTareas += 1

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

    def mostrar(self):
        aux = self.primero
        while aux != None:
            print(aux.carnet)
            aux = aux.siguiente

'''a = ListaTareas()

for x in range(1,5):
    nodo = NodoTarea(x+2000,'Diego'+str(x),'Desc'+str(x),'Mate'+str(x),'10/10/2021',x,'Pendiente')
    a.insertar(nodo)

g = grafo()
g.listaTareas(a)'''