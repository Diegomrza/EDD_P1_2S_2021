from Estructuras.ListaMeses import ListaMeses
from Estructuras.ListaSemestres import ListaSemestres

#from ListaMeses import ListaMeses
#from ListaSemestres import ListaSemestres

class NodoAnios: #Nodo de todos los años posibles
    def __init__(self, id):
        self.siguiente = None
        self.anterior = None

        self.id = id #Id del año Ej: 2020, 2021, 2022, etc...

        self.semestre = ListaSemestres() #Lista de semestres
        self.meses = ListaMeses() #Lista de meses