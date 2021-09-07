from Estructuras.Nodos import NodoAnios

class ListaAnios:
    def __init__(self):
        self.primero = None

    def insertar(self, nuevo):

        if self.primero == None:
            self.primero = nuevo
        elif nuevo.id < self.primero.id:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
        else:
            aux = self.primero
            while aux.siguiente != None:
                if nuevo.id < aux.siguiente.id:
                    nuevo.siguiente = aux.siguiente
                    aux.siguiente.anterior = nuevo
                    nuevo.anterior = aux
                    aux.siguiente = nuevo
                    break
                aux = aux.siguiente

            if aux.siguiente == None:
                aux.siguiente = nuevo
                nuevo.anterior = aux
    
    def mostrar(self):
        pass

    def modificar(self):
        pass

    def eliminar(self):
        pass