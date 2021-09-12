from Nodos.NodoMeses import NodoMeses

class ListaMeses:
    def __init__(self):
        self.primero = None
        self.contador_meses = 0

    def insertar(self, mes):
        if (mes >= 1 and mes <= 12) and self.contador_meses < 13: 
            nuevo = NodoMeses(mes)
            if self.primero == None:
                self.primero = nuevo
                self.contador_meses += 1
            elif mes < self.primero.mes:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
                self.contador_meses += 1
            else:
                temp = self.primero
                while temp.siguiente != None:
                    if mes == temp.mes:
                        print('El valor ya existe')
                        break
                    elif mes < temp.siguiente.mes:
                        nuevo.siguiente = temp.siguiente
                        temp.siguiente.anterior = nuevo
                        nuevo.anterior = temp
                        temp.siguiente = nuevo
                        self.contador_meses += 1
                        break
                    
                    temp = temp.siguiente
                if temp.siguiente == None: #self.repetidos(mes) != True and 
                    temp.siguiente = nuevo
                    nuevo.anterior = temp
                    self.contador_meses += 1
        else:
            print('El mes está fuera de rango')

    def modificar(self, id):
        aux = self.primero
        while aux != None:
            if id == aux.mes:
                print('Aqui realizar los cambios')
            aux = aux.siguiente

    def eliminar(self, id):
        aux = self.primero
        while aux != None:
            if id == aux.mes:
                if id == self.primero.mes:
                    aux.siguiente.anterior = None
                    self.primero = aux.siguiente
                    aux.siguiente = None
                    break
                elif aux.siguiente == None:
                    aux.anterior.siguiente = None
                    aux.anterior = None
                    break
                else:
                    aux.anterior.siguiente = aux.siguiente
                    aux.siguiente.anterior = aux.anterior
                    break
            aux = aux.siguiente

    def mostrar(self):
        temp = self.primero
        print('Contador meses: ',self.contador_meses)
        while temp != None:
            print('Mes: ',temp.mes)
            temp = temp.siguiente
        print('\n')
