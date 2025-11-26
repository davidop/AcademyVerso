"""Demo Plan: genera un roadmap simulado y exporta tickets.

Ejecuta:
  py .\examples\plan_demo.py
"""
import csv


DEFAULT_PLAN = [
    (1, 'Semana 1', 'Definir requisitos y MVP scope', 'high'),
    (2, 'Semana 2', 'Diseño de UI y prototipo', 'medium'),
    (3, 'Semana 3', 'Implementar backend básico (API)', 'high'),
    (4, 'Semana 4', 'Integración frontend-backend', 'medium'),
    (5, 'Semana 5', 'Pruebas y QA', 'medium'),
    (6, 'Semana 6', 'Despliegue y monitoreo', 'high'),
]


def display_plan(plan):
    print('Plan sugerido:')
    for item in plan:
        print(f"{item[0]}. {item[1]} - {item[2]} (prioridad: {item[3]})")


def edit_priorities(plan):
    print('\nEditar prioridades (escribe nueva prioridad: low/medium/high). Presiona Enter para mantener.')
    new_plan = []
    for item in plan:
        newp = input(f"{item[0]}. {item[1]} (actual: {item[3]}): ").strip()
        if newp in ('low','medium','high'):
            new_plan.append((item[0], item[1], item[2], newp))
        else:
            new_plan.append(item)
    return new_plan


def export_csv(plan, path='examples/tickets.csv'):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id','week','summary','priority'])
        for item in plan:
            writer.writerow([item[0], item[1], item[2], item[3]])
    print(f'Exportado a {path}')


def main():
    plan = DEFAULT_PLAN
    display_plan(plan)
    plan = edit_priorities(plan)
    display_plan(plan)
    export_csv(plan)


if __name__ == '__main__':
    main()
