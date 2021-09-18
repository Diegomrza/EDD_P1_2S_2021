from Estructuras.ArbolCursos import ArbolCursos

class NodoSemestre: #Nodo de la lista de dos semestres posibles
    def __init__(self, id):
        self.siguiente = None
        self.anterior = None
        self.id = id #Número de semestre

        self.cursos = ArbolCursos(5) #Arbol B

class ListaSemestres:
    def __init__(self):
        self.primero = None
        self.lista_semestres = []

    def insertar(self, id):
        if id > 0 and id < 3:
            nuevo = NodoSemestre(id)
            if self.primero == None:
                self.primero = nuevo
                self.lista_semestres.append(nuevo.id)
            elif nuevo.id < self.primero.id:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
                self.lista_semestres.append(nuevo.id)
            else:
                aux = self.primero
                while aux.siguiente != None:
                    if nuevo.id == aux.id:
                        print('El valor ya existe')
                        break
                    elif nuevo.id < aux.siguiente.id:
                        nuevo.siguiente = aux.siguiente
                        aux.siguiente.anterior = nuevo
                        nuevo.anterior = aux
                        aux.siguiente = nuevo
                        self.lista_semestres.append(nuevo.id)
                        break
                    aux = aux.siguiente
                if aux.siguiente == None and self.comparando(nuevo.id):
                    aux.siguiente = nuevo
                    nuevo.anterior = aux
                    self.lista_semestres.append(nuevo.id)
                else:
                    print('El valor ya existe')
        else:
            print('Valor fuera de rango')

    def modificar(self):
        pass

    def eliminar(self, id):
        aux = self.primero
        while aux != None:
            if id == aux.id:
                if id == self.primero.id:
                    aux.siguiente.anterior = None
                    self.primero = aux.siguiente
                    aux.siguiente = None
                    return
                elif aux.siguiente == None:
                    aux.anterior.siguiente = None
                    aux.anterior = None
                    return
                else:
                    aux.anterior.siguiente = aux.siguiente
                    aux.siguiente.anterior = aux.anterior
                    return
            aux = aux.siguiente
        print('No encontrado')

    def mostrar(self):
        aux = self.primero
        while aux != None:
            print('Semestre: ',aux.id)
            aux = aux.siguiente

    def comparando(self, id):
        if id in self.lista_semestres:
            return False
        else:
            return True