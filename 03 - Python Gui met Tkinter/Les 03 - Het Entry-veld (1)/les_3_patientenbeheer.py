"""
Python Gui met Tkinter - Les 3 - Het Entry-veld (1)

Als een gebruiker de inlogpagina opstart, kan hij inloggen. Als dat lukt, gaat de gebruiker naar het, nog lege, form.

Heeft de gebruiker geen registratie, dan kan hij op de knop ‘Registreren’ drukken en komt dan op de pagina ‘Registreren’.

De opdracht houdt in dat u deze schermen bouwt, dat het registratiescherm zijn data opslaat in een bestand en dat deze weer ingelezen worden om te kunnen controleren of de gebruiker bestaat.

1. Bouw de applicatie zo uit dat het lijkt op een zo goed mogelijk werkende beginpagina van een ziekenhuissysteem. Dus: login, registratie en een derde lege form waar men terechtkomt.
2. Controleer in de registratie de vorm van het e-mailadres.
3. Controleer of ze hetzelfde zijn.
4. Ga daarna terug naar de inlogpagina.
5. Login op een lege pagina.
"""

import json
import re
from pathlib import Path
from tkinter import Tk, Frame, StringVar, Label, Button, ttk, FLAT

USERS_FILE = Path(__file__).parent / "gebruikers.json"

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def show_login_screen(status_message="", focus_password=False):
    clear_window()

    global status_label

    root.title("Inloggen patiëntenbeheer - Streekziekenhuis de Blauwe Berg")
    root.geometry("400x300")

    Label(root, text="Streekziekenhuis de Blauwe Berg", bg="#4E96D2", fg="#1E5593", font=("Arial", 18)).pack(pady=(10,0))
    Label(root, text="Welkom bij het patiëntenbeheer", bg="#4E96D2", fg="white", font=("Arial", 14)).pack(pady=(10,0))
    Label(root, text="Log in om verder te gaan of maak een nieuw account aan.", bg="#4E96D2", fg="white", font=("Arial", 10)).pack(pady=(0,10))
    
    loginform = Frame(root, bg="#4E96D2")
    loginform.pack(padx=10, pady=10, fill="both", expand=True)

    loginform.columnconfigure(0, weight=0)
    loginform.columnconfigure(1, weight=1)

    status_label = Label(loginform, text="", bg="#f8d7da", bd=1, fg="#721c24", font=("Arial", 10), padx=8, pady=4, anchor="w")
    status_label.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="ew")
    status_label.grid_remove()

    if status_message:
        show_status(status_message, success=True)

    label_email = Label(loginform, text="Email:", fg="white", bg="#4E96D2", anchor="e")
    label_email.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    entry_email = ttk.Entry(loginform, textvariable=login_email, style="Padded.TEntry")
    entry_email.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    label_password = Label(loginform, text="Wachtwoord:", fg="white", bg="#4E96D2", anchor="e")
    label_password.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    entry_password = ttk.Entry(loginform, textvariable=login_password, show="*", style="Padded.TEntry")
    entry_password.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    entry_password.bind("<Return>", login)
    
    if focus_password:
        entry_password.focus()
    else:
        entry_email.focus()

    buttons = Frame(loginform, bg="#4E96D2")
    buttons.grid(row=3, column=1, padx=5, pady=10, sticky="w")

    button_login = Button(buttons, text="Inloggen", fg="white", bg="#1E5593", relief=FLAT, command=login, padx=10, pady=5)
    button_login.grid(row=0, column=0, padx=(0, 5))

    button_register = Button(buttons, text="Registreren", fg="white", bg="#1E5593", relief=FLAT, command=show_register_screen, padx=10, pady=5)
    button_register.grid(row=0, column=1)

def login(event=None):
    login_email_value = login_email.get().strip()
    login_password_value = login_password.get()

    if login_email_value == "" or login_password_value == "":
        show_status("Vul uw e-mailadres en wachtwoord in.")
        return

    users = load_users()

    if len(users) == 0:
        show_status("Er zijn nog geen gebruikers geregistreerd.")
        return

    for user in users:
        if (
            user["email"] == login_email_value
            and user["password"] == login_password_value
        ):
            show_dashboard_screen()
            return

    show_status("Ongeldige inloggegevens.")
    login_password.set("")

def show_dashboard_screen():
    clear_window()

    root.title("Dashboard patiëntenbeheer - Streekziekenhuis de Blauwe Berg")
    root.geometry("800x600")

    dashboard = Frame(root, bg="#4E96D2")
    dashboard.pack(fill="both", expand=True)

    Label(dashboard, text="Dashboard patiëntenbeheer", bg="#4E96D2", fg="white", font=("Arial", 14)).pack(pady=20)

    Button(dashboard, text="Uitloggen", fg="white", bg="#1E5593", relief=FLAT, command=show_login_screen, padx=10, pady=5).pack()

def show_register_screen():
    clear_window()

    global status_label

    root.title("Registreren patiëntenbeheer - Streekziekenhuis de Blauwe Berg")
    root.geometry("400x300")

    registerform = Frame(root, bg="#4E96D2")
    registerform.pack(padx=10, pady=10, fill="both", expand=True)

    registerform.columnconfigure(0, weight=0)
    registerform.columnconfigure(1, weight=1)

    Label(registerform, text="Maak hier een nieuw account aan.", bg="#4E96D2", fg="white", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=(0, 15), sticky="ew")

    status_label = Label(registerform, text="", bg="#f8d7da", bd=1, fg="#721c24", font=("Arial", 10), padx=8, pady=4, anchor="w")
    status_label.grid(row=1, column=0, columnspan=2, padx=5, pady=(0, 10), sticky="ew")
    status_label.grid_remove()

    label_email = Label(registerform, text="E-mailadres:", fg="white", bg="#4E96D2", anchor="e")
    label_email.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    entry_email = ttk.Entry(registerform, textvariable=register_email, style="Padded.TEntry")
    entry_email.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

    label_email_repeat = Label(registerform, text="Herhaal e-mailadres:", fg="white", bg="#4E96D2", anchor="e")
    label_email_repeat.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    entry_email_repeat = ttk.Entry(registerform, textvariable=register_email_repeat, style="Padded.TEntry")
    entry_email_repeat.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

    label_password = Label(registerform, text="Wachtwoord:", fg="white", bg="#4E96D2", anchor="e")
    label_password.grid(row=4, column=0, padx=5, pady=5, sticky="e")

    entry_password = ttk.Entry(registerform, textvariable=register_password, show="*", style="Padded.TEntry")
    entry_password.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

    label_password_repeat = Label(registerform, text="Herhaal wachtwoord:", fg="white", bg="#4E96D2", anchor="e")
    label_password_repeat.grid(row=5, column=0, padx=5, pady=5, sticky="e")

    entry_password_repeat = ttk.Entry(registerform, textvariable=register_password_repeat, show="*", style="Padded.TEntry")
    entry_password_repeat.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

    buttons = Frame(registerform, bg="#4E96D2")
    buttons.grid(row=6, column=1, padx=5, pady=10, sticky="w")

    button_register = Button(buttons, text="Registreren", fg="white", bg="#1E5593", relief=FLAT, command=register, padx=10, pady=5)
    button_register.grid(row=0, column=0, padx=(0, 5))

    button_login = Button(buttons, text="Terug naar login", fg="white", bg="#1E5593", relief=FLAT, command=show_login_screen, padx=10, pady=5)
    button_login.grid(row=0, column=1)

def register():
    register_email_value = register_email.get().strip()
    register_email_repeat_value = register_email_repeat.get().strip()
    register_password_value = register_password.get()
    register_password_repeat_value = register_password_repeat.get()

    if (
        register_email_value == ""
        or register_email_repeat_value == ""
        or register_password_value == ""
        or register_password_repeat_value == ""
    ):
        show_status("Vul alle velden in.")
        return

    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(email_pattern, register_email_value):
        show_status("Vul een geldig e-mailadres in.")
        return

    if register_email_value != register_email_repeat_value:
        show_status("De e-mailadressen zijn niet gelijk.")
        return

    if register_password_value != register_password_repeat_value:
        show_status("De wachtwoorden zijn niet gelijk.")
        return

    users = load_users()

    for user in users:
        if user["email"] == register_email_value:
            show_status("Dit e-mailadres is al geregistreerd.")
            return

    new_user = {
        "email": register_email_value,
        "password": register_password_value
    }

    users.append(new_user)
    save_users(users)

    login_email.set(register_email_value)
    login_password.set("")

    register_email.set("")
    register_email_repeat.set("")
    register_password.set("")
    register_password_repeat.set("")

    show_login_screen("Registratie succesvol! U kunt nu inloggen.",  focus_password=True)

def show_status(message, success=False):
    if success:
        status_label.config(text=message, bg="#d4edda", fg="#155724")
    else:
        status_label.config(text=message, bg="#f8d7da", fg="#721c24")

    status_label.grid()

def load_users():
    if not USERS_FILE.exists():
        return []

    with open(USERS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

root = Tk()

style = ttk.Style()
style.configure("Padded.TEntry", padding=4)

root.configure(bg="#4E96D2")

login_email = StringVar()
login_password = StringVar()

register_email = StringVar()
register_email_repeat = StringVar()
register_password = StringVar()
register_password_repeat = StringVar()

# register_email.set("john@doe.com")
# register_email_repeat.set("john@doe.com")
# register_password.set("1234567890")
# register_password_repeat.set("1234567890")

show_login_screen()

root.mainloop()