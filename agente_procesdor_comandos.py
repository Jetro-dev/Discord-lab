import datetime

from practica01.procesador_comandos import obtener_saludo,procesar_comando_recordar, calcular_uptime, mostrar_ayuda

NOMBRE_BOT = "PedroBot"
PREFIJO = "!"

hora_inicio = datetime.datetime.now()

print(obtener_saludo(NOMBRE_BOT))

while True:
    entrada = input("Ingrese comando: ").strip()

    if not entrada.startswith(PREFIJO):
        print("Comando no reconocido.")
        continue

    partes = entrada[len(PREFIJO):].split(" ", 1)
    comando = partes[0]
    argumento = partes[1] if len(partes) > 1 else ""

    if comando == "saludo":
        print(obtener_saludo(NOMBRE_BOT))

    elif comando == "recordar":
        print(procesar_comando_recordar(argumento))

    elif comando == "uptime":
        print(calcular_uptime(hora_inicio))

    elif comando == "ayuda":
        print(mostrar_ayuda())

    elif comando == "finalizar":
        print("Finalizando el agente. ¡Hasta luego!")
        break

    else:
        print("Comando no reconocido.")