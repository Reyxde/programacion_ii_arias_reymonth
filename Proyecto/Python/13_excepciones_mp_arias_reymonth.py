print("======== CONTROL DE COMBUSTIBLE =========")
combustible_texto = "ochenta"
try:
    combustible = int(combustible_texto)
    print(combustible)
except ValueError:
    print("Error: debe ser numérico")

print("FIN DEL SISTEMA")


def calcular_consumo(total, horas):
    try:
        resultado = total / horas
        return resultado
    except ZeroDivisionError as error:
        print("Error: división entre cero", error)
        return None
    except TypeError:
        print("Error: valores deben ser numéricos")
        return None

print("Caso 1:", calcular_consumo(100, 4))
print("Caso 2:", calcular_consumo(100, 0))
print("Caso 3:", calcular_consumo(100, "cuatro"))


print("=========== DIAGNÓSTICO DEL RADAR ============")
try:
    senal = int(90)
    print("señal", senal)
except ValueError:
    print("error de lectura")
else:
    print("diagnóstico completado")
finally:
    print("Cerrando diagnóstico")

print("=========== DIAGNÓSTICO DEL RADAR ============")
try:
    senal = int("cuatro")
    print("señal", senal)
except ValueError:
    print("error de lectura")
else:
    print("diagnóstico completado")
finally:
    print("Cerrando diagnóstico")

print("===============================================================")

def validar_altitud(altitud):
    if type(altitud) is not int:
        raise TypeError("La altitud debe ser un número entero")
    if altitud < 0 or altitud > 45000:
        raise ValueError("La altitud debe estar entre 0 y 45000 pies")
    return altitud

try:
    resultado = validar_altitud(35000)
    print("Altitud", resultado)
except (TypeError, ValueError) as error:
    print("Error", error)

try:
    resultado = validar_altitud("alta")
    print("Altitud", resultado)
except (TypeError, ValueError) as error:
    print("Error", error)

try:
    resultado = validar_altitud(60000)
    print("Altitud", resultado)
except (TypeError, ValueError) as error:
    print("Error", error)