# ---------------------------
# Cliente API - TP PFO 2
# Programación sobre Redes
# ---------------------------

import requests
import getpass

URL_BASE = "http://localhost:5000"

def registrar_usuario(usuario, contraseña):
    url_registro = URL_BASE + "/registro"
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
    response = requests.post(URL_BASE + "/login", json=datos)
    return response.json(), response.status_code

def ver_tareas(usuario, contraseña):
    response = requests.get(URL_BASE + "/tareas", auth=(usuario, contraseña))    
    return response.text, response.status_code


def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            usuario = input("Usuario: ")
            contraseña = getpass.getpass("Contraseña: ")
            datos, codigo = registrar_usuario(usuario, contraseña)
            print(datos.get("status") or datos.get("error"))
        elif opcion == "2":
            usuario = input("Usuario: ")
            contraseña = getpass.getpass("Contraseña: ")
            datos, codigo = iniciar_sesion(usuario, contraseña)
            print(datos.get("status") or datos.get("error"))
        elif opcion == "3":
            usuario = input("Usuario: ")
            contraseña = getpass.getpass("Contraseña: ")
            texto, codigo = ver_tareas(usuario, contraseña)
            if codigo == 200:
                print(texto)
            else:
                print("Acceso denegado. Usuario o contraseña incorrectos.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, probá de nuevo.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma cerrado.")