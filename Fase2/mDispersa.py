from Estructuras.Dispersa import Dispersa
from Estructuras.ListaTareas import ListaTareas
from Estructuras.grafo import grafo

class mDispersa:
    def __init__(self):
        self.contador = 0
    
    def graficar(self, matriz):
        #matrizAux = Dispersa()
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
            principal += filaAux + '[label='+str(listaFilas[x].fila)+'group="1"'+']\n' #Creacion de un nodo fila

            if x < len(listaFilas)-1:
                principal += F+str(listaFilas[x].fila)+'->'+F+str(listaFilas[x+1].fila)+';\n' #Asignando hacia que fila apunta cada una
                
            aux = recorridoFilas[x] #Fila auxiliar que contiene una fila
            principal += F+str(listaFilas[x].fila)+'->'+N+str(aux[0].fila)+'_'+str(aux[0].columna)+';\n'
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

        for i in range(len(recorridoColumnas)):
            aux = recorridoColumnas[i]
            for j in aux:
                print(j.celdas.contadorTareas)

        principal+='}\n}'
        print(principal)

matriz = Dispersa()

matriz.insertar(1,1,ListaTareas())
matriz.insertar(2,2,ListaTareas())
matriz.insertar(1,13,ListaTareas())
matriz.insertar(13,2,ListaTareas())
matriz.insertar(4,5,ListaTareas())
matriz.insertar(5,3,ListaTareas())
matriz.insertar(3,8,ListaTareas())
matriz.insertar(8,3,ListaTareas())
matriz.insertar(9,10,ListaTareas())
matriz.insertar(10,1,ListaTareas())
matriz.insertar(5,10,ListaTareas())
matriz.insertar(13,13,ListaTareas())
matriz.insertar(10,10,ListaTareas())

g = grafo()
g.matrizDispersa(matriz)


g = mDispersa()
g.graficar(matriz)
'''
digraph g{
node[shape=box]
subgraph h{
label="Matriz dispersa"
raiz[label="0,0"]
edge[dir="both"]

Fila1[label="1", group=1];
Fila1->Fila2;
Fila2[label="2", group=1];
Columna1[label="1", group=2];
Columna1->Columna2;
Columna2[label="2", group=3];
Columna2->Columna3;
Columna3[label="3", group=4];
Columna3->Columna4;
Columna4[label="4", group=5];
Columna4->Columna5;
Columna5[label="5", group=6];
Columna5->Columna6;
Columna6[label="6", group=7];
Columna6->Columna7;
Columna7[label="7", group=8];
Columna7->Columna8;
Columna8[label="8", group=9];
Columna8->Columna9;
Columna9[label="9", group=10];
Columna9->Columna10;
Columna10[label="10", group=11];

raiz->Fila1;
raiz->Columna1;

{rank=same;raiz;Columna1;Columna2;Columna3;Columna4;Columna5;Columna6;Columna7;Columna8;Columna9;Columna10}

nodo1_1[label="0", group=2]
nodo2_1[label="0", group=2]
nodo1_2[label="0", group=3]
nodo2_2[label="0", group=3]
nodo1_3[label="0", group=4]
nodo2_3[label="0", group=4]
nodo1_4[label="0", group=5]
nodo2_4[label="0", group=5]
nodo1_5[label="0", group=6]
nodo2_5[label="0", group=6]
nodo1_6[label="0", group=7]
nodo2_6[label="0", group=7]
nodo1_7[label="0", group=8]
nodo2_7[label="0", group=8]
nodo1_8[label="0", group=9]
nodo2_8[label="0", group=9]
nodo1_9[label="0", group=10]
nodo2_9[label="0", group=10]
nodo1_10[label="0", group=11]
nodo2_10[label="0", group=11]

Fila1->nodo1_1;
Fila2->nodo2_1;

{rank=same;Fila1;nodo1_1;nodo1_2;nodo1_3;nodo1_4;nodo1_5;nodo1_6;nodo1_7;nodo1_8;nodo1_9;nodo1_10}
{rank=same;Fila2;nodo2_1;nodo2_2;nodo2_3;nodo2_4;nodo2_5;nodo2_6;nodo2_7;nodo2_8;nodo2_9;nodo2_10}

Columna1->nodo1_1;
Columna2->nodo1_2;
Columna3->nodo1_3;
Columna4->nodo1_4;
Columna5->nodo1_5;
Columna6->nodo1_6;
Columna7->nodo1_7;
Columna8->nodo1_8;
Columna9->nodo1_9;
Columna10->nodo1_10;
nodo1_1->nodo1_2;
nodo1_2->nodo1_3;
nodo1_3->nodo1_4;
nodo1_4->nodo1_5;
nodo1_5->nodo1_6;
nodo1_6->nodo1_7;
nodo1_7->nodo1_8;
nodo1_8->nodo1_9;
nodo1_9->nodo1_10;
nodo2_1->nodo2_2;
nodo2_2->nodo2_3;
nodo2_3->nodo2_4;
nodo2_4->nodo2_5;
nodo2_5->nodo2_6;
nodo2_6->nodo2_7;
nodo2_7->nodo2_8;
nodo2_8->nodo2_9;
nodo2_9->nodo2_10;
nodo1_1->nodo2_1;
nodo1_2->nodo2_2;
nodo1_3->nodo2_3;
nodo1_4->nodo2_4;
nodo1_5->nodo2_5;
nodo1_6->nodo2_6;
nodo1_7->nodo2_7;
nodo1_8->nodo2_8;
nodo1_9->nodo2_9;
nodo1_10->nodo2_10;
}
}

'''