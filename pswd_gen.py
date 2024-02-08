import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Longueur du mot de passe (par défaut: 12) : ") or 12)
    generated_password = generate_password(password_length)
    print("Mot de passe généré :")
    print(generated_password)
