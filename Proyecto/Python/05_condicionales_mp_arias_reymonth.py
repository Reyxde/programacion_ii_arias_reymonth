#Condicional if
#Simple

combustible = 20
if combustible >= 20:
    print("Puedes despegar")

#Condicional if-else
pasajeros= int(input("Ingresa la cantidad de pasajeros en el vuelo: "))
asientos = int(input("Ingresa la cantidad de asientos disponibles: "))

if pasajeros <= asientos:
    print("Puedes realizar el vuelo")
else:
    print("No hay suficientes asientos para el vuelo")


#if anidado

if pasajeros <= asientos:
    print("Puedes volar el avión")
    if pasajeros > asientos:
        print("No tienes espacios disponibles")
    else:
        print("Puedes volar y aún tienes espacio")
else:
    print("La cantidad de pasajeros debe ser menor o igual que la cantidad de asientos disponibles")

# Condicional if-elif-else
if asientos > pasajeros :
    print("Puedes volar y te sobran asientos")
elif pasajeros == asientos:
    print("Puedes despegar pero no hay más asientos disponibles")
else:
    print("No tienes suficientes asientos para la cantidad de pasajeros")

tipo_vuelo = input("Ingresa el tipo de vuelo (nacional, internacional, carga): ")
if tipo_vuelo == "nacional":
    print("El vuelo es nacional")
elif tipo_vuelo == "internacional":
    print("El vuelo es internacional")
elif tipo_vuelo == "carga":
    print("El vuelo es de carga")
else:
    print("Tipo de vuelo no válido")


