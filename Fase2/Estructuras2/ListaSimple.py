class NodoSimple:
    def __init__(self, carnet, titulo, contenido):
        self.carnet = carnet
        self.titulo = titulo
        self.contenido = contenido
        self.id = 1
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.primero = None
        self.contador = 1

    def insertar(self, carnet, titulo, contenido):
        nuevoApunte = NodoSimple(carnet, titulo, contenido)

        if self.primero == None:
            self.primero = nuevoApunte
            
            nuevoApunte.id = self.contador
            self.contador += 1
        else:
            aux = self.primero
            while aux.siguiente != None:
                aux = aux.siguiente
                
            aux.siguiente = nuevoApunte

            nuevoApunte.id = self.contador
            self.contador += 1

    def mostrarApuntes(self):
        aux = self.primero
        while aux != None:
            print(vars(aux))
            aux = aux.siguiente
        print('-------')