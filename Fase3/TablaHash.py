from NodoHash import NodoHash

class TablaHash:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.primero = None
        self.factor_carga = 0.0
        self.id = 0
    
    def insertarHash(self, carnet, nombre):
        #Calculamos de primero el factor de carga
        self.factor_carga = (self.id/self.tamanio)*100
        if self.factor_carga < 56 and self.factor_carga >= 0:
            llave = carnet % self.tamanio
            self.insertar(carnet,nombre, llave)
        else:
            #Realizando un rehash
            self.tamanio += 2

    def insertar(self, carnet, nombre, llave_calculada):
        nuevo = NodoHash(llave_calculada, carnet, nombre)

        if self.primero == None:
            self.primero = nuevo
            self.id += 1
            return
        #Aplicando la colisión, para saber si la llave ya existe
        if self.buscarLlave(llave_calculada): #Solo entra si es True
            i = 0
            #pos = self.buscarPos(nuevo, i)
            pos = self.cuadratica(nuevo, i)
            self.insertar(carnet, nombre, pos)
        else:
            tmp = self.primero
            if nuevo.llave < tmp.llave: #Insercion al inicio
                nuevo.siguiente = tmp
                self.primero = nuevo
                self.id += 1
            else: #Insercion al medio
                while tmp.siguiente != None:
                    tmp2 = tmp.siguiente
                    if nuevo.llave < tmp2.llave:
                        tmp.siguiente = nuevo
                        nuevo.siguiente = tmp2
                        self.id += 1
                        break
                    tmp = tmp.siguiente
                if tmp.siguiente == None: #insercion al final
                    tmp.siguiente = nuevo
                    self.id +=1



    def buscarPos(self, actual, i):
        #Se usa la función: 
        pos = (actual.llave % self.tamanio)*i
        if self.buscarLlave(pos): #La posicion ya está ocupada por lo tanto se debe buscar otra posición
            i = i + 1
            return self.buscarPos(actual, i)
        #si la posicion no está ocupada se retorna la posicion calculada
        return pos



    #Exploración cuadrática /////////////////////////////////////////////////////
    def cuadratica(self,actual, i):
        pos = i*i
        if self.buscarLlave(pos):
            i = i + 1
            return self.cuadratica(actual, i)
        return pos
    #///////////////////////////////////////////////////////////////////////////


    def buscarLlave(self, llave):
        tmp = self.primero
        while tmp != None:
            if llave == tmp.llave:
                return True
            tmp = tmp.siguiente
        return False