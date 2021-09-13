from Estructuras.Nodos.NodoAnios import NodoAnios
#from Nodos.NodoAnios import NodoAnios

class ListaAnios:
    def __init__(self):
        self.primero = None

    def insertar(self, anio):
        nodo = NodoAnios(anio)
        if self.primero == None:
            self.primero = nodo
        elif nodo.id < self.primero.id:
            nodo.siguiente = self.primero
            self.primero.anterior = nodo
            self.primero = nodo
        else:
            aux = self.primero
            while aux.siguiente != None:
                
                if nodo.id < aux.siguiente.id:
                    nodo.siguiente = aux.siguiente
                    aux.siguiente.anterior = nodo
                    nodo.anterior = aux
                    aux.siguiente = nodo
                    break
                elif nodo.id == aux.id:
                    print('El valor ya existe')
                    break
                aux = aux.siguiente
            if aux.siguiente == None:
                aux.siguiente = nodo
                nodo.anterior = aux
                
    def modificar(self):
        aux = self.primero
        while aux != None:
            if id == aux.id:
                print('Aqui realizar los cambios')
            aux = aux.siguiente

    def eliminar(self,id):
        aux = self.primero
        while aux != None:
            if id == aux.id:
                if id == self.primero.id:
                    aux.siguiente.anterior = None
                    self.primero = aux.siguiente
                    aux.siguiente = None
                    break
                elif aux.siguiente == None:
                    aux.anterior.siguiente = None
                    aux.anterior = None
                    break
                else:
                    aux.anterior.siguiente = aux.siguiente
                    aux.siguiente.anterior = aux.anterior
                    break
            aux = aux.siguiente

    def mostrar(self):
        aux = self.primero
        while aux != None:
            print('Año: ',aux.id)
            aux = aux.siguiente
        print('\n')
