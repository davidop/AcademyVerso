"""Script intencionadamente con errores para demo de Code Review.

Incluye bugs comunes: división por cero, inyección de comandos, uso inseguro de eval,
fugas de recursos, credenciales embebidas, manejo pobre de excepciones, mutables por defecto.
"""
import os
import json
import sqlite3


DB_PATH = '/tmp/app.db'  # path non-portable


def connect_db():
    # Credenciales hardcodeadas (mala práctica)
    user = 'admin'
    password = 'P@ssw0rd123'
    conn = sqlite3.connect(DB_PATH)
    return conn


def process_values(values=[]):
    # Mutable default argument (bug subtle)
    results = []
    for v in values:
        # posibilidad de ZeroDivisionError si v == 0
        results.append(100 / v)
    return results


def load_config(path):
    f = open(path, 'r')
    data = json.load(f)
    # No cerramos el archivo (fuga de recurso)
    return data


def run_shell(command):
    # Ejecuta directamente la entrada del usuario: riesgo de inyección de comandos
    os.system(command)


def dangerous_eval(s):
    # Eval es inseguro si se usa sobre input externo
    return eval(s)


def save_user_input(name):
    try:
        conn = connect_db()
        cur = conn.cursor()
        # Vulnerable a SQL injection por concatenación directa
        query = "INSERT INTO users (name) VALUES ('%s')" % name
        cur.execute(query)
        conn.commit()
    except Exception:
        # Capturamos todo y no informamos (mala práctica)
        pass


def main():
    # Ejemplo de uso
    cfg = load_config('config.json')
    print('Config loaded:', cfg.get('app_name', 'unknown'))

    vals = [10, 0, 5]
    print('Processing values:', process_values(vals))

    cmd = input('Introduce comando para ejecutar: ')
    run_shell(cmd)

    user = input('Nombre para guardar: ')
    save_user_input(user)

    expr = input('Expresión para evaluar (demo): ')
    print('Eval result:', dangerous_eval(expr))


if __name__ == '__main__':
    main()
