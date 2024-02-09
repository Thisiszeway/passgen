import sys
import random
import string

def generate_password(length=12, special_characters=True, include_characters=None):
    characters = string.ascii_letters + string.digits
    if special_characters:
        characters += string.punctuation

    if include_characters:
        characters += ''.join(c for c in include_characters if c not in characters)

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12, special_characters=True, include_characters=None):
    passwords = [generate_password(length, special_characters, include_characters) for _ in range(num_passwords)]
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

    include_characters = None
    if "--include" in sys.argv:
        index = sys.argv.index("--include")
        if index + 1 < len(sys.argv):
            include_characters = sys.argv[index + 1]

    generated_passwords = generate_multiple_passwords(num_passwords, password_length, include_special_characters, include_characters)

    print(f"Mots de passe générés ({num_passwords}):")
    for password in generated_passwords:
        print(password)
