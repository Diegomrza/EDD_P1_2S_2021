class NodoTarea:
    def __init__(self, carnet, nombre, descripcion, materia, fecha, hora, estado):
        self.carnet = carnet
        self.nombre = nombre
        self.descripcion = descripcion
        self.materia = materia
        self.fecha = fecha
        self.hora = hora
        self.estado = estado

        self.pos = 0
        self.siguiente = None