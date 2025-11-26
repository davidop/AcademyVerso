from auth import authenticate

def test_auth_success():
    assert authenticate('student', 'secret') == 'fake-jwt-token-123'

def test_auth_fail():
    assert authenticate('student', 'wrong') is None
