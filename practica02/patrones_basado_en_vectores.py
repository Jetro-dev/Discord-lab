def leer_sentimientos():
    puntajes_sentimiento = [0, 0, 0]

    for i in range(5):
        clasificacion = int(input(f"Palabra {i+1} - Clasificación (0, 1, 2): "))

        if clasificacion >= 0 and clasificacion <= 2:
            puntajes_sentimiento[clasificacion] += 1

    return puntajes_sentimiento


def buscar_mayor(vector):
    mayor = vector[0]
    indice_mayor = 0

    for i in range(1, 3):
        if vector[i] > mayor:
            mayor = vector[i]
            indice_mayor = i

    return indice_mayor


def mostrar_resultado(vector, indice):
    print(f"\nEstado final del vector de características: {vector}")

    if indice == 0:
        print("Resultado de IA: La frase es Positiva (Predominancia en índice 0)")
    elif indice == 1:
        print("Resultado de IA: La frase es Neutral (Predominancia en índice 1)")
    else:
        print("Resultado de IA: La frase es Negativa (Predominancia en índice 2)")


def main():
    print("--- ANALIZADOR DE SENTIMIENTOS IA ---\n")

    vector = leer_sentimientos()

    indice_mayor = buscar_mayor(vector)

    mostrar_resultado(vector, indice_mayor)


if __name__ == "__main__":
    main()