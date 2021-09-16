from Estructuras.Nodos.NodoDispersa import NodoDispersa
#import random

#Estructuras adicionales para la matriz dispersa
class NodoEncabezado:
    def __init__(self, id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.acceso = None

class ListaEncabezado:
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

    def devolver_encabezado(self, id):
        aux = self.primero
        while aux != None:
            if aux.id == id:
                return aux
            aux = aux.siguiente
        return None

#Matriz Dispersa
class Dispersa:
    def __init__(self):
        self.encabezado_filas = ListaEncabezado()
        self.encabezado_columnas = ListaEncabezado()
        self.contador_filas = 0
        self.contador_columnas = 0
                                       #lista de tareas
    def insertar(self, fila, columna, contenido):
        nuevo_nodo = NodoDispersa(fila, columna)
        nuevo_nodo.celdas = contenido
        if (fila > 0 and fila < 25) and (columna > 0 and columna < 25):
            if self.contador_filas < 25:
                efila = self.encabezado_filas.devolver_encabezado(fila)
                if efila == None:
                    efila = NodoEncabezado(fila)
                    efila.acceso = nuevo_nodo
                    self.encabezado_filas.insertar(efila)
                    self.contador_filas += 1
                else:
                    if nuevo_nodo.columna < efila.acceso.columna:
                        nuevo_nodo.derecha = efila.acceso
                        efila.acceso.izquierda = nuevo_nodo
                        efila.acceso = nuevo_nodo
                    else:
                        aux = efila.acceso
                        while aux.derecha != None:
                            if nuevo_nodo.columna < aux.derecha.columna:
                                nuevo_nodo.derecha = aux.derecha
                                aux.derecha.izquierda = nuevo_nodo
                                nuevo_nodo.izquierda = aux
                                aux.derecha = nuevo_nodo
                                break
                            aux = aux.derecha
                        if aux.derecha == None:
                            aux.derecha = nuevo_nodo
                            nuevo_nodo.izquierda = aux

            #Insertar encabezado columna
            if self.contador_columnas < 25:
                ecolumna = self.encabezado_columnas.devolver_encabezado(columna)
                if ecolumna == None:
                    ecolumna = NodoEncabezado(columna)
                    ecolumna.acceso = nuevo_nodo
                    self.encabezado_columnas.insertar(ecolumna)
                    self.contador_columnas += 1
                else:
                    if nuevo_nodo.fila < ecolumna.acceso.fila:
                        nuevo_nodo.abajo = ecolumna.acceso
                        ecolumna.acceso.arriba = nuevo_nodo
                        ecolumna.acceso = nuevo_nodo
                    else:
                        aux = ecolumna.acceso
                        while aux.abajo != None:
                            if nuevo_nodo.fila < aux.abajo.fila:
                                nuevo_nodo.abajo = aux.abajo
                                aux.abajo.arriba = nuevo_nodo
                                nuevo_nodo.arriba = aux
                                aux.abajo = nuevo_nodo
                                break
                            aux = aux.abajo
                        if aux.abajo == None:
                            aux.abajo = nuevo_nodo
                            nuevo_nodo.arriba = aux

    def recorrerColumnas(self):
        eColumna = self.encabezado_columnas.primero
        print('\n************ #Recorrido por columnas ************')

        while eColumna != None:

            actual = eColumna.acceso
            print('\ncolumna ',str(actual.columna))
            print('fila  Valor')
            while actual != None:
                print(str(actual.fila)+"    "+actual.celdas)
                actual = actual.abajo
            eColumna = eColumna.siguiente
        print('*********** fin recorrido por columnas ************')
