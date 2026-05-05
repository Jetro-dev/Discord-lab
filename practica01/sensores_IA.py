def leer_temperaturas():
    temperaturas = []
    for i in range(8):
        valor = float(input(f"Lectura {i+1}: "))
        temperaturas.append(valor)
    return temperaturas


def filtrar_datos(temperaturas):
    contador_errores = 0

    for i in range(8):
        if temperaturas[i] < 0 or temperaturas[i] > 100:
            temperaturas[i] = 35.0
            contador_errores += 1

    return contador_errores


def calcular_promedio(temperaturas):
    suma = 0
    contador = 0

    for valor in temperaturas:
        suma += valor
        contador += 1

    return suma / contador


def mostrar_resultados(temperaturas, errores, promedio):
    print(f"\nSe detectaron {errores} lecturas erróneas y fueron corregidas a 35.0.")
    print(f"\nDatos limpios: {temperaturas}")
    print(f"\nPromedio de operación: {promedio:.2f}°C")

    if promedio > 75:
        print("ALERTA: Activando sistema de enfriamiento líquido")
    else:
        print("Estado: Operación normal")


def main():
    print("--- SISTEMA DE FILTRADO DE DATOS (SENSOR GPU) ---\n")

    temperaturas = leer_temperaturas()
    errores = filtrar_datos(temperaturas)
    promedio = calcular_promedio(temperaturas)

    mostrar_resultados(temperaturas, errores, promedio)


if __name__ == "__main__":
    main()