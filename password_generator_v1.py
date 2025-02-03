import re
import secrets #this is more secure and random than importing 'random'
import string


def generate_password(length, nums, special_chars, uppercase, lowercase):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        # r before the expression means regex
        constraints = [
            (nums, r'\d'),
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),            
            (special_chars, fr'[{symbols}]')            
        ]

        # Check constraints by adding a FOR loop and a COUNT variable
        count = 0
        for constraint, pattern in constraints:
            if constraint <= len(re.findall(pattern, password)):
                count += 1
            
        if count == 4:
            break

    return password

new_password = generate_password(8, 1, 1, 1, 1)  #length, nums, lowercase, uppercase, and special characters
print(new_password)
