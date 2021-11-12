import hashlib

class nodoMerkle: #Hojas del arbol
    def __init__(self, izq, der, hash):
        self.izquierda = izq
        self.derecha = der
        self.hash = hash #Hash

class merkleTree:
    def __init__(self):
        #self.hojas = self.parOimpar(lista)
        self.niveles = []
        self.hashes = [] #hashes o nodos
        self.root = None

    def parOimpar(self, lista):
        if len(lista)%2 != 0:
            lista.append(nodoMerkle(None, None, self.crearHash(-1)))
        return lista

    def crearHash(self, dato):
        if type(dato) != str:
            dato = str(dato)
        return hashlib.sha256(dato.encode()).hexdigest()

    def crear(self):
        for x in self.hojas:
            if type(x) != str:
                x = str(x)
            #x = str(x)
            h = hashlib.sha256(x.encode())
            self.hashes.append(h.hexdigest())
        
        while len(self.niveles) != 1:
            k = 0
            while k < len(self.hashes):
                if len(self.hashes)%2 == 0:
                    raiz = self.hashes[k] + self.hashes[k+1]
                else:
                    raiz = self.hashes[k]
                converse = hashlib.sha256(raiz.encode())
                self.niveles.append(converse.hexdigest())
                #self.hashes = self.niveles
                k += 2
            
            aux = self.niveles.copy()
            self.hashes = aux.copy()
            if len(self.niveles) != 1:
                self.niveles.clear()
                
        self.root = self.niveles[0]

    def hashing(self, lista):
        lista = self.parOimpar(lista)
        aux = []

        while len(lista) != 1:
            i = 0
            tamanio = len(lista)
            while i < tamanio:
                izq = lista[i]
                der = None
                if (i+1) < tamanio:
                    der = lista[i+1]
                else:
                    der = nodoMerkle(None, None, izq.hash)
                
                hashPrincipal = self.crearHash(izq.hash + der.hash)
                aux.append(nodoMerkle(izq, der, hashPrincipal))
                i += 2
            lista = aux
            aux = []
        self.root = lista[0]

    def limpiarArbol(self):
        self.root = None
        self.hashes.clear()
        self.niveles.clear()
        
'''def crearHash(dato):
    if type(dato) != str:
        dato = str(dato)
    return hashlib.sha256(dato.encode()).hexdigest()

lista = []
for x in range(7):
    arbolAux = merkleTree()
    nuevo = nodoMerkle(None, None, crearHash(x+1))
    lista.append(nuevo)

arbol = merkleTree()
#arbol.crear()
arbol.hashing(lista)
print('Raíz: ',vars(arbol.root))'''