import datetime

def agregar_tarea(lista_tareas, descripcion):
    '''
    Agrega una tarea a la lista si cumple con los requisitos
    '''

    if len(descripcion) < 3:
        return "Error: Longitud no válida"
    
    #crear formato para la tarea
    fecha = datetime.datetime.now().strftime("%H:%M")
    nueva_tarea = f"{descripcion} - {fecha}"
    lista_tareas.append(nueva_tarea)
    return f"Tarea agregada con éxito"

def listado_tareas(lista_tareas):
    '''
    Devuelve un listado de tareas formateado
    '''
    if not lista_tareas:
        return "No hay tareas pendientes"
    
    #agrega una variable llamada resultado
    resultado = "Listado de tareas:\n"

    #Iterar la lista de tareas y formatear la salida
    for i, tarea in enumerate(lista_tareas, 1):
        resultado += f"{i}. {tarea}\n"
    return resultado.strip()

def eliminar_tarea(lista_tareas, indice):
    '''
    Elimina una tarea de la lista según su índice
    '''
    if not indice.isdigit():
        return "Error: El índice debe ser un número"
    
    indice = int(indice)-1

    #Agregamos la logica para preguntar
    #Si el elemento esta en la lista y eliminarlo
    if 0 <= indice < len(lista_tareas):
        tarea_eliminada = lista_tareas.pop(indice)
    else:
        return "Error: Índice fuera de rango"
    return f"Tarea eliminada: {tarea_eliminada}"

def main():
    tareas = []
    PREFIJO = "!"

    print("Bienvenido al gestor de tareas")
    activa = True
    while activa:
        entrada = input(">>> ").strip()

        if not entrada.startswith(PREFIJO):
            print("Error: Comando no reconocido")
            continue

        #Procesamiento de la entrada
        cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""

        #Seleccion de accion
        if comando == "add":
            resultado = agregar_tarea(tareas, argumento)
            print