import sys
import random
import string

def generate_password(length=12, special_characters=True):
    characters = string.ascii_letters + string.digits
    if special_characters:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            password_length = int(sys.argv[1])
        except ValueError:
            print("Veuillez entrer un nombre entier valide. Utilisation de la longueur par défaut (12).")
            password_length = 12
    else:
        password_length = 12

    include_special_characters = "--no-special" not in sys.argv

    generated_password = generate_password(password_length, include_special_characters)

    print("Mot de passe généré :")
    print(generated_password)
