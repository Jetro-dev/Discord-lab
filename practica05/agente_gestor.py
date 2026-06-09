import discord
import os
import re
from dotenv import load_dotenv
from practica02.gestor_de_comandos import buscar_en_diccionario, validar_variable, analizar_comando

def mostrar_bienvenida():
    """Retorna la lista de comandos disponibles."""
    return (
        "📜 Bot de Gestión de Tareas (Modo Estructurado):\n"
        "📜 Primeros pasos Agente Discord UX:\n"
        "📜 escriba !busca <el término> para buscar en el diccionario\n"
        "📜 escriba !valida <la variable> para validar una variable\n"
        "📜 escriba !analiza <el comando> para analizar un comando\n"
        "📜 Esccriba !Exit para salir del Agente:"
    )

def main(entrada):
    
        PREFIJO = "!"
        
        if not entrada.startswith(PREFIJO):
            if entrada: print("Recuerda usar '!' para comandos.")
            
        # Procesamiento de la entrada
        cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""
        
        # Selección de acción (Estructura de control)
        if comando == "exit":
            print("Saliendo del gestor...")
            return "Saliendo del gestor..."
                        
        elif comando == "inicio":
           # print(mostrar_bienvenida())
            return mostrar_bienvenida()
        elif comando == "busca":            
            return buscar_en_diccionario(argumento)
        elif comando == "valida":
            return validar_variable(argumento)
        elif comando == "analiza":
            return analizar_comando(argumento)
        else:
            print(f" Error: Comando '!{comando}' no reconocido.")
            return f" Error: Comando '!{comando}' no reconocido."
        
        print("-" * 20)


# --- CONFIGURACIÓN DE DISCORD ---

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Definir los "intents" (permisos) necesarios
intents = discord.Intents.default()
intents.message_content = True  # Necesario para leer el contenido de los mensajes

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Sincronizado como {client.user} (ID: {client.user.id})')
    print('------')

@client.event
async def on_message(message):
    # Evitar que el bot se responda a sí mismo
    if message.author == client.user:
        return
    
    # 3. Procesamiento: Pasamos el contenido del mensaje a nuestra lógica
    print(f"Mensaje recibido de {message.author}: {message.content}")

      # Solo procesamos si el mensaje empieza con un prefijo (opcional, pero recomendado)
    if message.content.startswith('!'):
        resultado = main(message.content)

        print(f"Resultado del procesamiento: {resultado}")
        
        # 4. Respuesta: El bot escribe el resultado en el mismo canal
        await message.channel.send(f" **Bot Procesador:** {resultado}")
    
# Ejecutar el bot
if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("ERROR: No se encontró el TOKEN en el archivo .env")