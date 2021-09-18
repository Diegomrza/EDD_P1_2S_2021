class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, nuevo):
        self.items.append(nuevo)
        #print(self.items)
    
    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError('La cola está vacía')

    def es_vacia(self):
        if len(self.items) == 0:
            return True
        else:
            return False