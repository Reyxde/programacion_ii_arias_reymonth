class Aeronave:
    nombre: str

    def __init__(self, nombre: str):
        self.nombre = nombre

    def presentarse(self):
        print("Aeronave en el control aéreo: ", self.nombre)

class AvionComercial(Aeronave):
    def __init__(self, nombre: str):
        super().__init__(nombre)

    def despegar(self):
        print(self.nombre, "despega rumbo a su destino")

avion = AvionComercial("Airbus A320")
avion.presentarse()
avion.despegar()

class Pista:
    nombre: str
    longitud: int

    def __init__(self, nombre: str, longitud: int):
        self.nombre = nombre
        self.longitud = longitud

    def mostrar_longitud(self):
        print("Pista: ", self.nombre)
        print("Longitud (m): ", self.longitud)

class PistaAmpliable(Pista):
    def __init__(self, nombre, longitud):
        super().__init__(nombre, longitud)

    def ampliar(self, metros: int):
        if metros > 0:
            self.longitud += metros

pista36 = PistaAmpliable("Pista 36", 3000)
print("ANTES DE AMPLIAR")
pista36.mostrar_longitud()
pista36.ampliar(500)
print("DESPUÉS DE AMPLIAR")
pista36.mostrar_longitud()