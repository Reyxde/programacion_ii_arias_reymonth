# Operadores

valor1= 22
valor2=4

suma= valor1+valor2
resta= valor1-valor2
multiplicacion= valor1*valor2
division= valor1/valor2
modulo= valor1%valor2
potencia= valor1**valor2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Potencia:", potencia)

print("-----------------------------------------------")
print("TABLA DEL 6:")
print("6 x 1 =", 6*1)
print("6 x 2 =", 6*2)
print("6 x 3 =", 6*3)
print("6 x 4 =", 6*4)
print("6 x 5 =", 6*5)
print("6 x 6 =", 6*6)
print("6 x 7 =", 6*7)
print("6 x 8 =", 6*8)
print("6 x 9 =", 6*9)
print("6 x 10 =", 6*10)
print("-----------------------------------------------")

print("El area de un triángulo de base 6 y altura 12 es de: ", (6*12)/2)
print("-----------------------------------------------")

#COMPARADORES 

velocidad1 = 550 
velocidad2= 800
print("Vuelo 01 es más rápido que Vuelo 02?", velocidad1 > velocidad2)
print("¿Vuelo 01 es más lento que Vuelo 02?", velocidad1 < velocidad2)
print("¿Vuelo 01 es igual que Vuelo 02?", velocidad1 == velocidad2)
print("¿Vuelo 01 es diferente que Vuelo 02?", velocidad1 != velocidad2)
print("¿Vuelo 01 es más rápido o igual que Vuelo 02?", velocidad1 >= velocidad2)
print("¿Vuelo 01 es más lento o igual que Vuelo 02?", velocidad1 <= velocidad2)
print("-----------------------------------------------")

#OPERADORES LOGICOS

motores = True
radar = False
combustible = 80 

print("¿Todos los sistemas están funcionando?", motores and radar)
print("¿Algunos sistemas están funcionando?", motores or radar)
print("¿Los motores no están funcionando?", not motores)
print("-----------------------------------------------")

cant_motores= 2
cant_pistas = 4
combustible= 80 


print("¿El avión tiene al menos 2 motores, 4 pistas para aterrizar y suficiente combustible?")
print(cant_motores >= 2 and cant_pistas >= 4 and combustible >= 50 )
print("-----------------------------------------------")

# Operadores de asignación

velocidad = 100
print("Velocidad inicial:", velocidad)
velocidad += 40
print("Velocidad después de acelerar:", velocidad)
velocidad -= 10
print("Velocidad después de frenar:", velocidad)
multiplicador = 2
velocidad *= multiplicador
print("Velocidad después de multiplicar:", velocidad)
divisor = 4
velocidad /= divisor
print("Velocidad después de dividir:", velocidad)
modulo = 7
velocidad %= modulo
print("Velocidad después de aplicar módulo:", velocidad)
velocidad **= 2
print("Velocidad después de aplicar potencia:", velocidad)
print("-----------------------------------------------")

#PRECEDENCIA DE OPERADORES

result = 10+5*2
print("Resultado 1: ", result)
result2 = (10+5)*2
print("Resultado 2", result2)
result3 = 10+5*2**2
print("Resultado 3", result3)
print("-----------------------------------------------")
