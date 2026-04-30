import math
from datetime import date


def imprimir_encabezado():
    print("====================================")
    print("    SISTEMA DE SALUD INTELIGENTE   ")
    print("====================================")
    print(f"Fecha: {date.today()}\n")


def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)


def evaluar_presion(presion_sistolica):
    if presion_sistolica > 140:
        return "Alta"
    else:
        return "Normal"


def main():
    imprimir_encabezado()

    nombre = input("Nombre del Paciente: ")
    peso = float(input("Peso (kg): "))
    estatura = float(input("Estatura (m): "))
    presion = int(input("Presión Sistólica: "))

    imc = calcular_imc(peso, estatura)
    imc_redondeado = math.ceil(imc)
    estado_presion = evaluar_presion(presion)

    print("\n--- RESULTADOS DEL ANÁLISIS ---")
    print(f"Paciente: {nombre}")
    print(f"IMC Calculado: {imc_redondeado}")
    print(f"Estado de Presión: {estado_presion}")


if __name__ == "__main__":
    main()