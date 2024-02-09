import sys
import random
import string

def generate_password(length=12, special_characters=True):
    characters = string.ascii_letters + string.digits
    if special_characters:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12, special_characters=True):
    passwords = [generate_password(length, special_characters) for _ in range(num_passwords)]
    return passwords

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            num_passwords = int(sys.argv[1])
        except ValueError:
            print("Veuillez entrer un nombre entier valide. Utilisation de 1 mot de passe.")
            num_passwords = 1
    else:
        num_passwords = 1

    if len(sys.argv) > 2:
        try:
            password_length = int(sys.argv[2])
        except ValueError:
            print("Veuillez entrer un nombre entier valide. Utilisation de la longueur par défaut (12).")
            password_length = 12
    else:
        password_length = 12

    include_special_characters = "--no-special" not in sys.argv

    generated_passwords = generate_multiple_passwords(num_passwords, password_length, include_special_characters)

    print(f"Mots de passe générés ({num_passwords}):")
    for password in generated_passwords:
        print(password)
