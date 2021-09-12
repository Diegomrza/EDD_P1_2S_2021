#Nodo de Arbol B
class NodoCursos: 
    def __init__(self, orden):
        self.cuenta = 0
        self.m = orden
        self.claves = [ NodoCursos  for x in range(orden)]
        self.ramas = [NodoCursos for x in range(orden)]

        for i in range(orden):
            self.ramas [i] = None

    def pagina_llena(self):
        return self.cuenta == self.m -1

    def pagina_semillena(self):
        return self.cuenta < int(self.m/2)