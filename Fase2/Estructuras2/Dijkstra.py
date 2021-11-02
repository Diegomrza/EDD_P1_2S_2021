import math
class EstadoVertice:
    def __init__(self) -> None:
        self.ultimo = 0
        self.distancia = 0.0

class Dijkstra:
    def __init__(self) -> None:
        self.INFINITO = math.inf
        self.N = 5
        self.F = [0 for i in range(self.N)]

    def minimo(self, F, D, n):
        v = 0
        mx = self.INFINITO
        j = 1
        while j < n:
            if not(F[j]) and (mx >= D[j].distancia):
                mx = D[j].distancia
                v = j
            j += 1
        return v
    
    def caminiMinimo(self,D, MatPesos, n):
        s = 0
        self.F[s] = 1
        i = 1
        while i< n:
            self.F[i] = 0
            D[i].distancia = MatPesos[0][i]
            D[i].ultimo = 0
            i+=1
        i = 1
        while i< n:
            v=self.minimo(self.F, D, n)
            self.F[v] = 1
            w = 1
            while w<n:
                if not(self.F[w]):
                    if (D[v].distancia + MatPesos[v][w]) < D[w].distancia:
                        D[w].distancia = D[v].distancia + MatPesos[v][w]
                        D[w].ultimo = v

                w += 1
            i = i+1

djk = Dijkstra()

mat = [[0,4,11,math.inf,math.inf],[math.inf,0,math.inf,6,2],[math.inf,3,0,6,math.inf],[math.inf,math.inf,math.inf,0,math.inf],[math.inf,math.inf,5,3,0]]

D = [EstadoVertice() for i in range(5)]
djk.caminiMinimo(D,mat,5)

x=23
if x == 23:
    print('yes')