import hashlib

class nodoMerkle: #Hojas del arbol
    def __init__(self):
        self.izquierda = arbol()
        self.derecha = arbol()
        self.id = None #Hash

class arbol:
    def __init__(self):
        self.rootHash = None

class merkleTree:
    def __init__(self, lista):
        self.hojas = self.parOimpar(lista)
        self.niveles = []
        self.hashes = [] #hashes o nodos
        self.root = None
    
    def parOimpar(self, lista):
        if len(lista)%2 != 0:
            lista.append(-1)
        return lista

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
                raiz = self.hashes[k] + self.hashes[k+1]
                converse = hashlib.sha256(raiz.encode())
                self.niveles.append(converse.hexdigest())
                #self.hashes = self.niveles
                k += 2
            
            aux = self.niveles.copy()
            self.hashes = aux.copy()
            if len(self.niveles) != 1:
                self.niveles.clear()
                
        self.root = self.niveles[0]


    def hashing(self):
        while len(self.niveles) != 1:
            k = 0
            while k < len(self.hashes):
                #raiz = self.hashes[k] + self.hashes[k+1]
                arbol = nodoMerkle()
                arbol.izquierda = self.hashes[k].id
                arbol.derecha = self.hashes[k+1].id
                converse = hashlib.sha256(arbol.id.encode())
                arbol.id = converse.hexdigest()
                self.niveles.append(arbol)

                #self.hashes = self.niveles
                k += 2
             
            self.hashes = self.niveles


arbol = merkleTree(['1','2','3','4','5','6','7'])
arbol.crear()
print('Raíz: ',arbol.root)