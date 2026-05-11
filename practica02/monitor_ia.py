

def leer_telemetria():
    temperatura = float(input("Temperatura actual (°C): "))
    memoria = int(input("Uso de Memoria VRAM (%): "))
    enfriamiento = input("¿Enfriamiento activo? (si/no): ").lower()

    return temperatura, memoria, enfriamiento


def validar_memoria(memoria):
    if memoria < 0 or memoria > 100:
        return False
    return True


def diagnosticar_sistema(temperatura, memoria, enfriamiento):
  
    if temperatura > 90 or memoria == 100:
        return "¡ALERTA CRÍTICA! Apagando servidores para evitar daños físicos."

    elif temperatura >= 75 and temperatura <= 90:

        if enfriamiento == "no":
            return "Peligro: Temperatura alta y enfriamiento desactivado. Pausando entrenamiento."

        elif enfriamiento == "si":
            return "Temperatura elevada. Reduciendo velocidad de procesamiento (Throttling)."

    
    elif temperatura < 75 and memoria < 80:
        return "Sistema Estable: Entrenamiento en curso a máxima capacidad."

    return "Estado no definido."




def main():
    print("--- TELEMETRÍA DE CLUSTER IA ---\n")

    temperatura, memoria, enfriamiento = leer_telemetria()

    if not validar_memoria(memoria):
        print("\nError: Lectura de memoria fuera de rango (0-100%).")
    else:
        resultado = diagnosticar_sistema(temperatura, memoria, enfriamiento)
        print(f"\n> Diagnóstico: {resultado}")



if __name__ == "__main__":
    main()