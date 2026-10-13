droides = [
    {
    "codigo": "B1",
    "modelo": "B1",
    "energia": 90,
    "activo": True
    },
    {
        "codigo": "B1-002",
        "modelo": "B1",
        "energia": 40,
        "activo": False
        },
    {
        "codigo": "DRO-001",
        "modelo": "Droiketa",
        "energia": 80,
        "activo": True  
    }
]
cantidad_droides = len(droides)
print(cantidad_droides)
print(droides)

nuevo_droide= {
    "codigo": "B1-004",
    "modelo": "B1",
    "energia" : 100,
    "activo" : True
}
#CRUD
#CREATE
print("=================================")
droides.append(nuevo_droide)
print(len(droides))
print(droides)
print("=================================")
#READ| LEER CADA ELEMENTO
droide = droides[2]
print(f"Codigo: {droide["codigo"]}")
print(f"Modelo: {droide["modelo"]}")
print(f"Energía: {droide["energia"]}")
print(f"Activo: {droide["activo"]}")
print("=================================")
#UPDATE
droide = droides[2]
droide["codigo"]="DRO-002"
droide["energia"]=85
droide["activo"]= False
print(f"droides: {droides}")
print("=================================")
#DELETE pop se usa con el numero de indice
eliminado= droides.pop(2)
print(f"Droides: {droides}")
