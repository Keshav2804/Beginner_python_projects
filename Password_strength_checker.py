#Password strngth checker
def password_strength(password):
    special_characters = "!@#$%^&*()"
    length = len(password)
    
    # Conditions
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in special_characters for char in password)
    
    # Checking the strength
    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length >= 6 and (has_upper or has_lower) and (has_digit or has_special):
        return "Medium"
    else:
        return "Weak"

# Example usage
print(password_strength("Abc123!"))  # Medium
print(password_strength("Abcdef!1"))  # Strong
print(password_strength("abc"))       # Weak
