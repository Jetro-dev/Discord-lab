def leer_sensores():
    sensores = []
    for i in range(5): 
        distancia = float(input(f"Ingrese distancia sensor {i+1}: "))
        sensores.append(distancia)
    return sensores


def calcular_promedio(sensores):
    return sum(sensores) / len(sensores)


def leer_matriz():
    matriz = []
    print("\nLlenando matriz de cámara 3x3:\n")
    for fila in range(3): 
        fila_datos = []
        for col in range(3):
            valor = int(input(f"Fila {fila}, Col {col} (Brillo 0-255): "))
            
            # Saturación
            if valor > 255:
                valor = 255

            fila_datos.append(valor)
        matriz.append(fila_datos)
    return matriz


def imprimir_matriz(matriz):
    print("\nVisualización de la imagen capturada:\n")
    for fila in matriz:
        print("[ ", end="")
        for valor in fila:
            print(f"{valor:3}", end=" ")
        print("]")


def contar_brillantes(matriz):
    contador = 0
    for fila in matriz:
        for valor in fila:
            if valor > 200:
                contador += 1
    return contador


def main():
    print("--- MÓDULO DE SENSORES (VECTORES) ---\n")

    sensores = leer_sensores()
    promedio = calcular_promedio(sensores)

    if promedio < 2.0:
        print(f"\nPromedio de proximidad: {promedio:.1f}m. Aviso: Reduciendo velocidad global.")
    else:
        print(f"\nPromedio de proximidad: {promedio:.1f}m. Estado: Seguro.")

    print("\n--- MÓDULO DE VISIÓN (MATRICES) ---")

    matriz = leer_matriz()
    imprimir_matriz(matriz)

    brillantes = contar_brillantes(matriz)

    print("\nResultado de Análisis IA:")
    print(f"Se detectaron {brillantes} píxeles de alta intensidad.")


if __name__ == "__main__":
    main()