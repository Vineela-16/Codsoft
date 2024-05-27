import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1"
    
    # Defining the characters for generating the password:
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generating a random password of specified length:
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the length for the password: "))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        return
    
    password = generate_password(length)
    print(f"Generated Password: {password}")

main()

