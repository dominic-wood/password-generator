import tkinter as tk
from ttkbootstrap import Style

def create_theme_toggle(root, style):
    icon_var = tk.StringVar(value="🌙")

    def toggle_theme():
        if style.theme.name == "yeti":
            style.theme_use("darkly")
            icon_var.set("☀️")
        else:
            style.theme_use("yeti")
            icon_var.set("🌙")

    button = tk.Button(root, textvariable=icon_var, command=toggle_theme, width=2)
    button.place(relx=1.0, rely=1.0, x=-20, y=-20, anchor="se")
    return button
