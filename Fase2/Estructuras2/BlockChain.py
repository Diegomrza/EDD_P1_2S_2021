import hashlib, datetime
import os
import errno

try:
    os.mkdir(r'C:\Users\Squery\Desktop\Bloques')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

class Block:
    def __init__(self, indice, hashAnterior, merkleROOT): #, info
        self.indice = indice
        self.hashAnterior = hashAnterior
        #self.info = info
        self.nonce = 0
        self.fecha = str(datetime.datetime.now().day)+'/'+str(datetime.datetime.now().month)+'/'+str(datetime.datetime.now().year)
        self.merkleROOT = merkleROOT
        self.hash = self.crearHash()
        
    def crearHash(self):
        return hashlib.sha256((str(self.indice)+self.hashAnterior+str(self.fecha)+str(self.nonce)+self.merkleROOT).encode()).hexdigest() #self.info+
    
    def minar(self, dificultad):
        while not (self.hash.startswith(dificultad)):
            self.nonce += 1
            self.hash = self.crearHash() 

class BlockChain:
    def __init__(self):
        self.contadorBloques = 1
        self.dificultad = '00'
        self.chain = [self.setPrimerBloque()]

    def setPrimerBloque(self):
        nuevo = Block(0,'00','00')
        nuevo.minar(self.dificultad)

        archivo = open(r'C:\Users\Squery\Desktop\Bloques\\'+str(nuevo.indice)+'.txt', 'w')
        
        contenido = '{\n'
        contenido += '\t"indice":"'+str(nuevo.indice)+'",\n'; contenido += '\t"hashAnterior":"'+nuevo.hashAnterior+'",\n'
        contenido += '\t"nonce":"'+str(nuevo.nonce)+'",\n'; contenido += '\t"fecha":"'+nuevo.fecha+'",\n'
        contenido += '\t"merkleRoot":"'+nuevo.merkleROOT+'",\n'; contenido += '\t"hash"":'+nuevo.hash+'"\n'
        contenido += '}'

        archivo.write(contenido)
        archivo.close()
        return nuevo
        
    def getUltimoBloque(self):
        return self.chain[len(self.chain)-1]
    
    def addBloque(self, merkleROOT):
        anterior = self.getUltimoBloque()
        nuevoBloque = Block(self.contadorBloques, anterior.hash, merkleROOT) #Creacion del nuevo bloque
        nuevoBloque.minar(self.dificultad) #Minado de bloques
        self.chain.append(nuevoBloque)
        self.contadorBloques += 1

        archivo = open(r'C:\Users\Squery\Desktop\Bloques\\'+str(nuevoBloque.indice)+'.txt', 'w')
        
        contenido = '{\n'
        contenido += '\t"indice":"'+str(nuevoBloque.indice)+'",\n'; contenido += '\t"hashAnterior":"'+nuevoBloque.hashAnterior+'",\n'
        contenido += '\t"nonce":"'+str(nuevoBloque.nonce)+'",\n'; contenido += '\t"fecha":"'+nuevoBloque.fecha+'",\n'
        contenido += '\t"merkleRoot":"'+nuevoBloque.merkleROOT+'",\n'; contenido += '\t"hash"":'+nuevoBloque.hash+'"\n'
        contenido += '}'

        archivo.write(contenido)
        archivo.close()


EDDCoin = BlockChain()
for x in range(5):
    EDDCoin.addBloque('Diego'+str(x))

for y in EDDCoin.chain:
    print(vars(y))
    print()