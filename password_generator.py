import random
import string
import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap import ttk

def generate_password(*args):
    length = int(length_var.get())
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_specials = specials_var.get()

    selected_sets = []
    if use_lower:
        selected_sets.append(string.ascii_lowercase)
    if use_upper:
        selected_sets.append(string.ascii_uppercase)
    if use_digits:
        selected_sets.append(string.digits)
    if use_specials:
        selected_sets.append(string.punctuation)

    if not selected_sets:
        password_var.set("Please select at least one option.")
        strength_bar.configure(value=0, bootstyle="secondary")
        return

    # Guarantee inclusion of at least one character from each selected set
    password = [random.choice(char_set) for char_set in selected_sets]
    
    # Fill the rest of the password
    remaining_length = length - len(password)
    all_chars = ''.join(selected_sets)
    password += random.choices(all_chars, k=remaining_length)

    # Shuffle the password list and convert to string
    random.shuffle(password)
    password_str = ''.join(password)

    password_var.set(password_str)
    update_strength_meter(password_str)


def update_strength_meter(password):
    score = 0
    length = len(password)

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1

    percent = int((score / 6) * 100)

    if percent < 40:
        style = "danger"
    elif percent < 70:
        style = "warning"
    elif percent < 90:
        style = "info"
    else:
        style = "success"

    strength_bar.configure(value=percent, bootstyle=style)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()

def update_length_label(*args):
    length_display.config(text=f"{int(length_var.get())} characters")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

style = Style(theme="yeti")
frame = ttk.Frame(root, padding=20)
frame.pack()

# Password Length Slider
ttk.Label(frame, text="Password Length:").grid(row=0, column=0, sticky="w")
length_var = tk.DoubleVar(value=12)
length_slider = ttk.Scale(frame, from_=4, to=64, variable=length_var, command=generate_password, length=200)
length_slider.grid(row=0, column=1, sticky="ew", pady=5)

length_display = ttk.Label(frame, text="12 characters")
length_display.grid(row=1, column=1, sticky="e")
length_var.trace_add("write", update_length_label)

# Options
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
specials_var = tk.BooleanVar(value=True)

ttk.Checkbutton(frame, text="Include Uppercase", variable=upper_var).grid(row=2, column=0, sticky="w")
ttk.Checkbutton(frame, text="Include Lowercase", variable=lower_var).grid(row=2, column=1, sticky="w")
ttk.Checkbutton(frame, text="Include Numbers", variable=digits_var).grid(row=3, column=0, sticky="w")
ttk.Checkbutton(frame, text="Include Symbols", variable=specials_var).grid(row=3, column=1, sticky="w")

# Buttons
ttk.Button(frame, text="Generate Password", command=generate_password, bootstyle="primary", width=20).grid(row=4, column=0, sticky="ew", padx=(0, 5), pady=10)
ttk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard, bootstyle="info-outline", width=20).grid(row=4, column=1, sticky="ew", padx=(5, 0), pady=10)

# Password Output + Strength Bar
password_var = tk.StringVar()
ttk.Entry(frame, textvariable=password_var, width=40).grid(row=5, column=0, columnspan=2, pady=(0, 5))

strength_bar = ttk.Progressbar(frame, maximum=100, mode='determinate', bootstyle="secondary")
strength_bar.grid(row=6, column=0, columnspan=2, sticky="ew", pady=(2, 10))

# Reactive triggers
for var in (upper_var, lower_var, digits_var, specials_var):
    var.trace_add("write", generate_password)

# Initial generation
generate_password()

root.mainloop()
