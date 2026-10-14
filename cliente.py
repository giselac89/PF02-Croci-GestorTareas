# ---------------------------
# Cliente API - TP PFO 2
# Programación sobre Redes
# ---------------------------

import requests

url = "http://localhost:5000/tareas"

def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Ver tareas")
    print("4. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            print(">> Elegiste Registrarse")
        elif opcion == "2":
            print(">> Elegiste Iniciar sesión")
        elif opcion == "3":
            print(">> Elegiste Ver tareas")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, probá de nuevo.")


if __name__ == "__main__":
    main()