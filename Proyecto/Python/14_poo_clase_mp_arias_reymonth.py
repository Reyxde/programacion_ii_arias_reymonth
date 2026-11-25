class Vuelo:
    codigo: str
    pasajeros: int

    def __init__(self, codigo: str, pasajeros: int):
        self.codigo = codigo
        self.pasajeros = pasajeros

    def anunciar(self):
        print("Atención, vuelo: ", self.codigo)

    def abordar(self):
        abordaje = 20
        self.pasajeros += abordaje

    def calcular_ingresos(self, tarifa):
        ingresos = self.pasajeros * tarifa
        print("Vuelo", self.codigo)
        print("Ingresos generados: ", ingresos)

vuelo = Vuelo("AV100", 100)

vuelo.anunciar()

print("Código del vuelo: ", vuelo.codigo)
print("Pasajeros del vuelo: ", vuelo.pasajeros)
vuelo.abordar()
print("Pasajeros del vuelo: ", vuelo.pasajeros)
vuelo.calcular_ingresos(150)