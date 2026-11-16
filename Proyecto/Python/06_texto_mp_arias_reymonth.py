#String cadena de caracteres

piloto= "Rey Arias"
copiloto = "Bengy Ortiz"
destino = "Bogotá"

print("El piloto es: " + piloto)
print("El piloto", type(piloto))
print("El copiloto es: " + copiloto)
print("El copiloto", type(copiloto))
print("El destino es: " + destino)
print("El destino", type(destino))


longitud_piloto = len(piloto)
print("La longitud de nombre piloto es: " + str(longitud_piloto))
longitud_copiloto = len(copiloto)
print("La longitud del nombre del copiloto es: " + str(longitud_copiloto))

mensaje = "El vuelo 01 con destino a Bogotá ha sufrido un retraso."
print("El mensaje es: " + mensaje)
mensaje_mayus = mensaje.upper()
print("El mensaje en mayúsculas es: " + mensaje_mayus)
mensaje_minus = mensaje.lower()
print("El mensaje en minúsculas es: " + mensaje_minus)

comunicado = " Los piloto son enviados a una capacitación antes del vuelo 01."
print("El comunicado es: " + comunicado)
nuevo_comunicado = comunicado.replace("01", "02")
print("El nuevo comunicado es: " + nuevo_comunicado) 

destinos= "Ecuador, Bogotá, Argentina, Italia"
destinos_lista = destinos.split(",")
print(destinos_lista)
print("La lista de destinos es: " + str(destinos_lista))
print("El primer destino es: " + destinos_lista[0])

destino = "Ecuador"
print("El destino es: " + destino)
print("El primer caracter del destino es: " + destino[0])
print("El segundo caracter del destino es: " + destino[1])
print("El tercer caracter del destino es: " + destino[2])
print("El cuarto caracter del destino es: " + destino[3])
print("El quinto caracter del destino es: " + destino[4])
print("El quinto caracter del destino es: " + destino[5])
print("El sexto caracter del destino es: " + destino[-1])

destino= "     Alemania     "
print("El planeta es: " + destino)
print("El planeta sin espacios es: " +destino.strip())