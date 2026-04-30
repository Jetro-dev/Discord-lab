class ControlAcceso:
    def __init__(self):
        self.usuarios_autorizados = {
            "2024001": "Investigador",
            "2024002": "Estudiante",
            "2024003": "Administrador"
        }

    def verificar_permisos(self, matricula):
        if matricula in self.usuarios_autorizados:
            rol = self.usuarios_autorizados[matricula]
            print(f"> [ACCESO CONCEDIDO] Bienvenido, rol detectado: {rol}.")
            return rol
        else:
            print("> [ACCESO DENEGADO] Usuario no registrado en la base de datos de IA.")
            return None

    def agregar_usuario(self, matricula, rol):
        self.usuarios_autorizados[matricula] = rol
        print("> Usuario agregado correctamente.")



def main():
    sistema = ControlAcceso()

    print("--- Sistema de Seguridad Laboratorio IA - UX ---\n")

    while True:
        try:
            matricula = input("Ingrese su matrícula: ").strip()

            if matricula == "":
                raise ValueError("Campo vacío")

            rol = sistema.verificar_permisos(matricula)

            # Funcionalidad extra: solo el administrador puede agregar usuarios
            if rol == "Administrador":
                opcion = input("¿Desea agregar un nuevo usuario? (s/n): ").lower()
                if opcion == "s":
                    nueva_matricula = input("Nueva matrícula: ").strip()
                    nuevo_rol = input("Rol del usuario: ").strip()
                    sistema.agregar_usuario(nueva_matricula, nuevo_rol)

        except ValueError:
            print("> [ERROR] Entrada inválida. No deje el campo vacío.")

        finally:
            print("--- Intento de acceso registrado en el log del servidor ---\n")


# --- EJECUCIÓN ---
if __name__ == "__main__":
    main()