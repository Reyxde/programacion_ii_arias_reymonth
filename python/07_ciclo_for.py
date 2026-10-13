#Ciclo for

naves= [
    "Caza N-1",
    "Nave real de Naboo",
    "Transporte"
]

for nave in naves:
    print("Inspeccionando ", nave)

print("Inspección realizada")

rondas= range(1,6)

print("Tipo de rondas", type(rondas))
for ronda in rondas:
    print(f"Ronda de vigilancia: {ronda}")
    print(f"Tipo de dato ronda: {type(ronda)}")

#va de 3 en 3
droides= range(1,17,3)

print("Tipo de Droides", type(droides))
for droide in droides:
    print(f"Reparar : droide B1-{droide}")
    print(f"Tipo de dato droide: {type(droide)}")

planetas = [
    "naboo",
    "Tatooine",
    "Coruscant"
]

recorrido= enumerate(planetas, start=1)

for posicion, planeta in recorrido:
    print(f"Destino {posicion}: {planeta}")
    print(f"TIpos de dato {type(posicion)}: {type(planeta)}")

#Continue omite la interacción y continua | break rompe el ciclo
paises = [
    "Ecuador",
    "Venezuela",
    "Chile",
    "Colombia",
    "Brasil",
    "Estados Unidos"
]

for pais in paises:
    if pais== "Chile":
        continue
    if pais=="Brasil":
        break
    print(f"País visitado: {pais}")

jedi = {}
print(jedi)
jedi_activo = {
    "nombre": "Obiwan",
    "fuerza" : "120",
    "estilo_pelea" : "Samurai",
    "misiones" : ["guerra alderan", "secuestro palpatine", "escolta de leia"],
    "descripcion": {
        "estatura": 1.80,
        "especie": "humana"
    }
}
print(jedi_activo)
nave= dict(nombre= "AZ-1", capacidad= 8, turbo_laser=2)
print(nave)

jedi["nombre"] = "Luck"
jedi["fuerza"] = 150
print(jedi)

for clave, valor in jedi_activo.items():
    print(f"{clave} - {valor}")