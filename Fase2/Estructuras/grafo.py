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

        cadena = '''digraph G {\nnode[shape=box]
        '''
        
        cola = Cola() #Creando la cola
        au = ['',arbolAVL.root]
        cola.encolar(au) #Metiendo la raiz a la cola

        while cola.es_vacia() != True:
            nodo = cola.desencolar()
            if nodo[0] != '':
                cadena += str(nodo[1].carnet)+'[label="'+str(nodo[1].carnet)+'\n'+nodo[1].nombre+'\n'+nodo[1].carrera+'"];\n'
                cadena += str(nodo[0].carnet)+"->"+str(nodo[1].carnet)+";\n"
            else:
                cadena += str(nodo[1].carnet)+'[label="'+str(nodo[1].carnet)+'\n'+nodo[1].nombre+'\n'+nodo[1].carrera+'"];\n'

            if nodo[1].izquierda != None:
                aux = [nodo[1], nodo[1].izquierda]
                cola.encolar(aux)
            if nodo[1].derecha != None:
                aux2 = [nodo[1], nodo[1].derecha]
                cola.encolar(aux2)
        
            
        cadena += '''}'''
        #
        #print(cadena)
        nombre = r'C:\Users\Squery\Desktop\Reportes_F2\arbolAVL'+str(self.contadorArbolAVL)
        archivo = open(nombre+'.dot','w')
        archivo.write(cadena)
        archivo.close()
        cadena = ''
        system('dot -Tsvg'+' '+nombre+'.dot -o '+nombre+'.svg')
        #system('cd ./'+nombre+'.png')
        startfile(nombre+'.svg')
        self.contadorArbolAVL += 1

    def matrizDispersa(self, matriz):
        principal = 'digraph g{\nlabel="Matriz dispersa"\nnode[shape=box]\nsubgraph h{\n'
        principal += 'raiz[label="Inicio",group="1"]\nedge[dir="both"]\n\n'

        grupos = 2

        F='Fila'; C='Columna'; N='nodo' #constantes para facilitar las filas y columnas
        listaFilas = [] #Se almacenan las filas de la matriz
        listaColumnas = [] #Se almacenan las columnas de la matriz

        recorridoFilas = [] #Aquí se guardarán todas las filas
        recorridoColumnas = [] #Aquí se guardarán todas las columnas

        eFila = matriz.encabezado_filas.primero #primer elemento de la lista de filas
        eColumna = matriz.encabezado_columnas.primero #primer elemento de la lista de columnas

        while eFila != None:
            actual = eFila.acceso
            listaFilas.append(actual)
            listaAux = []

            while actual != None:
                listaAux.append(actual)
                actual = actual.derecha
                
            recorridoFilas.append(listaAux)
            eFila = eFila.siguiente
        while eColumna != None:
            actual = eColumna.acceso
            listaColumnas.append(actual)
            listaAux = []

            while actual != None:
                listaAux.append(actual)
                actual = actual.abajo

            recorridoColumnas.append(listaAux)
            eColumna = eColumna.siguiente

        for x in range(len(listaFilas)):
            filaAux = F + str(listaFilas[x].fila)
            principal += filaAux + '[label='+str(listaFilas[x].fila)+',group="1"'+']\n' #Creacion de un nodo fila

            if x < len(listaFilas)-1:
                principal += F+str(listaFilas[x].fila)+'->'+F+str(listaFilas[x+1].fila)+';\n' #Asignando hacia que fila apunta cada una
                
            aux = recorridoFilas[x] #Fila auxiliar que contiene una fila
            principal += F+str(listaFilas[x].fila)+'->'+N+str(aux[0].fila)+'_'+str(aux[0].columna)+';\n' #Asignando a cada fila su acceso
            rankAux = '{rank=same;'+filaAux+';' #Filas en horizontal
            
            for y in range(len(aux)): #recorriendo cada fila

                #principal += N + str(aux[y].fila)+'_'+str(aux[y].columna)+'[label="0",group="'+str(grupos)+'"]\n' #Creacion de los nodos
                
                if y < len(aux)-1: #Asignando la direccion de los nodos
                    principal += N + str(aux[y].fila)+'_'+str(aux[y].columna)+'->'+N+str(aux[y].fila)+'_'+str(aux[y+1].columna)+';\n'

                rankAux += N + str(aux[y].fila)+'_'+str(aux[y].columna)+';' #Poniendo las filas horizontales
            #grupos+=1
            principal += rankAux.rstrip(';')+'}\n'
        grupos=2
        rankColumnas = '{rank=same;raiz;'
        for y in range(len(listaColumnas)):
            columnaAux = C +str(listaColumnas[y].columna)
            principal += columnaAux + '[label='+str(listaColumnas[y].columna)+',group="'+str(grupos)+'"]\n'
            
            rankColumnas+=columnaAux+';'

            aux = recorridoColumnas[y] #Contiene cada columna
            principal += columnaAux+'->'+N+str(aux[0].fila)+'_'+str(aux[0].columna)+';\n'
            for x in range(len(aux)):
                principal += N + str(aux[x].fila)+'_'+str(aux[x].columna)+'[label="0",group="'+str(grupos)+'"]\n'#Creacion de los nodos
                if x < len(aux)-1:
                    principal += N + str(aux[x].fila)+'_'+str(aux[x].columna)+'->'+N+str(aux[x+1].fila)+'_'+str(aux[x].columna)+';\n'
            grupos+=1
            if y < len(listaColumnas)-1:
                principal += C+str(listaColumnas[y].columna)+'->'+C+str(listaColumnas[y+1].columna)+';\n' #Asignando hacia que fila apunta cada una
        principal += rankColumnas.rstrip(';')+'}\n'

        #raiz apunta a los principales
        principal += 'raiz->'+F+str(listaFilas[0].fila)+';\n'
        principal += 'raiz->'+C+str(listaColumnas[0].columna)+';\n'

        principal+='}\n}'
        
        nombre = ''
        nombre += r'C:\Users\Squery\Desktop\Reportes_F2\matriz' + str(self.contadorDispersa)
        
        archivo = open(nombre+'.dot','w')
        archivo.write(principal)
        archivo.close()

        system('dot -Tpng'+' '+nombre+'.dot -o'+nombre+'.png')
        #system('cd ./matriz.png')
        startfile(nombre+'.png')
        self.contadorDispersa += 1

    def listaTareas(self, listaTareas):
        g = Digraph('G', format='png', node_attr={'shape': 'box', 'height': '.1','rank':'same'}, edge_attr={ 'dir':'both'})
        g.attr(rankdir='LR')
        
        aux = listaTareas.primero
        lista = []
        contador = 0
        while aux != None:
            cad = ''
            cad += str(aux.carnet) + '\n'
            cad += aux.nombre    + '\n'
            cad += aux.descripcion + '\n'
            cad += aux.materia + '\n'
            cad += aux.fecha + '\n'
            cad += str(aux.hora) + '\n'
            cad += aux.estado + '\n'
            g.node('nodo'+str(contador), label=cad)
            lista.append('nodo'+str(contador))
            contador += 1
            aux = aux.siguiente

        for x in range(len(lista)):
            if x < len(lista)-1:
                g.edge(str(lista[x]),str(lista[x+1]))
            else:
                continue
        
        nombre = r'C:\Users\Squery\Desktop\Reportes_F2\ListaTareas'+str(self.contadorListaTareas)
        g.render(nombre)
        startfile(nombre+'.png')
        self.contadorListaTareas += 1

    def arbolB_cursosGeneral(self, arbolB_general):
        # [ ACUMULADOR, ACUMULADORE DE ENLACES, CONTADOR PAGINA, CONTADOR AUX ]
        acumulador = ["digraph G\n{\nnode[shape = record,width=.1];\n", "", 0, 0]

        if arbolB_general.raiz != None:
            cola = queue.Queue()
            cola.put(arbolB_general.raiz)

            while not(cola.empty()): # Mientras la cola no este vacia
                tmpPagina = cola.get()
                self.imprimir(tmpPagina, acumulador)
                #print(acumulador,'\n\n') #tmpPagina, 
                i = 0
                while i <= tmpPagina.cuenta:
                    if tmpPagina.ramas[i] != None:
                        cola.put(tmpPagina.ramas[i])
                    i += 1
                acumulador[2] += 1 #contador de pagina
            acumulador[0] += "\n" + acumulador[1]

        acumulador[0] += "}\n"
        #print(acumulador[0])

        nombre = r'C:\Users\Squery\Desktop\Reportes_F2\arbolPensum'+str(self.contadorArbolBGeneral)
        archivo = open(nombre+'.dot','w')
        archivo.write(acumulador[0])
        archivo.close()

        system('dot -Tsvg'+' '+nombre+'.dot -o '+nombre+'.svg')
        #system('cd ./'+nombre+'.png')
        startfile(nombre+'.svg')
        self.contadorArbolBGeneral += 1
        
    def imprimir(self, actual, acumulador):
        acumulador[0] += 'node{}[label="<r0>'.format(str(acumulador[2]))

        if actual.ramas[0] != None:
            acumulador[3] += 1 # contador auxiliar
            acumulador[1] += '"node{}":r0 -> "node{}"\n'.format(str(acumulador[2]) , str(acumulador[3]))

        i = 1
        while i <= actual.cuenta:
            acumulador[0] += '|<c{}> {} |<r{}>'.format(str(i),str(actual.claves[i].codigo)+'\\n '+str(actual.claves[i].nombre),str(i))

            if actual.ramas[i] != None:
                acumulador[3] += 1 # contador auxiliar
                acumulador[1] += '"node{}":r{} -> "node{}"\n'.format(str(acumulador[2]) ,str(i), str(acumulador[3]))
            i += 1
        acumulador[0] += '"];\n'

    def arbolB_cursosEstudiante(self, arbolB_Estudiante):
        pass