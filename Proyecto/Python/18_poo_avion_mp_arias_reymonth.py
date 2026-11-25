from Python.poo_avion_mp_arias_reymonth import Avion

class AvionComercial(Avion):
    def __init__(self, nombre: str):
        super().__init__(nombre)

    def despegar(self):
        print(self.nombre, "despega rumbo a su destino")

avion = AvionComercial("Modelo 737")
avion.presentarse()
avion.despegar()