import string
import random
import json
import create_settings_file
import Verify_Password_Security

class Password_Manager:
    def __init__(self):
        self.asscii_digits = string.digits
        self.asscii_upper_chars = string.ascii_uppercase
        self.asscii_lower_chars = string.ascii_lowercase
        self.asscii_especial_chars = string.punctuation
        self.save = "D:\\Visual Studio Code\\Python\\Password Manager\\Passwords.txt"
    
    def create_password(self, settings):
        self.settings = settings

        self.length = self.settings["password_length"]
        self.upper_chars = self.settings["has_upper_chars"]
        self.digits = self.settings["has_digits"]
        self.especial_chars = self.settings["has_especial_chars"]
        self.only_upper_chars = self.settings["has_only_upper_chars"]
        self.only_digits = settings["has_only_digits"]
        self.only_especial_chars = settings["has_only_especial_chars"]
        
        if self.upper_chars and self.digits and self.especial_chars:
            password_chars = self.asscii_digits + self.asscii_upper_chars + self.asscii_especial_chars + self.asscii_lower_chars

        elif self.upper_chars and self.digits:
            password_chars = self.asscii_digits + self.asscii_upper_chars + self.asscii_lower_chars

        elif self.upper_chars and self.especial_chars:
            password_chars = self.asscii_upper_chars + self.asscii_especial_chars + self.asscii_lower_chars

        elif self.only_digits:
            password_chars = self.asscii_digits

        elif self.only_upper_chars:
            password_chars = self.asscii_upper_chars

        elif self.only_especial_chars:
            password_chars = self.asscii_especial_chars

        else:
            password_chars = self.asscii_lower_chars

        password = "".join(random.choice(password_chars) for i in range(self.length))
        if Verify_Password_Security.verify_password_security(password) == "WEAK" or Verify_Password_Security.verify_password_security(password) == "SO WEAK" or Verify_Password_Security.verify_password_security(password) == "MID":
            print("\nPassword isn't safe!!\n")
            improve = True if input("Do you want to improve password security? (y/n): ").lower() == "y" else False
            if improve:
                print("\n")
                suggest = Verify_Password_Security.suggest_safe_password()
                print(f"\nPassword suggested is: {suggest}\n")
                if input("Do you want to continue? (y/n): ").lower() == "y":
                    password = suggest
                    print("\n")
        print("\nPassword created successfully")
        print(f"Password created is: {password}\n")
        with open(self.save, "a") as file:
            file.write(password)

    def view_all_passwords(self):
        with open(self.save, "r") as file:
            lines = file.readlines()
            if lines:
                for line in lines:
                    print(line)
            else:
                print("No passwords created yet\n")

    def modify_password(self, identifier):
        with open(self.save, "r") as file:
            lines = file.readlines()

        if identifier < 0 or identifier >= len(lines):
            print("Invalid identifier. Try again\n")
            return
        else:
            new_password = input("Enter the new password: ")
            if Verify_Password_Security.verify_password_security(new_password) == "WEAK" or Verify_Password_Security.verify_password_security(new_password) == "SO WEAK" or Verify_Password_Security.verify_password_security(new_password) == "MID":
                print("\nPassword isn't safe!!\n")
                improve = True if input("Do you want to improve password security? (y/n): ").lower() == "y" else False
                if improve:
                    print("\n")
                    suggest = Verify_Password_Security.suggest_safe_password()
                    print(f"\nPassword suggested is: {suggest}\n")
                    if input("Do you want to continue? (y/n): ").lower() == "y":
                        new_password = suggest
                        print("\n")

        with open(self.save, "w") as file:
            lines[identifier] = new_password
            file.writelines(lines)
        print("Password changed successfully\n")
        print(f"New password is: {new_password}\n")
    
    def delete_password(self, identifier):
        with open(self.save, "r") as file:
            lines = file.readlines()
            if identifier < 0 or identifier > len(lines):
                print("Invalid identifier. Try again\n")
                return
        
        with open(self.save, "w") as file:
            overwrite_file = [line for index, line in enumerate(lines) if index != identifier]
            file.writelines(overwrite_file)
        print("Password deleted successfully\n")

def main():
    create_settings_file.create_settings_file()
    password_manager = Password_Manager()
    settings_path_file = "D:\\Visual Studio Code\\Python\\Password Manager\\Settings.json"
    while True:
        print(
            "What do you want to do?\n"
            "1. Create a password\n"
            "2. View all the passwords created\n"
            "3. Modify a password\n"
            "4. Delete a password\n"
            "5. Quit\n"
        )
        while True:
            try:
                choose_option = int(input("Choose an option (1-5): "))
                if choose_option < 1 or choose_option > 5:
                    print("\nValue is lower or higher. Please try again\n")
                else:
                    break
            except ValueError:
                print("\n")
                print("Invalid value. Please try again\n")
                print("\n")
                continue
            except KeyboardInterrupt:
                print("\n")
                print("Operation cancelled successfully\n")
                print("\n")
                print(
                    "What do you want to do?\n"
                    "1. Create a password\n"
                    "2. View all the passwords created\n"
                    "3. Modify a password\n"
                    "4. Delete a password\n"
                    "5. Quit\n"
                )

        try:
            if choose_option == 1:
                print("\n")
                create_settings_file.add_settings_to_file()
                try:
                    with open(settings_path_file, "r") as file:
                        settings_file = json.load(file)
                except json.JSONDecodeError:
                    print("An error had ocurred during executing json file. Please, try again later\n")
                    return
                password_manager.create_password(settings_file)
    
            elif choose_option == 2:
                print(" PASSWORDS! ".center(30, "-") + "\n")
                password_manager.view_all_passwords()
                print("\n")
        
            elif choose_option == 3:
                password_manager.view_all_passwords()
                print("\n")
                try:
                    identifier = int(input("Enter the identifier of the password (The line number of the password): "))
                except ValueError:
                    print("Invalid input. Try again\n")
                print("\n")
                file_modify = identifier - 1
                password_manager.modify_password(file_modify)
    
            elif choose_option == 4:
                password_manager.view_all_passwords()
                print("\n")
                try:
                    identifier = int(input("Enter the identifier of the password (The line number of the password): "))
                except ValueError:
                    print("Invalid input. Try again\n")
                print("\n")
                file_delete = identifier - 1
                password_manager.delete_password(file_delete)

            elif choose_option == 5:
                print("Bye!\n")
                input("Press enter to continue...\n")
                exit()
        except (KeyboardInterrupt, InterruptedError):
            print("\n")
            print("Operation cancelled successfully\n")

if __name__ == "__main__":
    print("Welcome to the password manager\n")
    main()