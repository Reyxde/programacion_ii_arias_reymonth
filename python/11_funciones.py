#FUNCIONES 
#FUNCIONES SIN PARAMETROS O SIMPLES
def activar_sistema():
    print("Sistema de Naboo")
    print("Sistema de control activado")

activar_sistema()

#FUNCIONES CON PARAMETROS

def saludar_jedi(nombre):
    print(f"Que la fuerza te acompañe {nombre}")

saludar_jedi("Qui-Gon Jim")
saludar_jedi("Obi-Wan Kenobi")

def mostrar_nave(nombre,combustible):
    print(f"Nave: {nombre}")
    print(f"Cantidad combustible: {combustible}")

mostrar_nave("Caza N-1", 80)

#FUNCIONES QUE DEVUELVEN DATOS O INFO
#return 

def calcular_combustible(inicial, consumo):
    restante = inicial - consumo
    return restante
def calcular_combustible2(inicial, consumo):
    
    return inicial - consumo

resultado = calcular_combustible(100,25)
print(f"Combustible: {resultado}")

resultado = calcular_combustible(100,35)
print(f"Combustible: {resultado}")

print(f"Combustible: {calcular_combustible2(100,15)}")