# This is a program designed to generate a password that fits the
# requirements of 75% of websites and is only 8 characters long.
 
import random
import string

def generate_Password(length = 8):
    char_sets = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation
    ]

    password = [random.choice(char_set) for char_set in char_sets]

    all_chars = ''.join(char_sets)
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the list to avoid predictable sequences
    random.shuffle(password)

    # Join the list into a string and return it
    return ''.join(password)

print("Password:",generate_Password(8))