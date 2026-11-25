# FUNCIONES
# FUNCIONES SIN PARÁMETROS O SIMPLES
def activar_sistema():
    print("Sistema de Control de Vuelos")
    print("Sistema de radar activado")

activar_sistema()

# FUNCIONES CON PARÁMETROS

def saludar_piloto(nombre):
    print(f"Torre de control saluda al capitán {nombre}")

saludar_piloto("Ramírez")
saludar_piloto("Herrera")

def mostrar_vuelo(codigo, combustible):
    print(f"Vuelo: {codigo}")
    print(f"Cantidad de combustible: {combustible}")

mostrar_vuelo("AV100", 80)


def calcular_combustible(inicial, consumo):
    restante = inicial - consumo
    return restante

def calcular_combustible2(inicial, consumo):
    return inicial - consumo

resultado = calcular_combustible(100, 25)
print(f"Combustible: {resultado}")

resultado = calcular_combustible(100, 35)
print(f"Combustible: {resultado}")

print(f"Combustible: {calcular_combustible2(100, 15)}")

def vuelo_preparado(combustible):
    return combustible >= 50

if vuelo_preparado(80):
    print("Vuelo autorizado para despegar")
else:
    print("Vuelo necesita recarga")