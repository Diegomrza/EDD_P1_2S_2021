from Estructuras.Nodos.NodoAVL import NodoAVL

class ArbolAVL:
    def __init__(self):
        self.root = None

#####################
    def altura(self, nodo): #retorna la altura de un nodo
        if nodo == None:
            return 0
        else:
            return nodo.altura

    def maximo(self, numero1, numero2): #retorna el maximo de dos numeros recibidos
        if numero1 > numero2:
            return numero1
        else:
            return numero2

    def minimo(self, nodo): #retorna el nodo mas a la izquierda de un arbol
        aux = nodo
        while aux.izquierda != None:
            aux = aux.izquierda
        return aux

    def balance(self, nodo):
        if nodo == None:
            return 0

        return self.altura(nodo.derecha) - self.altura(nodo.izquierda)

    def rotar_derecha(self, nodo):
        if nodo != None:
            aux = nodo.izquierda
            nodo.izquierda = aux.derecha
            aux.derecha = nodo
            nodo.altura = self.maximo(self.altura(nodo.izquierda), self.altura(nodo.derecha)) + 1
            aux.altura = self.maximo(self.altura(aux.izquierda), self.altura(aux.derecha)) + 1  
            return aux
        return nodo

    def rotar_izquierda(self, nodo):
        if nodo != None:
            aux = nodo.derecha
            nodo.derecha = aux.izquierda
            aux.izquierda = nodo
            nodo.altura = self.maximo(self.altura(nodo.izquierda), self.altura(nodo.derecha)) + 1
            aux.altura = self.maximo(self.altura(aux.izquierda), self.altura(aux.derecha)) + 1
            return aux
        return nodo
#####################
    def insertar0(self, nodo):
        self.root = self.insertar(self.root, nodo)
    def insertar(self, raiz, nodo): #Recibe como parámetro un nodo de tipo avl
        if raiz == None:
            raiz = nodo
        elif nodo.carnet < raiz.carnet:
            raiz.izquierda = self.insertar(raiz.izquierda, nodo)
        elif nodo.carnet > raiz.carnet:
            raiz.derecha = self.insertar(raiz.derecha, nodo)
        else:
            return raiz
        raiz.altura = self.maximo(self.altura(raiz.izquierda), self.altura(raiz.derecha)) + 1
        balance = self.balance(raiz)

        #rotacion a la derecha
        if balance < -1 and nodo.carnet < raiz.izquierda.carnet:
            return self.rotar_derecha(raiz)
        #rotacion a la izquierda
        if balance > 1 and nodo.carnet > raiz.derecha.carnet:
            return self.rotar_izquierda(raiz)
        #rotacion izquierda derecha
        if balance < -1 and nodo.carnet > raiz.izquierda.carnet:
            raiz.izquierda = self.rotar_izquierda(raiz.izquierda)
            return self.rotar_derecha(raiz)
        #rotacion derecha izquierda
        if balance > 1 and nodo.carnet < raiz.derecha.carnet:
            raiz.derecha = self.rotar_derecha(raiz.derecha)
            return self.rotar_izquierda(raiz)
        return raiz

    def eliminar0(self,valor):
        self.root = self.eliminar(self.root, valor)
    def eliminar(self, raiz, valor):
        if raiz == None:
            return raiz
        if valor < raiz.carnet:
            raiz.izquierda = self.eliminar(raiz.izquierda, valor)
        elif valor > raiz.carnet:
            raiz.derecha = self.eliminar(raiz.derecha, valor)
        else:
            if raiz.izquierda == None or raiz.derecha == None:
                temporal = None
                if temporal == raiz.izquierda:
                    temporal = raiz.derecha
                else:
                    temporal = raiz.izquierda
                if temporal == None:
                    temporal = raiz
                    raiz = None
                    #return raiz
                else:
                    raiz = temporal
            else:
                temporal = self.minimo(raiz.derecha)
                raiz.carnet = temporal.carnet #
                raiz.derecha = self.eliminar(raiz.derecha, temporal.carnet)

        if raiz == None:
            return raiz
        raiz.altura = self.maximo(self.altura(raiz.izquierda), self.altura(raiz.derecha)) + 1
        balance = self.balance(raiz)
        #rotacion a la derecha
        if balance < -1 and valor < raiz.izquierda.carnet:
            return self.rotar_derecha(raiz)
        #rotacion a la izquierda
        if balance > 1 and valor > raiz.derecha.carnet:
            return self.rotar_izquierda(raiz)
        #rotacion izquierda derecha
        if balance < -1 and valor > raiz.izquierda.carnet:
            print('Rotacion doble')
            raiz.izquierda = self.rotar_izquierda(raiz.izquierda)
            return self.rotar_derecha(raiz)
        #rotacion derecha izquierda
        if balance > 1 and valor < raiz.derecha.carnet:
            print('Rotacion doble')
            raiz.derecha = self.rotar_derecha(raiz.derecha)
            return self.rotar_izquierda(raiz)

        return raiz

    def modificar0(self, valor):
        self.modificar(self.root, valor)
    def modificar(self, raiz, valor):
        if raiz == None:
            return raiz
        if valor < raiz.carnet:
            raiz.izquierda = self.modificar(raiz.izquierda, valor)
        elif valor > raiz.carnet:
            raiz.derecha = self.modificar(raiz.derecha, valor)
        else:
            print('Cambios realizados')
            #raiz.carnet = ''
            raiz.dpi = ''
            raiz.nombre = 'F'
            raiz.carrera = 'F'
            raiz.correo = 'F'
            raiz.password = 'F'
            raiz.creditos = ''
            raiz.edad = ''
        return raiz
    
    def mostrar0(self):
        self.mostrar(self.root)
    def mostrar(self, raizActual):
        if raizActual == None:
            return
        else:
            self.mostrar(raizActual.izquierda)
            print(raizActual.carnet,"-", end="")
            print(raizActual.dpi,"-", end="")
            print(raizActual.nombre,"-", end="")
            print(raizActual.carrera,"-", end="")
            print(raizActual.correo,"-", end="")
            print(raizActual.password,"-", end="")
            print(raizActual.creditos,"-", end="")
            print(raizActual.edad,"-", end="")
            print()
            self.mostrar(raizActual.derecha)

    def mostrar_solo_un_nodo0(self,valor):
        self.mostrar_solo_un_nodo(self.root, valor)
    def mostrar_solo_un_nodo(self, raiz, valor):
        if raiz == None:
            return raiz
        if valor < raiz.carnet:
            raiz.izquierda = self.mostrar_solo_un_nodo(raiz.izquierda, valor)
        elif valor > raiz.carnet:
            raiz.derecha = self.mostrar_solo_un_nodo(raiz.derecha, valor)
        else:
            print(raiz.carnet,"-", end="")
            print(raiz.dpi,"-", end="")
            print(raiz.nombre,"-", end="")
            print(raiz.carrera,"-", end="")
            print(raiz.correo,"-", end="")
            print(raiz.password,"-", end="")
            print(raiz.creditos,"-", end="")
            print(raiz.edad,"-", end="")
            print()
        return raiz