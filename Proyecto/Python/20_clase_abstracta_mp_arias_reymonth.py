from abc import ABC, abstractmethod

class Aeronave(ABC):
    modelo: str

    def __init__(self, modelo: str):
        self.modelo = modelo

    @abstractmethod
    def despegar(self):
        pass

class AvionComercial(Aeronave):
    modelo: str

    def __init__(self, modelo: str):
        super().__init__(modelo)

    def despegar(self):
        print(self.modelo, "despega por la pista principal con autorización de la torre")

class Helicoptero(Aeronave):
    def __init__(self, modelo):
        super().__init__(modelo)

    def despegar(self):
        print(self.modelo, "despega verticalmente desde el helipuerto")

avion = AvionComercial("Modelo 837")
heli = Helicoptero("Helicóptero de rescate")
avion.despegar()
heli.despegar()