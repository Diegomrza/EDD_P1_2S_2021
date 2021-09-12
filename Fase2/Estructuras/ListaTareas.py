from Nodos.NodoTarea import NodoTarea

class ListaTareas:
    def __init__(self):
        self.primero = None

    def insertar(self, nuevo):
        if self.primero == None:
            self.primero = nuevo
        else:
            aux = self.primero
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = nuevo

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

a = ListaTareas()

for x in range(1,5):
    nodo = NodoTarea(x+2000,'','','','',x,'')
    a.insertar(nodo)

a.mostrar()
a.modificar(2001)
a.eliminar(2002)
a.mostrar()