import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_specials):
    selected_sets = []
    if use_lower: selected_sets.append(string.ascii_lowercase)
    if use_upper: selected_sets.append(string.ascii_uppercase)
    if use_digits: selected_sets.append(string.digits)
    if use_specials: selected_sets.append(string.punctuation)

    if not selected_sets:
        return None

    password = [random.choice(char_set) for char_set in selected_sets]
    remaining_length = length - len(password)
    all_chars = ''.join(selected_sets)
    password += random.choices(all_chars, k=remaining_length)
    random.shuffle(password)
    return ''.join(password)

def assess_strength(password):
    score = 0
    length = len(password)
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    if length >= 12: score += 1
    if length >= 16: score += 1
    percent = int((score / 6) * 100)
    if percent < 40: return percent, "danger", "Weak"
    elif percent < 70: return percent, "warning", "Moderate"
    elif percent < 90: return percent, "info", "Strong"
    else: return percent, "success", "Very Strong"
