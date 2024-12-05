import json
import os

settings_path_file = "D:\\Visual Studio Code\\Python\\Password Manager\\Settings.json"
passwords_path_file = "D:\\Visual Studio Code\\Python\\Password Manager\\Passwords.txt"

def create_settings_file():
    if os.path.exists(settings_path_file) or os.path.exists(passwords_path_file):
        return
    else:
        with open(settings_path_file, "w") as file:
            file.write("{}")
        with open(passwords_path_file, "w") as file_txt:
            file_txt.write("")

def add_settings_to_file():
    switch_case = True if input("Do you want to use default settings? (y/n): ") == "y" else False
    print("\n")
    if switch_case:
        print("Using default settings\n")
        default_settings()
    else:
        print("Using custom settings\n")
        custom_settings()
    
def default_settings():
    settings = {
    "settings_path_file": settings_path_file,
    "password_path_file": passwords_path_file,
    "password_length": 8,
    "has_digits": True,
    "has_upper_chars": True,
    "has_especial_chars": True,
    "has_only_upper_chars": False,
    "has_only_digits": False,
    "has_only_especial_chars": False
    }
    with open(settings_path_file, "w") as file:
        json.dump(settings, file, indent = 4)

def custom_settings():
    try:
        length = int(input("Enter the length of the password: "))
        print("\n")
        has_digits = True if input("Do you want to include digits in the password? (y/n): ").lower() == "y" else False
        print("\n")
        has_upper_chars = True if input("Do you want to include uppercase letters in the password? (y/n): ").lower() == "y" else False
        print("\n")
        has_especial_chars = True if input("Do you want to include special characters in the password? (y/n): ").lower() == "y" else False
        print("\n")
        has_only_upper_chars = True if input("Do you want to include only uppercase letters in the password? (y/n): ").lower() == "y" else False
        print("\n")
        has_only_digits = True if input("Do you want to include only digits in the password? (y/n): ").lower() == "y" else False
        print("\n")
        has_only_especial_chars = True if input("Do you want to include only special characters in the password? (y/n): ").lower() == "y" else False
        print("\n")
    except ValueError:
        print("Invalid input, using default values:\n")
        print(
            f"Password length: 8\n"
            f"Include digits: Yes\n"
            f"Include uppercase letters: Yes\n"
            f"Include special characters: Yes\n"
            f"Include only uppercase letters: No\n"
            f"Include only digits: No\n"
            f"Include only special characters: No\n"
        )
        default_settings()

    if has_only_upper_chars:
        has_digits = False
        has_especial_chars = False
        has_only_especial_chars = False
        has_only_digits = False

    elif has_only_especial_chars:
        has_digits = False
        has_upper_chars = False
        has_only_upper_chars = False
        has_only_digits = False

    elif has_only_digits:
        has_upper_chars = False
        has_only_upper_chars = False
        has_especial_chars = False
        has_only_especial_chars = False

    settings = {
        "settings_path_file": settings_path_file,
        "password_path_file": passwords_path_file,
        "password_length": length,
        "has_digits": has_digits,
        "has_upper_chars": has_upper_chars,
        "has_especial_chars": has_especial_chars,
        "has_only_upper_chars": has_only_upper_chars,
        "has_only_digits": has_only_digits,
        "has_only_especial_chars": has_only_especial_chars
    }
    with open(settings_path_file, "w") as file:
        json.dump(settings, file, indent = 4)