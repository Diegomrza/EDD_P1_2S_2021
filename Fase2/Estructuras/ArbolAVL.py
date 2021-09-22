from Estructuras.Nodos.NodoAVL import NodoAVL
from Estructuras.grafo import grafo
from Estructuras.Nodos.NodoTarea import NodoTarea

class ArbolAVL:
    def __init__(self):
        self.root = None
        self.listaNodos = []
        self.buscados = []

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
            self.buscados.append(nodo.carnet)
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
        self.root = self.modificar(self.root, valor)
    def modificar(self, raiz, valor):
        if raiz == None:
            return raiz
        if valor[0] < raiz.carnet:
            raiz.izquierda = self.modificar(raiz.izquierda, valor)
        elif valor[0] > raiz.carnet:
            raiz.derecha = self.modificar(raiz.derecha, valor)
        else:
            raiz.dpi = valor[1]
            raiz.nombre = valor[2]
            raiz.carrera = valor[3]
            raiz.correo = valor[4]
            raiz.password = valor[5]
            raiz.creditos = valor[6]
            raiz.edad = valor[7]
        return raiz
    
    def mostrar0(self):
        self.mostrar(self.root)
    def mostrar(self, raizActual):
        if raizActual == None:
            return
        else:
            self.mostrar(raizActual.izquierda)
            #print(raizActual.carnet,"-", end="")
            #print(raizActual.dpi,"-", end="")
            #print(raizActual.nombre,"-", end="")
            #print(raizActual.carrera,"-", end="")
            #print(raizActual.correo,"-", end="")
            #print(raizActual.password,"-", end="")
            #print(raizActual.creditos,"-", end="")
            #print(raizActual.edad,"-", end="")
            #print()
            self.listaNodos.append(raizActual)
            self.mostrar(raizActual.derecha)
            
    #Para mostrar matriz dispersa
    def mostrar_solo_un_nodo0(self, valor, anio, mes):
        self.mostrar_solo_un_nodo(self.root, valor, anio, mes)
    def mostrar_solo_un_nodo(self, raiz, valor, anio, mes):
        if raiz == None:
            return raiz
        if valor < raiz.carnet:
            raiz.izquierda = self.mostrar_solo_un_nodo(raiz.izquierda, valor, anio, mes)
        elif valor > raiz.carnet:
            raiz.derecha = self.mostrar_solo_un_nodo(raiz.derecha, valor, anio, mes)
        else:

            year = raiz.lista_anios.buscar(anio)
            if year != None:
                mes = year.meses.buscarMes(mes)
                if mes != None:
                    print('Mes encontrado', mes.mes)
                    gAVL = grafo()
                    gAVL.matrizDispersa(mes.actividades)
                else:
                    print('\nEl mes no existe en los meses del usuario buscado')
            else:
                print('\nEl año no existe en la lista del usuario')

        return raiz
    
    #Para mostrar lista de tareas
    def mostrar_tareas0(self, valor, anio, mes, dia, hora):
        self.mostrar_tareas(self.root, valor, anio, mes, dia, hora)
    def mostrar_tareas(self, raiz, valor, anio, mes, dia, hora):
        if raiz == None:
            return raiz
        if valor < raiz.carnet:
            raiz.izquierda = self.mostrar_tareas(raiz.izquierda, valor, anio, mes, dia, hora)
        elif valor > raiz.carnet:
            raiz.derecha = self.mostrar_tareas(raiz.derecha, valor, anio, mes, dia, hora)
        else:

            year = raiz.lista_anios.buscar(anio)
            if year != None:
                mes = year.meses.buscarMes(mes)
                if mes != None:
                    listaTareas = mes.actividades.buscarLista(hora, dia)
                    if listaTareas != None:
                        print('Contador: ',listaTareas.celdas.contadorTareas)
                        listaTareas.celdas.mostrar()
                    else:
                        print('No hay elementos en la lista')
                else:
                    print('\nEl mes no existe en los meses del usuario buscado')
            else:
                print('\nEl año no existe en la lista del usuario')

        return raiz

    #Get Estudiante
    def mostrar_estudiante0(self, carnet):
        self.mostrar_estudiante(self.root, carnet)
    def mostrar_estudiante(self, raiz, carnet):
        if raiz == None:
            return raiz
        if carnet < raiz.carnet:
            raiz.izquierda = self.mostrar_estudiante(raiz.izquierda, carnet)
        elif carnet > raiz.carnet:
            raiz.derecha = self.mostrar_estudiante(raiz.derecha, carnet)
        else:
            print('encontrado: ', vars(raiz))
        return raiz

    #Para recordatorios
    def get_(self, raiz, carnet, anio, mes, dia, hora, datos):
        #aux = None
        if raiz == None:
            return None
        if carnet < raiz.carnet:
            raiz.izquierda = self.get_(raiz.izquierda, carnet, anio, mes, dia, hora, datos) 
        elif carnet > raiz.carnet:
            raiz.derecha = self.get_(raiz.derecha, carnet, anio, mes, dia, hora, datos)
        else:
            anio_encontrado = raiz.lista_anios.buscar(anio)
            if anio_encontrado != None:
                print('Encontrado')
                mes_encontrado = anio_encontrado.meses.buscarMes(mes)
                if mes_encontrado != None:
                    print('Encontrado')
                    matriz = mes_encontrado.actividades.buscarLista(hora,dia)
                    if matriz != None:
                        print('Encontrado')
                        nuevo = NodoTarea(carnet, datos[0], datos[1], datos[2], str(dia)+'/'+str(mes)+'/'+str(anio), hora, datos[3])
                        matriz.celdas.insertar(nuevo)
                    else:
                        print('Nel')
                else:
                    print('Nel')
            else:
                print('Nel')
            
        return raiz

