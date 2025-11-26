def authenticate(username, password):
    # Simulación simple: usuario 'student' y password 'secret'
    if username == 'student' and password == 'secret':
        return 'fake-jwt-token-123'
    return None
