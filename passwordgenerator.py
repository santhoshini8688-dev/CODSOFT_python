import random
import string
def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return None
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        print("\nSelect Password Complexity:")
        print("1. Letters only")
        print("2. Letters and Numbers")
        print("3. Letters, Numbers, and Special Characters")
        complexity = int(input("Enter your choice (1-3): "))
        password = generate_password(length, complexity)
        if password:
            print("\nGenerated Password:")
            print(password)
        else:
            print("Invalid complexity choice.")
except ValueError:
    print("Please enter valid numeric input.")