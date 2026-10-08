
peso_paquete= float(input("Ingrese el peso (kg) del paquete: "))
destino = int(input("Ingrese la zona de destino 1. America 2.Europa 3. Resto del mundo: "))

if destino == 1:   
    print("El costo de su paquete es de: ", peso_paquete*5)
elif destino == 2:
        print("El costo de su paquete es de: ", peso_paquete*7.5)
elif destino == 3:
          print("El costo de su paquete es de: ", peso_paquete*10)
else:
       print("El destino no está disponible")


