from Estructuras.Nodos import NodoAVL

#Estructura complicada

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
    def insertar(self, raiz, nodo): #Recibe como parámetro un nodo de tipo avl
        if raiz == None:
            raiz = nodo
        elif nodo.carnet < raiz.carnet:
            raiz.izquierda = self.insertar(raiz.izquierda, nodo)
        elif nodo.carnet > raiz.carnet:
            raiz.derecha = self.insertar(raiz.derecha, nodo)
        else:
            print('El nodo ya existe')
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

    def eliminar(self):
        pass

    def modificar(self):
        pass
    
    def mostrar0(self):
        self.mostrar(self.root)

    def mostrar(self, raizActual):
        if raizActual == None:
            return
        else:
            self.enorden2(raizActual.izquierda)
            print(raizActual.valor," - ", end="")
            self.enorden2(raizActual.derecha)

    def mostrar_solo_un_nodo(self):
        pass

nuevo = NodoAVL(201901429,2993323220101,'Diego Robles Meza','Ingenieria en ciencias y sistemas','Diegomrza98@gmail.com','7291384650',85,23,2)
nuevo = NodoAVL(201901421,2993323220101,'Diego Abraham Meza','Ingenieria en ciencias y sistemas','Diegomrza98@gmail.com','7291384650',85,23,2)
nuevo = NodoAVL(201901422,2993323220101,'Abraham Robles Meza','Ingenieria en ciencias y sistemas','Diegomrza98@gmail.com','7291384650',85,23,2)
nuevo = NodoAVL(201901423,2993323220101,'Diego Robles','Ingenieria en ciencias y sistemas','Diegomrza98@gmail.com','7291384650',85,23,2)
nuevo = NodoAVL(201901424,2993323220101,'Diego Abraham','Ingenieria en ciencias y sistemas','Diegomrza98@gmail.com','7291384650',85,23,2)
nuevo = NodoAVL(201901425,2993323220101,'Abraham Meza','Ingenieria en ciencias y sistemas','Diegomrza98@gmail.com','7291384650',85,23,2)
nuevo = NodoAVL(201901426,2993323220101,'Abraham Robles','Ingenieria en ciencias y sistemas','Diegomrza98@gmail.com','7291384650',85,23,2)

arbol = ArbolAVL()
arbol.insertar(nuevo)
arbol.mostrar0()