"""Script de demostración para Modos de chat.

Simula una sesión multi-turn con un mensaje de sistema inicial y cambios de comportamiento.
"""

def simulate_chat():
    system = 'Eres un asistente técnico que responde en español, tono claro y conciso.'
    print('Mensaje de sistema:', system)

    # Turn 1
    user1 = 'Hola, necesito configurar un servidor web en Ubuntu.'
    print('\nUsuario:', user1)
    assistant1 = 'Para configurar un servidor web en Ubuntu, instala Nginx con `sudo apt install nginx` y configura /etc/nginx/sites-available.'
    print('Asistente:', assistant1)

    # Turn 2 (user adds context)
    user2 = 'Perfecto. ¿Y cómo activo HTTPS con Let\'s Encrypt? Mi dominio es example.com.'
    print('\nUsuario:', user2)
    assistant2 = 'Usa Certbot: `sudo apt install certbot python3-certbot-nginx` y luego `sudo certbot --nginx -d example.com`. Asegúrate de abrir puertos 80 y 443.'
    print('Asistente:', assistant2)

    # Change behavior: temporary instruction
    print('\n-- Instrucción temporal: responde ahora en formato de lista corta --')
    user3 = 'Resume los pasos anteriores en 3 bullets.'
    print('\nUsuario:', user3)
    assistant3 = '- Instalar Nginx; - Instalar Certbot; - Ejecutar Certbot para emitir certificado y configurar HTTPS.'
    print('Asistente (lista):', assistant3)


if __name__ == '__main__':
    simulate_chat()
