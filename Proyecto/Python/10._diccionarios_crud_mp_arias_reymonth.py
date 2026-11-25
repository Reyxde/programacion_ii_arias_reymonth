vuelos = [
    {
        "id_vuelo": "100",
        "destino": "Bogotá",
        "pasajeros": 150,
        "activo": True
    },
    {
        "id_vuelo": "200",
        "destino": "Lima",
        "pasajeros": 40,
        "activo": False
    },
    {
        "id_vuelo": "300",
        "destino": "Miami",
        "pasajeros": 80,
        "activo": True
    }
]
cantidad_vuelos = len(vuelos)
print(cantidad_vuelos)
print(vuelos)

nuevo_vuelo = {
    "id_vuelo": "400",
    "destino": "Madrid",
    "pasajeros": 200,
    "activo": True
}
# CRUD
# CREATE
print("=================================")
vuelos.append(nuevo_vuelo)
print(len(vuelos))
print(vuelos)
print("=================================")
# READ | LEER CADA ELEMENTO
vuelo = vuelos[2]
print(f"Código: {vuelo['id_vuelo']}")
print(f"Destino: {vuelo['destino']}")
print(f"Pasajeros: {vuelo['pasajeros']}")
print(f"Activo: {vuelo['activo']}")
print("=================================")
# UPDATE
vuelo = vuelos[2]
vuelo["id_vuelo"] = "301"
vuelo["pasajeros"] = 85
vuelo["activo"] = False
print(f"Vuelos: {vuelos}")
print("=================================")
# DELETE: pop se usa con el número de índice
eliminado = vuelos.pop(2)
print(f"Vuelo eliminado: {eliminado}")
print(f"Vuelos: {vuelos}")