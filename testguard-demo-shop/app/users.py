def create_user(username, email):
    if not username or not email:
        return None
    return {"username": username, "email": email}

def validate_email(email):
    return "@" in email and "." in email
