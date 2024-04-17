import random
import string
import argparse

def generate_password(length, include_uppercase=False, include_digits=False, include_special_chars=False):
    chars = string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_digits:
        chars += string.digits
    if include_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description='Password Generator CLI')
    parser.add_argument('length', type=int, help='Length of the password')
    parser.add_argument('-u', '--include-uppercase', action='store_true', help='Include uppercase letters')
    parser.add_argument('-d', '--include-digits', action='store_true', help='Include digits')
    parser.add_argument('-s', '--include-special-chars', action='store_true', help='Include special characters')

    args = parser.parse_args()

    password = generate_password(args.length, args.include_uppercase, args.include_digits, args.include_special_chars)
    print(password)

if __name__ == "__main__":
    main()
