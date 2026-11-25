class Avion:
    nombre: str

    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print("Avión en el control aéreo: ", self.nombre)