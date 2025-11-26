# Instala dependencias en el entorno actual (recomendado usar virtualenv)
python -m pip install -r .\examples\requirements.txt

# Ejecutar tests
pytest .\examples

# Ejecutar la app (abre http://127.0.0.1:5000/api/login)
python .\examples\app.py
