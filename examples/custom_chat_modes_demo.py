"""Demo Custom Chat Modes: define un modo y lo aplica a una conversación simulada.

Ejecuta:
  py .\examples\custom_chat_modes_demo.py
"""
import json


MODE = {
    'name': 'Soporte Técnico',
    'system_message': 'Eres un asistente de soporte técnico con conocimiento en redes y Linux. Responde en español, tono claro.'
}


def save_mode(mode, path='examples/custom_mode.json'):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(mode, f, ensure_ascii=False, indent=2)
    print(f'Modo guardado en {path}')


def simulate_conversation(mode):
    print('Mensaje de sistema:', mode['system_message'])
    print('\nUsuario: No puedo conectar al servidor SSH')
    print('Asistente: Comprueba que el puerto 22 esté abierto y que el servicio sshd esté en ejecución. Usa `systemctl status sshd`.')


def main():
    simulate_conversation(MODE)
    save_mode(MODE)


if __name__ == '__main__':
    main()
