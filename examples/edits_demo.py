"""Demo de Edits: aplica ediciones simuladas a un párrafo.

Ejecuta:
  py .\examples\edits_demo.py
"""

ORIGINAL = (
    "Este documento tiene como objetivo explicar en términos generales y con cierto detalle el procedimiento por el cual "
    "se deben tramitar las solicitudes, incluyendo los posibles plazos y condicionantes que pueden afectar al proceso. "
    "Se recomienda encarecidamente que todas las partes implicadas revisen la documentación adjunta y, en caso de duda, "
    "contacten con el departamento correspondiente para obtener aclaraciones adicionales."
)


def edit_formal(text):
    # Simula una edición para hacerlo más formal
    return (
        "El presente documento expone el procedimiento para tramitar las solicitudes, detallando plazos y condicionantes aplicables. "
        "Se recomienda que las partes revisen la documentación adjunta y contacten con el departamento competente para aclaraciones."
    )


def edit_concise(text):
    # Simula una edición para hacerlo conciso
    return (
        "Resumen del procedimiento, plazos y condiciones. Revisar documentación adjunta y contactar al departamento encargado si procede."
    )


def main():
    print('--- Original ---')
    print(ORIGINAL)
    print('\n--- Formalizado ---')
    print(edit_formal(ORIGINAL))
    print('\n--- Conciso ---')
    print(edit_concise(ORIGINAL))


if __name__ == '__main__':
    main()
