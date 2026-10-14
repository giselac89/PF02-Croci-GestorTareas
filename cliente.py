# ---------------------------
# Cliente API - TP PFO 2
# Programación sobre Redes
# ---------------------------

import requests

URL_BASE = "http://localhost:5000"

def registrar_usuario(usuario, contraseña):
    url_registro = "http://localhost:5000/registro"
    datos = {"usuario": usuario, "contraseña": contraseña}
    response = requests.post(url_registro, json=datos)
    return response.json(), response.status_code



def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Ver tareas")
    print("4. Salir")

def iniciar_sesion(usuario, contraseña):
    datos = {"usuario": usuario, "contraseña": contraseña}
    response = requests.post("http://localhost:5000/login", json=datos)
    return response.json(), response.status_code


def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            datos, codigo = registrar_usuario(usuario, contraseña)
            print(datos.get("status") or datos.get("error"))
        elif opcion == "2":
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            datos, codigo = iniciar_sesion(usuario, contraseña)
            print(datos.get("status") or datos.get("error"))
        elif opcion == "3":
            print(">> Elegiste Ver tareas")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, probá de nuevo.")


if __name__ == "__main__":
    main()