import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    alphabet = ""
    if use_uppercase:
        alphabet += string.ascii_uppercase
    if use_lowercase:
        alphabet += string.ascii_lowercase
    if use_digits:
        alphabet += string.digits
    if use_special:
        alphabet += string.punctuation

    generated_password = ''.join(random.choice(alphabet) for _ in range(length))
    return generated_password

def main():
    try:
        password_length = int(input("Enter desired password length: "))
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(password_length, use_upper, use_lower, use_digits, use_special)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()