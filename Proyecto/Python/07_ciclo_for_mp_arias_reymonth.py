#Ciclo for

destinos= [
    "Ecuador",
    "Colombia",
    "Argentina"
]

for destino in destinos:
    print("Seleccionando destino: ", destino)

print("Destino seleccionado")

rondas= range(1,6)

print("Tipo de rondas", type(rondas))
for ronda in rondas:
    print(f"Ronda de vigilancia: {ronda}")
    print(f"Tipo de dato ronda: {type(ronda)}")

#va de 3 en 3
vuelo= range(1,17,3)

print("Vuelo", type(vuelo))
for id_vuelo in vuelo:
    print(f"Seguimiento : Vuelo-{id_vuelo}")
    print(f"Tipo de dato id_vuelo: {type(id_vuelo)}")


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

registro = {}
print(registro)
vuelo_pendiente = {
    "piloto": "Juan Perez",
    "id_vuelo" : "20",
    "destino" : "Cuenca",
    "combustible": 100
    
}
print(vuelo_pendiente)

vuelo_pendiente["piloto"] = "Luck Skywalker"
vuelo_pendiente["id_vuelo"] = 50
print(registro)

for clave, valor in vuelo_pendiente.items():
    print(f"{clave} - {valor}")