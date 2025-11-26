# Informe de fallos — `AcademyVerso_buggy.py`

Este documento lista los fallos intencionados presentes en `AcademyVerso_buggy.py`, su gravedad, el impacto y las correcciones sugeridas para cada uno.

Resumen rápido de fallos
- Credenciales hardcodeadas (`user`, `password`) — Alta gravedad (seguridad).
- Ruta no portable `DB_PATH = '/tmp/app.db'` — Media.
- Argumento por defecto mutable en `process_values(values=[])` — Media (bugs sutiles).
- División por cero posible en `100 / v` — Alta (crash en producción).
- Archivo abierto sin cerrar en `load_config` — Media (fuga de recursos).
- Ejecución directa de comandos con `os.system(command)` — Alta (inyección de comandos).
- Uso de `eval(s)` sobre input externo — Crítica (ejecución arbitraria de código).
- Construcción de query SQL por concatenación (SQL injection) — Crítica.
- Manejo de excepciones demasiado amplio que oculta errores (`except Exception: pass`) — Alta (oculta fallos y complica debugging).

Detalles, impacto y correcciones sugeridas

1) Credenciales hardcodeadas
- Dónde: `connect_db()` contiene `user = 'admin'` y `password = 'P@ssw0rd123'`.
- Impacto: exponer secretos en el código fuente es un riesgo directo de seguridad.
- Corrección: mover credenciales a variables de entorno o a un gestor de secretos.

Ejemplo:

```python
import os

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
```

2) Ruta no portable
- Dónde: `DB_PATH = '/tmp/app.db'`.
- Impacto: no funciona en Windows; uso inconsistente entre entornos.
- Corrección: usar `os.path.join` y configuración por entorno.

3) Argumento por defecto mutable
- Dónde: `def process_values(values=[])`.
- Impacto: la lista por defecto se comparte entre llamadas, causando resultados inesperados.
- Corrección: usar `None` por defecto y crear una nueva lista dentro.

Ejemplo:

```python
def process_values(values=None):
    if values is None:
        values = []
    # ...
```

4) División por cero
- Dónde: `results.append(100 / v)` sin validar `v`.
- Impacto: excepción `ZeroDivisionError` que puede romper el proceso.
- Corrección: validar antes de dividir; decidir política (omitir, devolver `None`, o lanzar excepción con mensaje).

Ejemplo:

```python
for v in values:
    if v == 0:
        results.append(None)  # política elegida
        continue
    results.append(100 / v)
```

5) Archivo abierto sin cerrar
- Dónde: `f = open(path, 'r')` en `load_config` y nunca se cierra.
- Impacto: fugas de file descriptors y problemas en sistemas con límite de archivos abiertos.
- Corrección: usar `with open(...) as f:` para asegurar cierre.

Ejemplo:

```python
def load_config(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
```

6) Ejecución de shell con input del usuario
- Dónde: `run_shell(command)` usa `os.system(command)` con input directo.
- Impacto: inyección de comandos y ejecución arbitraria; riesgo crítico.
- Corrección: evitar ejecución directa; si es necesario, validar/filtrar la entrada o usar `subprocess.run` con lista de argumentos.

Ejemplo seguro (evitar interpretar shell):

```python
import shlex, subprocess

def run_shell_safe(command):
    args = shlex.split(command)
    subprocess.run(args, check=True)
```

7) Uso de `eval` sobre input externo
- Dónde: `dangerous_eval(s)` usa `eval(s)`.
- Impacto: ejecución arbitraria de código — RIESGO CRÍTICO.
- Corrección: no usar `eval` en input externo. Para parsear expresiones simples, usar `ast.literal_eval` o implementar un parser seguro.

Ejemplo seguro:

```python
import ast

def safe_eval(s):
    return ast.literal_eval(s)
```

8) SQL injection por concatenación
- Dónde: `query = "INSERT INTO users (name) VALUES ('%s')" % name` y `cur.execute(query)`.
- Impacto: un atacante puede inyectar SQL en `name` y comprometer la BD.
- Corrección: usar parámetros en la consulta (placeholders) proporcionados por el conector DB.

Ejemplo con SQLite:

```python
cur.execute('INSERT INTO users (name) VALUES (?)', (name,))
```

9) Manejo de excepciones que oculta errores
- Dónde: `except Exception: pass` en `save_user_input`.
- Impacto: errores silenciosos que dificultan la detección y el debugging.
- Corrección: registrar el error (logging) y, si corresponde, propagarlo o devolver un código de error.

Ejemplo:

```python
import logging

logger = logging.getLogger(__name__)

except Exception as e:
    logger.exception('Error guardando usuario')
    raise
```

Pruebas y análisis que recomendamos ejecutar
- Ejecutar linters y scanners de seguridad:
  - `flake8` para estilo.
  - `bandit` para encontrar problemas de seguridad (eval, os.system, SQL injection).
  - `pylint` para más reglas.

- Añadir tests unitarios que cubran:
  - caso con `v == 0` en `process_values`.
  - archivo `config.json` inexistente o inválido.
  - entradas maliciosas para `save_user_input` (pruebas de inyección SQL con mocks de BD).

Checklist para el PR de corrección
- Mover secretos fuera del código (variables de entorno / secret manager).  
- Reemplazar rutas harcodeadas por configuración.  
- Evitar mutable default args y corregir la división por cero.  
- Usar context managers para archivos y conexiones a BD.  
- Reemplazar `eval` por `ast.literal_eval` o eliminar su uso.  
- Parametrizar consultas SQL y usar el API del driver correctamente.  
- Añadir logging y no silenciar excepciones.  
- Añadir tests que cubran casos límite y entradas maliciosas.

Ejemplo de mensaje de PR sugerido

```
Fix: multiple security and robustness issues in AcademyVerso_buggy.py

- Moved credentials to environment variables.
- Avoid division by zero in processValues and removed mutable default arg.
- Use context managers for file and DB access.
- Replace eval with safe parsing and parameterize SQL queries.
- Add unit tests for edge cases.
```

¿Quieres que genere además un prompt en `prompts/` para ejecutar una revisión automática (formato: JSON con hallazgos categorizados) sobre `AcademyVerso_buggy.py`? Puedo crear ese prompt y un pequeño script que lo ejecute y muestre un reporte simulado o real según prefieras.
