import re

def check_password_strength(password):
    strength = 0
    remarks = ""
    
    if len(password) >= 8:
        strength += 1  # Length Check
    if re.search(r"[A-Z]", password):
        strength += 1  # Uppercase Letter
    if re.search(r"[a-z]", password):
        strength += 1  # Lowercase Letter
    if re.search(r"\d", password):
        strength += 1  # Digit Check
    if re.search(r"[!@#$%^&*()_+]", password):
        strength += 1  # Special Characters
    
    if strength == 5:
        remarks = "Very Strong ...💪..."
    elif strength >= 3:
        remarks = "Medium ...👍..."
    else:
        remarks = "Weak ...⚠️..."
    
    return f"Password Strength: {remarks}"

password = input("Enter Password:- ")
print(check_password_strength(password))
