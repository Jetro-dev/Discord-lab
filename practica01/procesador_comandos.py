import datetime

def obtener_saludo(nombre_bot):
    return f"Hola, soy {nombre_bot}. ¿En qué puedo ayudarte?"

def procesar_comando_recordar(argumento):

   return f"entendido! recordaré el nombre: {argumento}"



def calcular_uptime(hora_inicio):
    ahora = datetime.datetime.now()
    diferencia = ahora - hora_inicio
    segundos = int(diferencia.total_seconds())
    return f"tiempo de actividad: {segundos} segundos."

    





def main():
    nombre_bot = "AgenteGPT"
    "iniciar_agente(nombre_bot)"

if __name__ == "__main__":
    main()

