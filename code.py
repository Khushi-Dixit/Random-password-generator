import secrets

def generate_custom_password():
    # Take user inputs
    name = input("Enter your name: ")
    dob = input("Enter your date of birth (only numbers): ")
    symbol = input("Enter your favorite symbol: ")

    # Combine user inputs to form a base for the password
    base_password = name.lower() + dob + symbol

    # Ensure the first letter is capitalized
    if len(base_password) > 0:
        base_password = base_password.capitalize()

    # Ask for desired password length
    password_len = int(input("Enter the desired length of your password: "))

    # Ensure length is sufficient to include at least name, dob, and symbol
    if password_len < len(base_password):
        print(f"Error: Password length should be at least {len(base_password)} to include all inputs.")
        return

    # Repeat the base_password to reach the desired length
    while len(base_password) < password_len:
        base_password += base_password  # Repeat the base password
    base_password = base_password[:password_len]  # Truncate to desired length

    # Shuffle the password (excluding the first character)
    password_body = list(base_password[1:])  # Exclude the first character from shuffling
    secrets.SystemRandom().shuffle(password_body)  # Secure shuffle
    final_password = base_password[0] + ''.join(password_body)

    print("Generated Password:", final_password)

# Call the function to generate a custom password
generate_custom_password()
