import string
import random

def generate_password(length):
    """Generate a strong password of the specified length."""
    if length < 4:
        raise ValueError("Password length should be at least 4 characters to ensure complexity.")
    
    # Character sets for the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password contains at least one character from each set
    password_chars = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with a mix of all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password_chars += random.choices(all_characters, k=length - 4)

    # Shuffle the resulting list to ensure randomness
    random.shuffle(password_chars)

    # Join the list to form the final password
    password = ''.join(password_chars)
    return password

def main():
    """Main function to run the password generator."""
    print("Welcome to the Password Generator created by Ushaswini.......!")
    try:
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        print(f"Generated password is : {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
