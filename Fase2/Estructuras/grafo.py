from typing import List
from graphviz import Digraph
from os import startfile, system

#from Estructuras.Dispersa import Dispersa
class grafo:
    def __init__(self):
        self.contadorArbolAVL = 0
        self.contadorDispersa = 0
        self.contadorListaTareas = 0
        self.contadorArbolBGeneral = 0
        self.contadorArbolEstudiante = 0

    def grafoArbolAVL(self, arbolAVL):
        pass

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
        print(cad_aux) 
        archivo = open('grafo.dot','w')
        archivo.write(cad_aux)
        archivo.close()

        system('dot -Tpng grafo.dot -o grafo.png')
        #system('cd ./grafo.png')
        startfile('grafo.png')

    def listaTareas(self, listaTareas):
        cadena = ''

        g = Digraph('G', format='png', node_attr={'shape': 'record', 'height': '.1'}, edge_attr={ 'dir':'both'})
        g.attr(label = 'Imagen original')
        
        for x in range(1,10):
            g.node(str(x), label=''+'|'+str(x)+'|'+'')
        g.node(str(10), label=''+'|'+'10'+'|'+'')
            
        
        for x in range(1, 10):
            g.edge(str(x),str(x+1))
        


        nombre = 'grafo'+str(self.contadorListaTareas)
        g.render(nombre)
        self.contadorListaTareas += 1

    def arbolB_cursosGeneral(self, arbolB_general):
        pass

    def arbolB_cursosEstudiante(self, arbolB_Estudiante):
        pass


#Parte de graficar dispersa
'''if len(lista_nodos_separados) > 1:
                        print('heloou')
                        for nodosSeparados in range(0,len(lista_nodos_separados)):
                            if nodosSeparados+1 < len(lista_nodos_separados):
                                separar = lista_nodos_separados[nodosSeparados].split(',')
                                separar2 = lista_nodos_separados[nodosSeparados+1].split(',')

                                cad_aux += 'nodo'+str(separar[0]+'_'+str(separar[1]))+'->'
                                cad_aux += 'nodo'+str(separar2[0]+'_'+str(separar2[1]))+';\n'
                            rankFilas += 'nodo'+str(separar[0]+'_'+str(separar[1]))+';'
                    else:'''