#from typing import List
from graphviz import Digraph
from os import startfile, system
import queue
import os

from Estructuras.Cola import Cola

#from Estructuras.Dispersa import Dispersa
class grafo:
    def __init__(self):
        self.contadorArbolAVL = 0
        self.contadorDispersa = 0
        self.contadorListaTareas = 0
        self.contadorArbolBGeneral = 0
        self.contadorArbolEstudiante = 0

    def grafoArbolAVL(self, arbolAVL):
        print('Método grafo avl')
        
        cola = Cola()
        cola.encolar(arbolAVL.root)
        while cola.es_vacia() != True:
            nodo = cola.desencolar()
            print(vars(nodo),'\n')
            if nodo.izquierda != None:
                cola.encolar(nodo.izquierda)
            if nodo.derecha != None:
                cola.encolar(nodo.derecha)
      
    def matrizDispersa(self, matriz):
        lista_nodos = []
        lista_cabecera_filas = []
        lista_cabecera_columnas = []

        cad_aux = '''digraph g{\nnode[shape=box]\nsubgraph h{\nlabel="Matriz dispersa"\nraiz[label="0,0"]\nedge[dir="both"]\n'''
        eColumna = matriz.encabezado_columnas.primero
        eFila = matriz.encabezado_filas.primero
        contadorGrupos = 1
        rankdir = '{rank=same;raiz;'
        stringNodos = ''

        while eFila != None:
            actual = eFila.acceso

            cad_aux += 'Fila'+str(actual.fila)+'[label="'+str(actual.fila)+'", group=1];\n'
            cad_aux += 'Fila'+str(actual.fila)+'->'+'Fila'+str(eFila.siguiente.acceso.fila)+';\n'
            lista_cabecera_filas.append(str(actual.fila))
            eFila = eFila.siguiente

            if eFila.siguiente == None:
                actual = eFila.acceso
                cad_aux += 'Fila'+str(actual.fila)+'[label="'+str(actual.fila)+'", group=1];\n'
                lista_cabecera_filas.append(str(actual.fila))
                break

        while eColumna != None:
            actual2 = eColumna.acceso

            aux = actual2   #variable temporal para obtener los nodos sin afectar la creacion de filas y columnas
            while aux != None:
                stringNodos += 'nodo'+str(aux.fila)+'_'+str(actual2.columna)+'[label="'+str(aux.fila)+','+str(actual2.columna)+'", group='+str(actual2.columna+1)+']\n' #Creacion de nodos del grafo
                lista_nodos.append(str(aux.fila)+','+str(actual2.columna))
                aux = aux.abajo 

            cad_aux += 'Columna'+str(actual2.columna)+'[label="'+str(actual2.columna)+'", group='+str(contadorGrupos+1)+'];\n'
            cad_aux += 'Columna'+str(actual2.columna)+'->'+'Columna'+str(eColumna.siguiente.acceso.columna)+';\n'
            rankdir += 'Columna'+str(actual2.columna)+';'
            contadorGrupos+=1

            lista_cabecera_columnas.append(str(actual2.columna))
            
            eColumna = eColumna.siguiente

            if eColumna.siguiente == None:
                actual2 = eColumna.acceso
                cad_aux += 'Columna'+str(actual2.columna)+'[label="'+str(actual2.columna)+'", group='+str(contadorGrupos+1)+'];\n'

                aux2 = actual2
                while aux2 != None:
                    stringNodos += 'nodo'+str(aux2.fila)+'_'+str(actual2.columna)+'[label="'+str(aux2.fila)+','+str(actual2.columna)+'", group='+str(actual2.columna+1)+']\n' #Creacion del ultimo nodo del grafo
                    lista_nodos.append(str(aux2.fila)+','+str(actual2.columna))
                    aux2 = aux2.abajo

                rankdir += 'Columna'+str(actual2.columna)+';'
                lista_cabecera_columnas.append(str(actual2.columna))
                break

        cad_aux += 'raiz->Fila1;\nraiz->Columna1\n'
        cad_aux += rankdir.rstrip(';')+'}\n'
        cad_aux += stringNodos
        
        for x in lista_cabecera_filas:
            for y in lista_nodos:
                nodoTemp = y.split(',')
                if x == nodoTemp[0]:
                    cad_aux += 'Fila'+ x +'->'+'nodo'+nodoTemp[0]+'_'+nodoTemp[1]+';\n'
                    break
            
        for i in lista_cabecera_filas:
            rankFilas = '{rank=same;Fila'+str(i)+';' #Numero de fila
            lista_nodos_separados = []

            for j in range(0, len(lista_nodos)):
                nodo_temp = lista_nodos[j].split(',') #[f, c]
                if i == nodo_temp[0]:
                    lista_nodos_separados.append(nodo_temp[0]+','+nodo_temp[1])  #["f,c", "f,c"]...

                    #Parte de graficar nodo matriz dispersa
                    if len(lista_nodos_separados) > 1:
                        print('heloou')
                        for nodosSeparados in range(0,len(lista_nodos_separados)):
                            if nodosSeparados+1 < len(lista_nodos_separados):
                                separar = lista_nodos_separados[nodosSeparados].split(',')
                                separar2 = lista_nodos_separados[nodosSeparados+1].split(',')

                                cad_aux += 'nodo'+str(separar[0]+'_'+str(separar[1]))+'->'
                                cad_aux += 'nodo'+str(separar2[0]+'_'+str(separar2[1]))+';\n'
                            rankFilas += 'nodo'+str(separar[0]+'_'+str(separar[1]))+';'
                    else:
                        unSoloNodo = lista_nodos_separados[0].split(',')
                        rankFilas += 'nodo'+str(unSoloNodo[0]+'_'+str(unSoloNodo[1]))+';'
                    ######################################

                lista_nodos_separados.clear()
            rankFilas = rankFilas.rstrip(';')
            rankFilas+='}\n'
            cad_aux += rankFilas

        for k in lista_cabecera_columnas:
            for l in lista_nodos:
                nodoTemp = l.split(',')
                if k == nodoTemp[1]:
                    cad_aux += 'Columna'+k+'->'+'nodo'+nodoTemp[0]+'_'+nodoTemp[1]+';\n'
                    break
        
        print('Filas: ')
        for nF in lista_cabecera_filas:
            listaF = []
            for n in lista_nodos:
                nodo = n.split(',')
                if nF == nodo[0]:
                    listaF.append(int(nodo[1]))
            if len(listaF) > 1:
                for elementoF in range(len(listaF)-1):
                    cad_aux += 'nodo'+str(nF)+'_'+str(listaF[elementoF])+'->nodo'+str(nF)+'_'+str(listaF[elementoF+1])+';\n'
            listaF.clear()
        #
        print('Columnas: ')
        for nC in lista_cabecera_columnas:
            listaC = []
            for n2 in lista_nodos:
                nodo2 = n2.split(',')
                if nC == nodo2[1]:
                    listaC.append(int(nodo2[0]))
            print('Col: ',nC, 'ListaC: ',listaC)
            if len(listaC) > 1:
                for elementoC in range(len(listaC)-1):
                    cad_aux += 'nodo'+str(listaC[elementoC])+'_'+str(nC)+'->nodo'+str(listaC[elementoC+1])+'_'+str(nC)+';\n'
            listaC.clear()

        cad_aux += '}\n}\n'
        #print(cad_aux)
        nombre = ''
        nombre += 'matriz' + str(self.contadorDispersa)
        self.contadorDispersa += 1
        archivo = open(nombre+'.dot','w')
        archivo.write(cad_aux)
        archivo.close()

        system('dot -Tpng'+' '+nombre+'.dot -o'+nombre+'.png')
        system('cd ./matriz.png')
        startfile(nombre+'.png')

    def listaTareas(self, listaTareas):
        print('Grafo tareas')

        g = Digraph('G', format='png', node_attr={'shape': 'box', 'height': '.1','rank':'same'}, edge_attr={ 'dir':'both'})
        g.attr(rankdir='LR')
        
        aux = listaTareas.primero
        lista = []
        while aux != None:
            cad = ''
            cad += str(aux.carnet) + '\n'
            cad += aux.nombre    + '\n'
            cad += aux.descripcion + '\n'
            cad += aux.materia + '\n'
            cad += aux.fecha + '\n'
            cad += str(aux.hora) + '\n'
            cad += aux.estado + '\n'
            g.node(str(aux.carnet), label=cad)
            lista.append(aux.carnet)
            aux = aux.siguiente

        for x in range(len(lista)):
            if x < len(lista)-1:
                g.edge(str(lista[x]),str(lista[x+1]))
            else:
                continue
        
        nombre = 'ListaTareas'+str(self.contadorListaTareas)
        g.render(nombre)
        self.contadorListaTareas += 1
        startfile(nombre+'.png')

    def arbolB_cursosGeneral(self, arbolB_general):
        # [ ACUMULADOR, ACUMULADORE DE ENLACES, CONTADOR PAGINA, CONTADOR AUX ]
        acumulador = ["digraph G\n{\nnode[shape = record, height= .1];\n", "", 0, 0]

        if arbolB_general.raiz != None:
            cola = queue.Queue()
            cola.put(arbolB_general.raiz)

            while not(cola.empty()): # Mientras la cola no este vacia
                tmpPagina = cola.get()
                self.imprimir(tmpPagina, acumulador)
                print(acumulador,'\n\n') #tmpPagina, 
                i = 0
                while i <= tmpPagina.cuenta:
                    if tmpPagina.ramas[i] != None:
                        cola.put(tmpPagina.ramas[i])
                    i += 1
                acumulador[2] += 1 #contador de pagina
            acumulador[0] += "\n" + acumulador[1]

        acumulador[0] += "}\n"

        f = open('grafo.dot', 'w')
        try:
            f.write(acumulador[0])
        finally:
            f.close()

        prog = "dot -Tsvg  grafo.dot -o grafo.svg"
        os.system(prog)

    def imprimir(self, actual, acumulador):
        acumulador[0] += 'node{}[label="<r0>'.format(str(acumulador[2]))

        if actual.ramas[0] != None:
            acumulador[3] += 1 # contador auxiliar
            acumulador[1] += '"node{}":r0 -> "node{}"\n'.format(str(acumulador[2]) , str(acumulador[3]))

        i = 1
        while i <= actual.cuenta:
            acumulador[0] += '|<c{}> {} |<r{}>'.format(str(i),'Codigo: '+str(actual.claves[i]),str(i))

            if actual.ramas[i] != None:
                acumulador[3] += 1 # contador auxiliar
                acumulador[1] += '"node{}":r{} -> "node{}"\n'.format(str(acumulador[2]) ,str(i), str(acumulador[3]))
            i += 1
        acumulador[0] += '"];\n'

    def arbolB_cursosEstudiante(self, arbolB_Estudiante):
        pass

