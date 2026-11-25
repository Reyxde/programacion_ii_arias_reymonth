class Vuelo:
    codigo: str
    __pasajeros: int

    def __init__(self, codigo: str, pasajeros: int):
        self.codigo = codigo
        self.__pasajeros = pasajeros

    def get_pasajeros(self):
        return self.__pasajeros


vuelo = Vuelo("AV100", 150)
print("Vuelo: ", vuelo.codigo)
print("Pasajeros: ", vuelo.get_pasajeros())

class CuentaAerolinea:
    titular: str
    __saldo: int

    def __init__(self, titular: str, saldo: int):
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def pagar_tasa(self, cantidad: int):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print("Pago de tasa realizado ", cantidad)
        else:
            print("Pago no permitido ")

cuenta = CuentaAerolinea("LATFLY", 5000)
print("Titular:", cuenta.titular)
print("Saldo inicial: ", cuenta.get_saldo())
cuenta.pagar_tasa(500)
print("Saldo final: ", cuenta.get_saldo())

