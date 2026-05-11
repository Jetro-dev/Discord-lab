# ==========================================
# SISTEMA DE BIENESTAR DIARIO
# ==========================================

print("========================================")
print(" SISTEMA DE BIENESTAR SEMANAL ")
print("========================================")

# ---------------------------------
# ENTRADA DE DATOS
# ---------------------------------

sueno = float(input("\n¿Cuántas horas dormiste hoy?: "))

ejercicio = input(
    "¿Hiciste actividad física? (si/no): "
).lower()

estres = int(input(
    "¿Qué tan estresado te sentiste hoy? (1-10): "
))

comidas = input(
    "¿Comiste al menos 3 veces hoy? (si/no): "
).lower()

saludable = input(
    "¿Tuviste alimentación saludable? (si/no): "
).lower()

redes = float(input(
    "¿Cuántas horas usaste redes sociales?: "
))

videojuegos = float(input(
    "¿Cuántas horas jugaste videojuegos?: "
))

tareas_totales = int(input(
    "¿Cuántas actividades escolares tenías?: "
))

tareas_completadas = int(input(
    "¿Cuántas completaste?: "
))

social = float(input(
    "¿Cuántas horas conviviste con familia o amigos?: "
))

temprano = input(
    "¿Dormiste temprano? (si/no): "
).lower()

# ---------------------------------
# CÁLCULO DE HORAS
# ---------------------------------

horas_tareas = tareas_totales * 1
horas_comidas = 1  # Aproximadamente 20 min por comida

horas_totales = (
    sueno +
    redes +
    videojuegos +
    horas_tareas +
    social +
    horas_comidas
)

if ejercicio == "si":
    horas_totales += 1

# ---------------------------------
# VARIABLES
# ---------------------------------

puntos = 0

positivos = []
negativos = []
consejos = []

# =================================
# SUEÑO
# =================================

if 8 <= sueno <= 10:
    puntos += 20
    positivos.append("Buen descanso")

else:
    negativos.append("Pocas horas de sueño")
    consejos.append(
        "Dormir entre 8 y 10 horas ayuda al rendimiento y energía."
    )

# =================================
# EJERCICIO
# =================================

if ejercicio == "si":
    puntos += 15
    positivos.append("Realizaste actividad física")

else:
    negativos.append("Faltó actividad física")
    consejos.append(
        "Hacer ejercicio ayuda a reducir estrés y mejorar salud."
    )

# =================================
# ESTRÉS
# =================================

if estres <= 4:
    puntos += 15
    positivos.append("Buen manejo del estrés")

elif estres <= 7:
    puntos += 8

else:
    negativos.append("Estrés elevado")
    consejos.append(
        "Buscar momentos de descanso puede ayudarte."
    )

# =================================
# ALIMENTACIÓN
# =================================

if comidas == "si":
    puntos += 10
    positivos.append("Comiste adecuadamente")

else:
    negativos.append("Saltaste comidas")
    consejos.append(
        "Comer bien ayuda a mantener energía y concentración."
    )

if saludable == "si":
    puntos += 10
    positivos.append("Tuviste alimentación saludable")

else:
    negativos.append("Alimentación poco saludable")
    consejos.append(
        "Intentar comer más saludable puede mejorar tu bienestar."
    )

# =================================
# REDES SOCIALES
# =================================

if redes <= 3:
    puntos += 10

else:
    negativos.append("Mucho tiempo en redes sociales")
    consejos.append(
        "Reducir tiempo en pantalla puede mejorar el descanso."
    )

# =================================
# VIDEOJUEGOS
# =================================

if videojuegos <= 3:
    puntos += 10

else:
    negativos.append("Muchas horas en videojuegos")
    consejos.append(
        "Tomar pausas puede ayudarte a descansar mejor."
    )

# =================================
# ACTIVIDADES ESCOLARES
# =================================

if tareas_totales > 0:

    porcentaje_tareas = (
        tareas_completadas / tareas_totales
    ) * 100

    if porcentaje_tareas >= 80:
        puntos += 10
        positivos.append(
            "Completaste la mayoría de actividades escolares"
        )

    elif porcentaje_tareas >= 50:
        puntos += 5

    else:
        negativos.append(
            "Muchas actividades escolares pendientes"
        )

        consejos.append(
            "Organizar mejor tu tiempo podría ayudarte."
        )

# =================================
# VIDA SOCIAL
# =================================

if social >= 1:
    puntos += 5
    positivos.append(
        "Conviviste con familia o amigos"
    )

else:
    negativos.append(
        "Poco tiempo social"
    )

# =================================
# DORMIR TEMPRANO
# =================================

if temprano == "si":
    puntos += 5

else:
    negativos.append("Dormiste tarde")
    consejos.append(
        "Dormir temprano mejora la calidad del sueño."
    )

# =================================
# VALIDACIÓN DE HORAS
# =================================

if horas_totales > 24:

    negativos.append(
        "Las actividades exceden las 24 horas del día"
    )

    consejos.append(
        "Revisa los datos ingresados o mejora tu organización."
    )

# =================================
# RESULTADO FINAL
# =================================

calidad_vida = puntos

# =================================
# RESULTADOS
# =================================

print("\n========================================")
print(" RESULTADOS ")
print("========================================")

print(f"\nCalidad de vida: {calidad_vida}%")

print("\nAspectos positivos:")
for p in positivos:
    print("✔", p)

print("\nAspectos negativos:")
for n in negativos:
    print("✘", n)

print("\nConsejos:")
for c in consejos:
    print("-", c)

print("\nHoras registradas en el día:", horas_totales)