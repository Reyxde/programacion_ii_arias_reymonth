flota = [
    {
        "AV-100": {
            "ruta": "Quito - Bogotá",
            "pasajeros": 150
        }
    },
    {
        "LA-200": {
            "ruta": "Quito - Lima",
            "pasajeros": 40
        }
    }
]

def create_vuelo(vuelo):
    flota.append(vuelo)

def update_vuelo(vuelo_updated, index):
    flota[index].update(vuelo_updated)

def read_vuelo(index):
    return flota[index]

def delete_vuelo(index):
    return flota.pop(index)

print(flota)
print("=================================================================")

new_vuelo = {
    "CG-300": {
        "ruta": "Quito - Miami",
        "pasajeros": 80
    }
}
create_vuelo(new_vuelo)
print(flota)
vuelo_updated = {
    "CG-301": {
        "ruta": "Quito - Madrid",
        "pasajeros": 85
    }
}
update_vuelo(vuelo_updated, 2)
print(flota)
print("=================================================================")
print(read_vuelo(2))
print("=================================================================")
print(delete_vuelo(2))
print("=================================================================")
print(flota)