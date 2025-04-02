import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_specials=True):
    # Base character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    specials = string.punctuation if use_specials else ''

    # Combine selected character sets
    all_chars = lower + upper + digits + specials
    if not all_chars:
        raise ValueError("No characters available to generate password. Enable at least one character set.")

    # Ensure at least one of each selected type is in the password
    password = []
    if use_uppercase:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_specials:
        password.append(random.choice(specials))
    password.append(random.choice(lower))  # Always include at least one lowercase

    # Fill the rest of the password
    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)

# Example usage
print(generate_password(length=16))
