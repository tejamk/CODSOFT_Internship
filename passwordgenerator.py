import random
import string


def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters randomly
    password = ''.join(random.choice(characters) for i in range(length))

    return password


# Take user input for password length
try:
    length = int(input("Enter the length of the password: "))
    if length <= 0:
        print("Please enter a positive integer for password length.")
    else:
        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid integer for password length.")