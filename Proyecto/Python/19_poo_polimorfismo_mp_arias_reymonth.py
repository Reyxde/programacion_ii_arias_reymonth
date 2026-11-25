class Aeronave:
    nombre: str
    velocidad_base: int
    horas: int

    def __init__(self, nombre: str, velocidad_base: int, horas: int):
        self.nombre = nombre
        self.velocidad_base = velocidad_base
        self.horas = horas

    def aterrizar(self):
        print(f"{self.nombre} realiza un aterrizaje")

    def calcular_distancia(self):
        return self.velocidad_base

class Avion(Aeronave):
    def __init__(self, nombre: str, velocidad_base: int, horas: int):
        super().__init__(nombre, velocidad_base, horas)

    def aterrizar(self):
        print(self.nombre, "aterriza en la pista principal")

    def calcular_distancia(self):
        return self.velocidad_base * self.horas


class Helicoptero(Aeronave):
    def __init__(self, nombre: str, velocidad_base: int, horas: int):
        super().__init__(nombre, velocidad_base, horas)

    def aterrizar(self):
        print(self.nombre, "aterriza en el helipuerto")

    def calcular_distancia(self):
        return self.velocidad_base * self.horas // 2


avion = Avion("Airbus A320", 800, 3)
helicoptero = Helicoptero("Helicóptero de rescate", 250, 2)

avion.aterrizar()
helicoptero.aterrizar()
print(avion.calcular_distancia())
print(helicoptero.calcular_distancia())