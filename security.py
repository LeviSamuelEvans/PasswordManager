import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    if not re.search("[a-z]", password):
        return "Weak"
    if not re.search("[A-Z]", password):
        return "Weak"
    if not re.search("[0-9]", password):
        return "Weak"
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak"
    return "Strong"
