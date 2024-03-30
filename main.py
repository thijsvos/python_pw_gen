import random
import sys

def generate_password(length: int, characters: str) -> str:
    """
    Generate a random password of a given length from a set of characters.

    Parameters:
    length (int): The length of the password.
    characters (str): The characters to use in the password.

    Returns:
    str: The generated password.
    """
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    """
    Main function to handle command line arguments and generate the password.
    """
    # Default password length
    password_length = 12

    # Check if a command line argument is provided
    if len(sys.argv) > 1:
        try:
            # Try to convert the argument to an integer
            password_length = int(sys.argv[1])
        except ValueError:
            # If the argument is not a valid integer, print a warning and use the default length
            print("Invalid input. Using default length of 12.")

    # The characters to use in the password
    characters = "abcdefghjkmnpqrstuvwxyz123456789ABCDEFGHJKLMNPQRSTUVWXYZ!?#$%&*()"

    # Generate and print the password
    print(generate_password(password_length, characters))

# Ensure that main() is only called when the script is run directly, not when it is imported as a module
if __name__ == "__main__":
    main()
