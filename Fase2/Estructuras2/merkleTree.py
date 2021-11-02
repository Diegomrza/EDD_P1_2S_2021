import hashlib

class nodoMerkle: #Hojas del arbol
    def __init__(self):
        self.izquierda = None
        self.derecha = None
        self.id = None

class merkleTree:
    def __init__(self, lista):
        self.root = None
        self.hojas = self.parOimpar(lista)
        self.hashes = [nodoMerkle for x in range(len(lista))]

        self.niveles = [nodoMerkle for x in range(len(self.parOimpar(lista))/2)]
    
    def parOimpar(self, lista):
        if len(lista)%2 != 0:
            lista.append(-1)
        return lista

    def crear(self):

        while self.niveles != 1:
            k = 0
            while k < len(self.niveles):
                print()    
            x = str(x)
            h = hashlib.sha256(x.encode())

        '''for x in lista:
            x = str(x)
            h = hashlib.sha256(x.encode())
            self.hojas.append(h.hexdigest())'''



arbol = merkleTree([1,2,3,4,5,6,7])
arbol.crear()

'''print('Hashes:')
for x in arbol.hojas:
    print('-',x)'''