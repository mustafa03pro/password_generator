import random
import string

def generate_password(length=12):
    """
    Generate a random password using letters, digits, and special characters.

    Parameters:
    length (int): Length of the password (default is 12).

    Returns:
    str: A randomly generated password.
    """
    # Define the character categories
    char_categories = {
        "lowercase": list(string.ascii_lowercase),
        "uppercase": list(string.ascii_uppercase),
        "digits": list(string.digits),
        "special": list("!@#$%^&*()-_=+[]{}|;:,.<>?/")
    }

    # Ensure each category is included at least once
    password_chars = [
        random.choice(char_categories["lowercase"]),
        random.choice(char_categories["uppercase"]),
        random.choice(char_categories["digits"]),
        random.choice(char_categories["special"])
    ]

    # Add remaining characters randomly
    all_chars = list(set(sum(char_categories.values(), [])))  # Convert to list for random.sample
    remaining_length = length - len(password_chars)

    password_chars += random.sample(all_chars, remaining_length)

    # Shuffle the password characters
    random.shuffle(password_chars)

    # Join the characters into a single string
    password = ''.join(password_chars)
    return password

# Main program
def main():
    print("Welcome to the Random Password Generator!")
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        if length < 4:
            print("Password length must be at least 4 characters.")
        else:
            password = generate_password(length)
            print(f"Your new password is: {password}")
    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
