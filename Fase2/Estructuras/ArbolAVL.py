from Estructuras.ListaTareas import ListaTareas
from Estructuras.Nodos.NodoAnios import NodoAnios
from Estructuras.Nodos.NodoMeses import NodoMeses
from Estructuras.grafo import grafo
from Estructuras.Nodos.NodoTarea import NodoTarea

class ArbolAVL:
    def __init__(self):
        self.root = None
        self.listaNodos = [] #Para el avl

        self.auxiliar = []

        self.buscadosCrear = [] #Aqui se guardan los estudiantes que se crean para comprobar si se repiten
        self.buscados = [] #Aqui se guardan todos los estudiantes que se mandan a buscar
        self.buscadosModificar = [] #Aqui se guardan los estudiantes a modificar
        self.buscadosEliminar = [] #Aqui se guardan los estudiantes a eliminar

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
    def insertar0(self, nodo, tipo):
        self.root = self.insertar(self.root, nodo, tipo)      
    def insertar(self, raiz, nodo, tipo): #Recibe como parámetro un nodo de tipo avl
        if raiz == None:
            raiz = nodo
        elif nodo.carnet < raiz.carnet:
            raiz.izquierda = self.insertar(raiz.izquierda, nodo, tipo)
        elif nodo.carnet > raiz.carnet:
            raiz.derecha = self.insertar(raiz.derecha, nodo, tipo)
        else:
            if tipo == 1:
                self.auxiliar.append(True)
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
            self.auxiliar.append(True)
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
                raiz.carnet = temporal.carnet
                raiz.dpi = temporal.dpi
                raiz.nombre = temporal.nombre
                raiz.carrera = temporal.carrera
                raiz.correo = temporal.correo
                raiz.password = temporal.password
                raiz.creditos = temporal.creditos
                raiz.edad = temporal.edad
                #raiz = temporal
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
            self.auxiliar.append(raiz)
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
            
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#
    #Para mostrar el reporte de la matriz dispersa 
    def reporteMatrizDispersa0(self, valor, anio, mes, g):
        self.root = self.reporteMatrizDispersa(self.root, valor, anio, mes, g)
    def reporteMatrizDispersa(self, raiz, valor, anio, mes, g):
        if raiz == None:
            return raiz
        if valor < raiz.carnet:
            raiz.izquierda = self.reporteMatrizDispersa(raiz.izquierda, valor, anio, mes, g)
        elif valor > raiz.carnet:
            raiz.derecha = self.reporteMatrizDispersa(raiz.derecha, valor, anio, mes, g)
        else:
            year = raiz.lista_anios.buscar(anio)
            if year != None:
                mesAux = year.meses.buscarMes(mes)
                if mesAux != None:
                    g.matrizDispersa(mesAux.actividades)
                    self.auxiliar.append('Matriz encontrada')
                else:
                    self.auxiliar.append('El mes no existe en los meses del usuario buscado')
            else:
                self.auxiliar.append('El año no existe en la lista del usuario')
        return raiz
    
    #Para mostrar el reporte de la lista de tareas
    def reporteListaTareas0(self, valor, anio, mes, dia, hora):
        self.root = self.reporteListaTareas(self.root, valor, anio, mes, dia, hora)
    def reporteListaTareas(self, raiz, valor, anio, mes, dia, hora):
        if raiz == None:
            return raiz
        if valor < raiz.carnet:
            raiz.izquierda = self.reporteListaTareas(raiz.izquierda, valor, anio, mes, dia, hora)
        elif valor > raiz.carnet:
            raiz.derecha = self.reporteListaTareas(raiz.derecha, valor, anio, mes, dia, hora)
        else:
            year = raiz.lista_anios.buscar(anio)
            if year != None:
                mesAux = year.meses.buscarMes(mes)
                if mesAux != None:
                    listaTareas = mesAux.actividades.buscarLista(hora, dia)
                    if listaTareas != None:
                        g = grafo()
                        g.listaTareas(listaTareas.celdas)
                        self.auxiliar.append('Lista encontrada')
                    else:
                        self.auxiliar.append('La lista no tiene ningún elemento')
                else:
                    self.auxiliar.append('El mes no existe en los meses del usuario buscado')
            else:
                self.auxiliar.append('El año no existe en la lista del usuario')
        return raiz

    #Para mostrar el árbol B de un estudiante
    def reporteArbolB0(self, carnet, anio, semestre):
        self.root = self.reporteArbolB(self.root, carnet, anio, semestre)
    def reporteArbolB(self, raiz, carnet, anio, semestre):
        if raiz == None:
            return raiz
        elif carnet < raiz.carnet:
            raiz.izquierda = self.reporteArbolB(raiz.izquierda, carnet, anio, semestre)
        elif carnet > raiz.carnet:
            raiz.derecha = self.reporteArbolB(raiz.derecha, carnet, anio, semestre)
        else:
            year = raiz.lista_anios.buscar(anio)
            if year != None:
                semestreAux = year.semestre.buscarSemestre(semestre)
                if semestreAux != None:
                    grafoB = grafo()
                    grafoB.arbolB_cursosGeneral(semestreAux.cursos)
                    self.auxiliar.append('Graficando el árbol b')
                else:
                    self.auxiliar.append('No se encontró el semestre')
            else:
                self.auxiliar.append('No se encontró el año indicado')
        return raiz

    #Para mostrar la información de un estudiante (Método GET)
    def mostrar_estudiante0(self, carnet):
        self.root = self.mostrar_estudiante(self.root, carnet)
    def mostrar_estudiante(self, raiz, carnet):
        if raiz == None:
            return raiz
        if carnet < raiz.carnet:
            raiz.izquierda = self.mostrar_estudiante(raiz.izquierda, carnet)
        elif carnet > raiz.carnet:
            raiz.derecha = self.mostrar_estudiante(raiz.derecha, carnet)
        else:
            self.auxiliar.append(raiz)
            #self.buscados.append(raiz)
        return raiz

    #POST recordatorios
    def crearRecordatorio0(self, carnet, anio, mes, dia, hora, datos):
        self.root = self.crearRecordatorio(self.root, carnet, anio, mes, dia, hora, datos)
    def crearRecordatorio(self, raiz, carnet, anio, mes, dia, hora, datos):
        if raiz == None:
            return None
        if carnet < raiz.carnet:
            raiz.izquierda = self.crearRecordatorio(raiz.izquierda, carnet, anio, mes, dia, hora, datos)
        elif carnet > raiz.carnet:
            raiz.derecha = self.crearRecordatorio(raiz.derecha, carnet, anio, mes, dia, hora, datos)
        else:

            year = raiz.lista_anios.buscar(anio)
            fecha = str(dia)+'/'+str(mes)+'/'+str(anio)
            nuevaTarea = NodoTarea(carnet, datos[0], datos[1], datos[2], fecha, hora, datos[3])

            if year != None: #si el año existe
                mesAux = year.meses.buscarMes(mes)
                if mesAux != None: #Si el mes existe
                    matriz = mesAux.actividades.buscarLista(hora,dia)
                    if matriz != None: #Si la celda existe
                        matriz.celdas.insertar(nuevaTarea)
                    else: 
                        listaT = ListaTareas()
                        listaT.insertar(nuevaTarea)
                        mesAux.actividades.insertar(hora,dia,listaT)
                else: 
                    nuevoMes0 = NodoMeses(mes)
                    listaT0 = ListaTareas()
                    listaT0.insertar(nuevaTarea)
                    nuevoMes0.actividades.insertar(hora, dia, listaT0)
                    year.meses.insertar(nuevoMes0)
            else:
                nuevoAnio = NodoAnios(anio)
                nuevoMes = NodoMeses(mes)
                tareas = ListaTareas()

                tareas.insertar(nuevaTarea)
                nuevoAnio.meses.insertar()
                nuevoMes.actividades.insertar(hora, dia, tareas)

                raiz.lista_anios.insertar(nuevoAnio)
        return raiz

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
                #print('Encontrado')
                mes_encontrado = anio_encontrado.meses.buscarMes(mes)
                if mes_encontrado != None:
                    #print('Encontrado')
                    matriz = mes_encontrado.actividades.buscarLista(hora,dia)
                    if matriz != None:
                        #print('Encontrado')
                        nuevo = NodoTarea(carnet, datos[0], datos[1], datos[2], str(dia)+'/'+str(mes)+'/'+str(anio), hora, datos[3])
                        matriz.celdas.insertar(nuevo)
                    else:
                        print('Matriz')
                else:
                    print('Mes no existe')
            else:
                print('Año no existe')
            
        return raiz


    #GET recordatorios
    def obtener_recordatorio0(self,carnet, dia, mes, anio, hora, pos):
        self.root = self.obtener_recordatorio(self.root,carnet, dia, mes, anio, hora, pos)
    def obtener_recordatorio(self, raiz, carnet, dia, mes, anio, hora, pos):
        if raiz == None:
            return raiz
        if carnet < raiz.carnet:
            raiz.izquierda = self.obtener_recordatorio(raiz.izquierda, carnet, dia, mes, anio, hora, pos)
        elif carnet > raiz.carnet:
            raiz.derecha = self.obtener_recordatorio(raiz.derecha, carnet, dia, mes, anio, hora, pos)
        else:
            #NodoAño
            anioGET = raiz.lista_anios.buscar(anio)
            if anioGET != None:
                #NodoMes
                mesGET = anioGET.meses.buscarMes(mes)
                if mesGET != None:
                    #Lista
                    dispersaGET = mesGET.actividades.buscarLista(hora, dia)
                    if dispersaGET != None:
                        aux = dispersaGET.celdas.obtener_un_elemento(pos)
                        if aux != None:
                            self.buscados.append(aux)
                        else:
                            print('No')
                    else:
                        print('No')
                else:
                    print('No')
            else:
                print('No')
        return raiz

    #DELETE
