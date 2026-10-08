#String cadena de caracteres

jedi= "Qui-gon Jinn"
aprendiz = "Obi wan"
droide = "R2D2"
planeta = "Naboo"
codigo = "327"

print("El jedi es: " + jedi)
print("El jedi", type(jedi))
print("El aprendiz es: " + aprendiz)
print("El aprendiz", type(aprendiz))
print("El droide es: " + droide)
print("El droide", type(droide))
print("El planeta es: " + planeta)
print("El planeta", type(planeta))
print("El codigo es: " + codigo)
print("El codigo", type(codigo))


longitud_jedi = len(jedi)
print("La longitud de nombre jedi es: " + str(longitud_jedi))
longitud_aprendiz = len(aprendiz)
print("La longitud del nombre del aprendiz es: " + str(longitud_aprendiz))

mensaje = "La federación de comercio ha establecido un bloqueo en Naboo."
print("El mensaje es: " + mensaje)
mensaje_mayus = mensaje.upper()
print("El mensaje en mayúsculas es: " + mensaje_mayus)
mensaje_minus = mensaje.lower()
print("El mensaje en minúsculas es: " + mensaje_minus)

comunicado = " Los jedi son enviados a Naboo."
print("El comunicado es: " + comunicado)
nuevo_comunicado = comunicado.replace("Naboo", "Tatooine")
print("El nuevo comunicado es: " + nuevo_comunicado) 

planetas= "Naboo, Tatooine, Coruscant, ALderaan"
planetas_lista = planetas.split(",")
print(planetas_lista)
print("La lista de planeta es: " + str(planetas_lista))
print("El primer planeta es: " + planetas_lista[0])

droide = "R2-D2"
print("El droide es: " + droide)
print("El primer caracter del droife es: " + droide[0])
print("El segundo caracter del droife es: " + droide[1])
print("El tercer caracter del droife es: " + droide[2])
print("El cuarto caracter del droife es: " + droide[3])
print("El quinto caracter del droife es: " + droide[4])
print("El sexto caracter del droife es: " + droide[-1])

planeta= "     Naboo     "
print("El planeta es: " + planeta)
print("El planeta sin espacios es: " +planeta.strip())