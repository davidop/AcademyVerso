"""Demo de Prompt Files: carga un prompt template, reemplaza variables y muestra el prompt final."""
from pathlib import Path

TEMPLATE = Path('prompts/prompt_files_demo.md')


def main():
    text = TEMPLATE.read_text(encoding='utf-8')
    text = text.replace('{{SERVICE_NAME}}', 'InventoryService')
    text = text.replace('{{OWNER}}', 'Equipo Backend')
    print('--- Prompt final ---')
    print(text)


if __name__ == '__main__':
    main()
