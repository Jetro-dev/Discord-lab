def leer_sensor():
    lectura_sensor = []

    for i in range(5):
        valor = int(input(f"Ingrese bit {i+1}: "))
        lectura_sensor.append(valor)

    return lectura_sensor


def comparar_patrones(patron_maestro, lectura_sensor):
    coincidencias = 0

    for i in range(5):
        if patron_maestro[i] == lectura_sensor[i]:
            coincidencias += 1

    return coincidencias


def calcular_similitud(coincidencias):
    similitud = (coincidencias / 5) * 100
    return similitud


def mostrar_resultado(coincidencias, similitud):
    print("\n> Comparando lectura con base de datos...")
    print(f"\n> Coincidencias encontradas: {coincidencias}")
    print(f"> Porcentaje de Similitud: {similitud}%")

    if similitud == 100:
        print("ESTADO: ACCESO TOTAL: Identidad Verificada.")
    elif similitud >= 60:
        print("ESTADO: ADVERTENCIA: Similitud parcial. Se requiere verificación manual.")
    else:
        print("ESTADO: ALERTA: Intruso detectado. Sistema bloqueado.")



def main():
    patron_maestro = [1, 0, 1, 1, 0]

    print("--- ESCÁNER BIOMÉTRICO DE IA ---\n")

    lectura_sensor = leer_sensor()

    coincidencias = comparar_patrones(patron_maestro, lectura_sensor)

    similitud = calcular_similitud(coincidencias)

    mostrar_resultado(coincidencias, similitud)



if __name__ == "__main__":
    main()