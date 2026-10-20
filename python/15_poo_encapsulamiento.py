class Guerrero:
    nombre : str 
    __poder : int

    def __init__(self, nombre : str , poder : int):
        self.nombre = nombre
        self.__poder = poder 

    def get_poder(self):
        return self.__poder


vegeta = Guerrero("vegeta", 8000)
print("Guerrero: ", vegeta.nombre)
print("Poder: ", vegeta.get_poder())

class CuentaZeni:
    titular : str
    __saldo : int

    def __init__(self, titular : str , saldo : int):
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def retirar_dinero(self, cantidad :  int):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print("Retiro realizado ", cantidad)
        else: 
            print("Retiro no permitido ")

cuenta = CuentaZeni("Mr. Satán",5000)
print("Titular:", cuenta.titular)
print("Saldo inicial: ", cuenta.get_saldo())
cuenta.retirar_dinero(500)
print("Saldo final: ", cuenta.get_saldo())


print("=====================================================")
print("                      TAREA")

class AlmacenSemillas:
    __cantidad : int

    def __init__(self,cantidad: int):
        self.__cantidad = cantidad
    def get_cantidad(self):
        return self.__cantidad
    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
    def entregar_semillas(self, cantidad):
        if cantidad <= self.__cantidad:
            self.__cantidad -= cantidad
            print(f"Se entregaron {cantidad} semillas con éxito.")
        else:
            print("No hay suficientes semillas.")

almacen= AlmacenSemillas(10)
print("GOKU")
almacen.entregar_semillas(3)
print("YAJIROBE")
almacen.entregar_semillas(9)

print(f"La cantidad final de semillas es de: {almacen.get_cantidad()}")