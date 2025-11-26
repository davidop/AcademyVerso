# Demo examples

Este directorio contiene un runner mínimo para las demos. Está diseñado para ejecutarse en modo `simulate` sin llamar a ninguna API externa.

Cómo usarlo:

1. Desde PowerShell en la raíz del repo ejecuta:

```powershell
python .\examples\demo_runner.py
```

2. Para integrar con una API real, implementa la función `call_model(prompt, mode='simulate')` en `demo_runner.py`.
