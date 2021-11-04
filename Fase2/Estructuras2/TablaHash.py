from Estructuras2.NodoHash import NodoHash

class TablaHash:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.primero = None
        self.factor_carga = 0.0
        self.id = 0
        self.carnets = []
    
    def insertarHash(self, carnet, titulo, contenido):
        #Calculamos de primero el factor de carga
        self.factor_carga = (self.id/self.tamanio)*100
        #print('factor carga',self.factor_carga)
        if self.factor_carga < 50 and self.factor_carga >= 0:
            llave = 0
            bandera = False
            for x in self.carnets:
                if x[0] == carnet:
                    llave = x[1]
                    bandera = True
                    break
            if bandera == False:
                llave = carnet % self.tamanio #Método división

            if self.buscarLlave(llave) and bandera == True:
                auxiliar = self.busqueda(llave)
                auxiliar.lista_apuntes.insertar(carnet, titulo, contenido)
            else:
                self.insertar(carnet, titulo, llave, contenido)

        else:
            #Realizando un rehash
            self.tamanio += 2
            self.insertarHash(carnet, titulo, contenido)
            
    def insertar(self, carnet, titulo, llave_calculada, contenido):
        nuevo = NodoHash(llave_calculada, carnet, titulo, contenido)
        
        if self.primero == None:
            #self.primero = nuevo
            self.id += 1
            nuevo.lista_apuntes.insertar(carnet, titulo, contenido)
            self.primero = nuevo
            self.carnets.append([nuevo.carnet, nuevo.llave]) ##
            return
        
        #Aplicando la colisión, para saber si la llave ya existe
        if self.buscarLlave(llave_calculada): #Solo entra si es True
            i = 0
            #pos = self.buscarPos(nuevo, i)
            pos = self.cuadratica(nuevo, i)
            self.insertar(carnet, titulo, pos, contenido)
        else:
            nuevo.lista_apuntes.insertar(carnet, titulo, contenido)
            tmp = self.primero
            if nuevo.llave < tmp.llave: #Inserción al inicio
                nuevo.siguiente = tmp
                self.primero = nuevo
                self.id += 1
                self.carnets.append([nuevo.carnet, nuevo.llave]) ###
            else: #Inserción al medio
                while tmp.siguiente != None:
                    tmp2 = tmp.siguiente
                    if nuevo.llave < tmp2.llave:
                        tmp.siguiente = nuevo
                        nuevo.siguiente = tmp2
                        self.id += 1
                        self.carnets.append([nuevo.carnet, nuevo.llave]) ###
                        break
                    tmp = tmp.siguiente
                if tmp.siguiente == None: #Inserción al final
                    tmp.siguiente = nuevo
                    self.id +=1
                    self.carnets.append([nuevo.carnet, nuevo.llave]) ###


    def buscarPos(self, actual, i):
        #Se usa la función: 
        pos = (actual.llave % self.tamanio)*i
        if self.buscarLlave(pos): #La posicion ya está ocupada por lo tanto se debe buscar otra posición
            i = i + 1
            return self.buscarPos(actual, i)
        #si la posicion no está ocupada se retorna la posicion calculada
        return pos


    #Exploración cuadrática /////////////////////////////////////////////////////
    def cuadratica(self, actual, i):
        pos = (actual.llave + i*i)%self.tamanio
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
    
    def mostrar(self): #Muestra todos estudiantes en la tabla
        aux = self.primero
        while aux != None:
            print(vars(aux))
            print('Apuntes: ')
            aux.lista_apuntes.mostrarApuntes()
            aux = aux.siguiente


    def busqueda(self, llave): #Retorna un estudiante
        aux = self.primero
        while aux != None:
            if llave == aux.llave:
                return aux
            aux = aux.siguiente
        return None
    
    def busqueda2(self, carnet):
        aux = self.primero
        while aux != None:
            if carnet == aux.carnet:
                return aux
            aux = aux.siguiente
        return None