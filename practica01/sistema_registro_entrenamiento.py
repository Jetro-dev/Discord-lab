

class MonitorEntrenamiento:
    def __init__(self, umbral_convergencia=0.01):
        self.historial_errores = []
        self.umbral_convergencia = umbral_convergencia

    def registrar_epoca(self, valor_error):
        if valor_error < self.umbral_convergencia:
            print("[SISTEMA] Entrenamiento completado: Se alcanzó el objetivo de precisión.")
        
        self.historial_errores.append(valor_error)
        print("> Registro exitoso.")



def main():
    monitor = MonitorEntrenamiento()

    print("--- Iniciando Monitor de Red Neuronal ---\n")

    epoca = 1
    while epoca <= 5:
        try:
            entrada = input(f"Ingrese el error de la Época {epoca}: ")
            valor = float(entrada)

            if valor < 0:
                print("> [ERROR] El error no puede ser negativo.")
                continue

            monitor.registrar_epoca(valor)
            epoca += 1

        except ValueError:
            print("> [ERROR] Entrada inválida. Por favor, ingrese un número decimal.")

    print("\n--- Resumen de Entrenamiento ---")

    historial = monitor.historial_errores
    print(f"Historial: {historial}")

    if len(historial) > 0:
        promedio = sum(historial) / len(historial)
        mejor = min(historial)

        print(f"Promedio de Error: {promedio}")
        print(f"Mejor resultado obtenido: {mejor}")



if __name__ == "__main__":
    main()