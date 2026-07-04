import re

def check_password(password):
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2

    common = ["password", "123456", "admin", "qwerty"]

    if password.lower() not in common:
        score += 2

    if score >= 8:
        strength = "Very Strong"
    elif score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Medium"
    else:
        strength = "Weak"

    return score, strength

password = input("Enter Password: ")

score, strength = check_password(password)

print("Strength:", strength)
