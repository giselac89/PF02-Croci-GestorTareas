# ---------------------------
# Servidor API - TP PFO 2
# Programación sobre Redes
# ---------------------------


from flask import Flask, request, jsonify
import sqlite3
from werkzeug.security import generate_password_hash


app = Flask(__name__)
NOMBRE_DB = 'usuarios.db'

app.config['SECRET_KEY'] = 'tu_clave_secreta'

# ---------------------------------------------------------
# Inicialización de la base de datos
# ---------------------------------------------------------

def inicializar_db():
    conn = sqlite3.connect(NOMBRE_DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_usuario TEXT UNIQUE NOT NULL,
            contraseña_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Base de datos inicializada correctamente.")

def obtener_conexion():
    return sqlite3.connect(NOMBRE_DB)

# ---------------------------------------------------------
# Endpoint: Registro
# ---------------------------------------------------------

def registrar_usuario(nombre_usuario, contraseña):

    datos = request.get_json(silent=True)
 
    if not datos or "usuario" not in datos or "contraseña" not in datos:
        return jsonify({"error": "Faltan datos: se requiere 'usuario' y 'contraseña'"}), 400

    nombre_usuario = datos["usuario"]
    contraseña = datos["contraseña"]
    
    contraseña_hash = generate_password_hash(contraseña)
    conn = obtener_conexion()
  
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (nombre_usuario, contraseña_hash) VALUES (?, ?)', (nombre_usuario, contraseña_hash))
        conn.commit()
        return jsonify({"status": f"Usuario '{nombre_usuario}' registrado con éxito"}), 200
    except sqlite3.IntegrityError:
        return jsonify({"error": f"El usuario '{nombre_usuario}' ya existe"}), 400
    finally:
        conn.close()

# ---------------------------------------------------------
# Programa principal
# ---------------------------------------------------------

if __name__ == "__main__":
    inicializar_db()
    app.run(port=5000, debug=True)