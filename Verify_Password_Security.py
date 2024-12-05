import string
import random

def verify_password_security(password):
    digits = string.digits
    upper_chars = string.ascii_uppercase
    symbols = string.punctuation
    strikes = 0
    def has_one_digit(password):
        count = 0
        for i in password:
            if i in digits:
                count += 1
        return count > 0
    def has_one_upperchar(password):
        count = 0
        for i in password:
            if i in upper_chars:
                count += 1
        return count > 0
    def has_one_symbol(password):
        count = 0
        for i in password:
            if i in symbols:
                count += 1
        return count > 0
    
    if len(password) < 8:
        strikes += 1
    if not has_one_digit(password):
        strikes += 1
    if not has_one_upperchar(password):
        strikes += 1
    if not has_one_symbol(password):
        strikes += 1
    
    if strikes > 3:
        return "SO WEAK"
    elif strikes == 3:
        return "WEAK"
    elif strikes == 2:
        return "MID"
    elif strikes == 1:
        return "GOOD"
    elif strikes == 0:
        return "STRONG"
    
def suggest_safe_password():
    asscii_digits = string.digits
    asscii_upper_chars = string.ascii_uppercase
    asscii_lower_chars = string.ascii_lowercase
    asscii_especial_chars = string.punctuation

    passwd = asscii_digits + asscii_upper_chars + asscii_lower_chars + asscii_especial_chars
    password = "".join(random.choice(passwd) for i in range(8))
    return password