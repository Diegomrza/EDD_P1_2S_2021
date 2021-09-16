from Estructuras.Nodos.NodoAnios import NodoAnios
#from Nodos.NodoAnios import NodoAnios

class ListaAnios:
    def __init__(self):
        self.primero = None
        self.lista_anios = []

    def insertar(self, nodo):
        #nodo = NodoAnios(anio)
        if self.primero == None:
            self.primero = nodo
            self.lista_anios.append(nodo.id)
        elif nodo.id < self.primero.id:
            nodo.siguiente = self.primero
            self.primero.anterior = nodo
            self.primero = nodo
            self.lista_anios.append(nodo.id)
        else:
            aux = self.primero
            while aux.siguiente != None:
                if nodo.id == aux.id:
                    print('El valor ya existe')
                    break
                elif nodo.id < aux.siguiente.id:
                    nodo.siguiente = aux.siguiente
                    aux.siguiente.anterior = nodo
                    nodo.anterior = aux
                    aux.siguiente = nodo
                    self.lista_anios.append(nodo.id)
                    break
                aux = aux.siguiente
            if aux.siguiente == None and self.comparando(nodo.id):
                aux.siguiente = nodo
                nodo.anterior = aux
                self.lista_anios.append(nodo.id)
                
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

    def comparando(self, id):
        '''lista = [] for x in self.lista_anios: if x not in lista: lista.append(x)'''
        if id in self.lista_anios:
            return False
        else:
            return True

'''listaAños = ListaAnios()

listaAños.insertar(2020)
listaAños.insertar(2020)
listaAños.insertar(2020)
listaAños.insertar(2021)
listaAños.insertar(2023)
listaAños.insertar(2023)
listaAños.insertar(2025)
listaAños.insertar(2025)
listaAños.insertar(2025)

listaAños.mostrar()'''