import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''

    all_chars = lowercase_letters + uppercase_letters + numbers + special_chars
    if not all_chars:
        raise ValueError('At least one character set must be enabled')

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

length = int(input('Enter password length: '))
use_uppercase = input('Use uppercase letters? (y/n): ').lower() == 'y'
use_numbers = input('Use numbers? (y/n): ').lower() == 'y'
use_special_chars = input('Use special characters? (y/n): ').lower() == 'y'

print(generate_password(length, use_uppercase, use_numbers, use_special_chars))