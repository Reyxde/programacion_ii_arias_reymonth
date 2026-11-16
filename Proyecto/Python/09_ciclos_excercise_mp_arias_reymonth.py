control_vuelo = [
    {
        "idv_vuelo" : "01",
        "combustible" : 80,
        "equipo" : ["Capitan Lopez", "Copiloto Martines", "Azafata Jimenez"] 

    },
    {
        "idv_vuelo" : "03",
        "combustible" : 35,
        "equipo" : ["Capitan Ibarra", "Azafata Hernandez"] 
    },
    {
        "idv_vuelo" : "04",
        "combustible" : 65,
        "equipo" : ["Capitan Heredia"] 
    }
]


vuelos_listos = 0
vuelos_recarga = 0
total_tripulantes = 0
total_ciclos = 0

for numero, vuelo in enumerate(control_vuelo, start=1):
    print(f"--- Vuelo : {numero} - {vuelo}")
    if vuelo["combustible"] >= 50:
        print("Estado Inicial: LISTO")
        vuelos_listos += 1
    else:
        print("Estado Inicial: RECARGAR")
        vuelos_recarga += 1
        ciclo = 0
        while vuelo["combustible"] < 50:
            ciclo += 1
            vuelo["combustible"] += 10
        total_ciclos += ciclo
        print("Recarga completada")
        print("Estado Final: LISTO")
    total_tripulantes += len(vuelo["equipo"])
    for tripulante in vuelo["equipo"]:
        print(f"Tripulante: {tripulante}")

print("=====================================")
print("              RESUMEN                ")
print("=====================================")
print(f"Total vuelos: {len(control_vuelo)}")
print(f"Vuelos listos inicialmente: {vuelos_listos}")
print(f"Total recargados: {vuelos_recarga}")
print(f"Total tripulantes: {total_tripulantes}")
print(f"Total ciclos: {total_ciclos}")