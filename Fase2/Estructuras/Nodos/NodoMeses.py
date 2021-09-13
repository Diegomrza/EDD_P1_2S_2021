from Estructuras.Dispersa import Dispersa

class NodoMeses: #Nodo de los doce meses posibles en un año
    def __init__(self, mes):
        self.actividades = Dispersa() #Matriz dispersa
        
        self.mes = mes # del 1 al 12

        self.siguiente = None
        self.anterior = None