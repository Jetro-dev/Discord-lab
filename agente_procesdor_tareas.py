import datetime
from practica03.tareas_agente import  agregar_tarea, listado_tareas, eliminar_tarea

tareas = []
PREFIJO = "!"

print("Bienvenido al gestor de tareas")

activa = True

while activa:
    entrada = input(">>> ").strip()

    if not entrada.startswith(PREFIJO):
        print("Error: Comando no reconocido")
        continue

    cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
    comando = cuerpo[0].lower()
    argumento = cuerpo[1] if len(cuerpo) > 1 else ""

    if comando == "add":
        print(agregar_tarea(tareas, argumento))

    elif comando == "list":
        print(listado_tareas(tareas))

    elif comando == "del":
        print(eliminar_tarea(tareas, argumento))

    elif comando == "salir":
        print("Hasta luego")
        activa = False

    else:
        print("Comando no reconocido")