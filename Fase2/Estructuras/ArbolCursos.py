from Estructuras.Nodos.NodoCursos import NodoCursos
import copy

class Arbol_B:
    def __init__(self, _orden):
        self.orden = _orden
        self.raiz = NodoCursos(5)


    def insertar(self,valor):

                    # [SUBE_ARRIBA, MEDIANA, ND, P]
        array_valores = [False,0,None, None]

        self.empujar(self.raiz, valor, array_valores)

        if array_valores[0]:
            array_valores[3] = NodoCursos(self.orden)
            array_valores[3].cuenta = 1;
            array_valores[3].claves[1] = array_valores[1];
            array_valores[3].ramas[0] = self.raiz;
            array_valores[3].ramas[1] = array_valores[2]
            self.raiz = array_valores[3]



    # flag_pagina = [bool sube_arriba, int mediana, pagina nuevo,P)
    def empujar(self, pagina_actual, valor, flag_pagina):
        camino = [0]  # a que rama irse
        if pagina_actual == None:
            flag_pagina[0] = True # sube_arriba
            flag_pagina[1] = valor # mediana
            flag_pagina[2] = None # pagina nuevo
        else:
            esta = self.buscarPagina(pagina_actual, valor, camino)
            if esta:
                print("hay una clave duplicada: " + valor)
                flag_pagina[0] = False
                return
            self.empujar(pagina_actual.ramas[camino[0]], valor, flag_pagina)
            if flag_pagina[0]:
                if pagina_actual.pagina_llena():
                    self.dividirNodo(pagina_actual,flag_pagina[1],copy.deepcopy(flag_pagina[2]),camino,flag_pagina)
                else:
                    flag_pagina[0] = False
                    self.meterHoja(pagina_actual,flag_pagina[1],flag_pagina[2],camino[0])


    def buscarPagina(self,pagina_actual, valor, camino):
        # Tomar en cuenta que "camino" es la direccion de las ramas por las que puede bajar la busqueda
        encontrado = False
        if valor < pagina_actual.claves[1] :
            camino[0] = 0   # Indica que vajaremos por la rama 0
            encontrado = False

        else: # Examina las claves del nodo en orden descendente

            camino[0] = pagina_actual.cuenta     #iniciamos desde la clave actual

            # Busacamos una posicion hasta donde el valor deje de ser menor
            # (por si viene un valor a los que hay en le nodo )
            while (valor < pagina_actual.claves[camino[0]]) and (camino[0] > 1):
                camino[0] = camino[0] - 1
            encontrado = valor == pagina_actual.claves[camino[0]]
        return encontrado

    def meterHoja(self , actual, valor, rd, k):
        # DESPLAZAR A LA DERECHA LOS ELEMENTOS PARA HACER UN HUECO
        i = actual.cuenta
        while i >= k + 1:
            actual.claves[i + 1] = actual.claves[i]
            actual.ramas[i + 1] = actual.ramas[i]
            i = i-1

        actual.claves[k + 1] = valor
        actual.ramas[k + 1] = rd
        actual.cuenta = actual.cuenta + 1


    def dividirNodo(self, pagina_actual, valor, rd, camino, flag_pagina):
        posMdna = self.orden / 2 if (camino[0] <= self.orden / 2) else self.orden / 2 + 1
        posMdna = int(posMdna)
        flag_pagina[2] = NodoCursos(5)
        i = posMdna + 1
        while i < self.orden:
            # Es desplazada  la mitad drecha al nuevo nodo, la clave mediana se queda en el nodo origen
            flag_pagina[2].claves[i - posMdna] = pagina_actual.claves[i]
            flag_pagina[2].ramas[i - 1] = pagina_actual.ramas[i]
            i = i + 1
        flag_pagina[2].cuenta = (self.orden -1) - posMdna #numero de claves en le nuevo nodo
        pagina_actual.cuenta = posMdna # numero de claves en el nodo origen

        # Es insertada la clave y rama en el nodo que le corresponde
        if camino[0] <= self.orden / 2: # si el camino[0 es menor al minimo de claves que puede haber en la pagina
            self.meterHoja(copy.deepcopy(pagina_actual),valor, rd, camino[0])
        else:
            self.meterHoja(copy.deepcopy(flag_pagina[2]), valor, rd, camino[0] - posMdna) # se inserta el nuevo alvor que trajimos en el nodo nuevo

        # se extrae la clave media del nodo origen
        flag_pagina[1] = pagina_actual.claves[pagina_actual.cuenta]

        # rama 0 del nuevo nodo es la rama de la mediana
        flag_pagina[2].ramas[0] = pagina_actual.ramas[pagina_actual.cuenta]
        pagina_actual.cuenta = pagina_actual.cuenta -1