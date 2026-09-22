from app.users import create_user, validate_email

def test_create_user():
    user = create_user("sarvesh", "sarvesh@example.com")
    assert user["username"] == "sarvesh"

def test_invalid_user():
    assert create_user("", "test@example.com") is None

def test_validate_email():
    assert validate_email("test@example.com") is True
