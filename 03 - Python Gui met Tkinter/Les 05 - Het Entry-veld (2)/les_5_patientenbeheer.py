"""
Python Gui met Tkinter - Les 5 - Het Entry-veld (2)

De opdracht die bij deze les hoort, is dat u het derde scherm gaat voorzien van widgets.
U gaat de NAW-gegevens gebruiken om het registratiescherm in te vullen. NAW staat voor Naam, Adres en Woonplaats.
Bouw het derde scherm zodanig dat, als iemand aan de bovenkant, in de Combobox, zijn achternaam invult en op een Button drukt, de rest van de widgets gevuld worden met NAW-gegevens.
"""

import re
from pathlib import Path
import sqlite3
from tkinter import Tk, Frame, StringVar, Label, Button, ttk, FLAT

DATABASE_PATH = Path(__file__).parent / "database.db"

def get_connection():
    """
    Maakt een verbinding met de database en retourneert het connection-object.
    """
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        connection.row_factory = sqlite3.Row
        return connection

    except sqlite3.Error as error:
        print("Fout opgetreden bij verbinden met database:", error)
        return None


def database_fetch(query, parameters=(), fetch_one=False):
    """
    Voert een SELECT-query uit.
    Retourneert standaard alle resultaten.
    Als fetch_one=True is, retourneert de functie één resultaat.
    """
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, parameters)

            if fetch_one:
                return cursor.fetchone()

            return cursor.fetchall()

    except sqlite3.Error as error:
        print("Databasefout:", error)

        if fetch_one:
            return None

        return []


def database_execute(query, parameters=()):
    """
    Voert een INSERT, UPDATE of DELETE-query uit.
    Retourneert True als het gelukt is, anders False.
    """
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, parameters)
            connection.commit()
            return True

    except sqlite3.Error as error:
        print("Databasefout:", error)
        return False


def create_database_tables():
    """
    Maakt de benodigde tabellen in de database aan als deze nog niet bestaan en vult ze met testdata.
    """
    sqlite_create_accounts_query = """
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL);
    """

    sqlite_create_persoon_query = """
        CREATE TABLE IF NOT EXISTS persoon (
            idpersoon INTEGER PRIMARY KEY AUTOINCREMENT,
            voornaam VARCHAR(45) NOT NULL,
            tussenvoegsel VARCHAR(45) NULL,
            achternaam VARCHAR(255) NOT NULL,
            mobiel VARCHAR(23) NOT NULL);
    """

    sqlite_create_adres_query = """
        CREATE TABLE IF NOT EXISTS adres (
            idadres INTEGER PRIMARY KEY AUTOINCREMENT,
            straat VARCHAR(45) NOT NULL,
            huisnr VARCHAR(45) NOT NULL,
            postcode VARCHAR(45) NOT NULL,
            woonplaats VARCHAR(45) NOT NULL,
            idpersoon INTEGER NOT NULL);
    """

    sqlite_insert_accounts_query = """
        INSERT INTO accounts (email, password)
        VALUES
            ("john@doe.com", "test");
    """

    sqlite_insert_persoon_data = """
        INSERT INTO persoon (idpersoon, voornaam, tussenvoegsel, achternaam, mobiel)
        VALUES
            (1, "Jan", "de", "Vries", "0612345678"),
            (2, "Lisa",	"van", "Dijk", "0687654321"),
            (3, "Peter", NULL, "Jansen", "0645612378"),
            (4, "Emma",	"van der", "Meer", "0698123476"),
            (5, "Mark",	NULL,	"Bakker", "0634567890"),
            (6, "Sophie", "de",	"Boer", "0678945612"),
            (7, "Tom", "van", "Leeuwen", "0623459876"),
            (8, "Noor", NULL,	"Smit",	"0698765432"),
            (9, "Bram",	"ter", "Horst", "0611223344"),
            (10, "Mila", "van den", "Berg", "0655443322");
    """

    sqlite_insert_adres_data = """
        INSERT INTO adres (straat, huisnr, postcode, woonplaats, idpersoon)
        VALUES
            ("Kerkstraat", "12", "1234 AB", "Utrecht", 1),
            ("Stationsweg", "45", "2345 CD", "Amersfoort", 2),
            ("Dorpsstraat", "8", "3456 EF", "Zwolle", 3),
            ("Lindenlaan", "101", "4567 GH", "Haarlem", 4),
            ("Molenweg", "22", "5678 IJ", "Groningen", 5),
            ("Schoolstraat", "7", "6789 KL", "Breda", 6),
            ("Prinsenstraat", "34", "7890 MN", "Leiden", 7),
            ("Hoofdweg", "56", "8901 OP", "Tilburg", 8),
            ("Eikenlaan", "19", "9012 QR", "Nijmegen", 9),
            ("Marktstraat", "3", "1122 ST", "Arnhem", 10);
    """

    if not database_execute(sqlite_create_accounts_query):
        return

    if not database_execute(sqlite_create_persoon_query):
        return

    if not database_execute(sqlite_create_adres_query):
        return

    accounts_count = database_fetch("SELECT COUNT(*) FROM accounts", fetch_one=True)
    if accounts_count and accounts_count[0] == 0:
        database_execute(sqlite_insert_accounts_query)

    persoon_count = database_fetch("SELECT COUNT(*) FROM persoon", fetch_one=True)
    if persoon_count and persoon_count[0] == 0:
        database_execute(sqlite_insert_persoon_data)

    adres_count = database_fetch("SELECT COUNT(*) FROM adres", fetch_one=True)
    if adres_count and adres_count[0] == 0:
        database_execute(sqlite_insert_adres_data)


def fetch_accounts():
    """
    Haalt alle accounts op uit de database en retourneert ze als rijen
    waarvan de kolommen op naam kunnen worden uitgelezen.
    """
    return database_fetch("""
        SELECT
            email,
            password
        FROM
            accounts
    """)


def save_user(email, password):
    """
    Slaat een nieuwe gebruiker op in de database.
    Retourneert True als de registratie succesvol is, anders False.
    """
    if not email or not password:
        show_status("Registratie mislukt")
        return False

    success = database_execute("""
        INSERT INTO
            accounts (
                email,
                password
            )
        VALUES (?, ?)
    """, (email, password))

    if not success:
        show_status("Registratie mislukt. Fout bij opslaan van de gegevens.")

    return success


def fetch_patient_data():
    """
    Haalt de gegevens van alle patiënten op uit de database en retourneert ze als rijen
    waarvan de kolommen op naam kunnen worden uitgelezen.
    """
    return database_fetch("""
        SELECT
            persoon.voornaam,
            persoon.idpersoon,
            persoon.tussenvoegsel,
            persoon.achternaam,
            persoon.mobiel,
            adres.straat,
            adres.huisnr,
            adres.postcode,
            adres.woonplaats
        FROM
            persoon
        JOIN
            adres ON persoon.idpersoon = adres.idpersoon
        ORDER BY
            persoon.achternaam ASC
    """)


def clear_window():
    """
    Verwijdert alle widgets uit het hoofdvenster.
    """
    for widget in root.winfo_children():
        widget.destroy()


def show_status(message, success=False):
    """
    Toont een statusbericht aan de gebruiker.
    Als 'success' True is, wordt het bericht in groen weergegeven, anders in rood.
    """
    if success:
        status_label.config(text=message, bg="#d4edda", fg="#155724")
    else:
        status_label.config(text=message, bg="#f8d7da", fg="#721c24")

    status_label.grid()


def show_login_screen(status_message="", focus_password=False):
    """
    Loginscherm van de applicatie. Hier kan de gebruiker zijn e-mailadres en
    wachtwoord invullen om in te loggen. Als de gebruiker nog geen account heeft,
    kan hij/zij doorklikken naar het registratiescherm.
    """
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


def show_register_screen():
    """
    Registratiescherm van de applicatie. Hier kan de gebruiker een nieuw account
    aanmaken door een e-mailadres en wachtwoord in te vullen. Als de gebruiker
    al een account heeft, kan hij/zij terugkeren naar het loginscherm.
    """
    clear_window()

    global status_label

    root.title("Registreren patiëntenbeheer - Streekziekenhuis de Blauwe Berg")
    root.geometry("400x300")

    registerform = Frame(root, bg="#4E96D2")
    registerform.pack(padx=10, pady=10, fill="both", expand=True)

    registerform.columnconfigure(0, weight=0)
    registerform.columnconfigure(1, weight=1)

    Label(registerform, text="Maak hier een nieuw account aan.", bg="#4E96D2", fg="white", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=(0, 15), sticky="w")

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


def show_dashboard_screen():
    """
    Dit is het derde scherm van de applicatie, waar de gebruiker kan inloggen en de
    gegevens van patiënten kan beheren. Het scherm bevat een Combobox om een patiënt
    te selecteren en een knop om de gegevens van de geselecteerde patiënt weer te geven.
    """
    clear_window()

    global status_label

    root.title("Dashboard patiëntenbeheer - Streekziekenhuis de Blauwe Berg")
    root.geometry("800x600")

    dashboard = Frame(root, bg="#4E96D2")
    dashboard.pack(padx=10, pady=10, fill="both", expand=True)

    dashboard.columnconfigure(0, weight=1)
    dashboard.columnconfigure(1, weight=0)
    dashboard.columnconfigure(2, weight=1)

    patients_by_name = {}

    def retrieve_patient_data():
        """
        Haalt de gegevens van alle patiënten op uit de database en vult de Combobox met de namen van de patiënten.
        """
        patients = fetch_patient_data()

        patient_names = []
        patients_by_name.clear()

        for patient in patients:
            if patient["tussenvoegsel"]:
                name = f"{patient['achternaam']}, {patient['tussenvoegsel']}"
            else:
                name = patient["achternaam"]

            patient_names.append(name)
            patients_by_name[name] = patient

        patient_combobox["values"] = patient_names


    def show_patient():
        """
        Toont de gegevens van de geselecteerde patiënt in de invoervelden.
        """
        selected_name = patient_combobox.get()

        if selected_name not in patients_by_name:
            show_status("Geen patiënt geselecteerd.")
            return

        status_label.grid_remove()

        patient = patients_by_name[selected_name]

        label_fullname.configure(text=f"{patient['achternaam']}, {patient['voornaam']} {patient['tussenvoegsel'] or ''}".strip())

        patient_voornaam.set(patient["voornaam"])
        patient_tussenvoegsel.set(patient["tussenvoegsel"] or "")
        patient_achternaam.set(patient["achternaam"])
        patient_straat.set(patient["straat"])
        patient_huisnr.set(patient["huisnr"])
        patient_postcode.set(patient["postcode"])
        patient_woonplaats.set(patient["woonplaats"])
        patient_mobiel.set(patient["mobiel"])

    Label(dashboard, text="Dashboard patiëntenbeheer", bg="#4E96D2", fg="white", font=("Arial", 14)).grid(row=0, column=0, sticky="w")
    Button(dashboard, text="Uitloggen", fg="white", bg="#1E5593", relief=FLAT, command=logout, padx=10, pady=5).grid(row=0, column=2, padx=10, pady=10, sticky="e")

    patientform = Frame(dashboard, bg="#4E96D2")
    patientform.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    patientform.columnconfigure(0, weight=0)
    patientform.columnconfigure(1, weight=1)

    status_label = Label(patientform, text="", bg="#f8d7da", bd=1, fg="#721c24", font=("Arial", 10), padx=8, pady=4, anchor="w")
    status_label.grid(row=0, column=0, columnspan=2, padx=5, pady=(0, 10), sticky="ew")
    status_label.grid_remove()

    label_patient = Label(patientform, text="Patiënt:", fg="white", bg="#4E96D2", anchor="e")
    label_patient.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    patient_select_frame = Frame(patientform, bg="#4E96D2")
    patient_select_frame.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    patient_combobox = ttk.Combobox(patient_select_frame, postcommand=retrieve_patient_data, style="Padded.TCombobox", width=30)
    patient_combobox.grid(row=0, column=0, sticky="w")

    Button(patient_select_frame, text="Toon patiënt", command=show_patient).grid(row=0, column=1, padx=(5, 0), sticky="w")

    label_fullname = Label(patientform, text="", bg="#4E96D2", fg="white", font=("Arial", 14))
    label_fullname.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="w")

    label_voornaam = Label(patientform, text="Voornaam:", fg="white", bg="#4E96D2", anchor="e")
    label_voornaam.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    entry_voornaam = ttk.Entry(patientform, textvariable=patient_voornaam, style="Padded.TEntry")
    entry_voornaam.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

    label_tussenvoegsel = Label(patientform, text="Tussenvoegsel:", fg="white", bg="#4E96D2", anchor="e")
    label_tussenvoegsel.grid(row=4, column=0, padx=5, pady=5, sticky="e")

    entry_tussenvoegsel = ttk.Entry(patientform, textvariable=patient_tussenvoegsel, style="Padded.TEntry")
    entry_tussenvoegsel.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

    label_achternaam = Label(patientform, text="Achternaam:", fg="white", bg="#4E96D2", anchor="e")
    label_achternaam.grid(row=5, column=0, padx=5, pady=5, sticky="e")

    entry_achternaam = ttk.Entry(patientform, textvariable=patient_achternaam, style="Padded.TEntry")
    entry_achternaam.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

    label_straat = Label(patientform, text="Straat:", fg="white", bg="#4E96D2", anchor="e")
    label_straat.grid(row=6, column=0, padx=5, pady=5, sticky="e")

    entry_straat = ttk.Entry(patientform, textvariable=patient_straat, style="Padded.TEntry")
    entry_straat.grid(row=6, column=1, padx=5, pady=5, sticky="ew")

    label_huisnr = Label(patientform, text="Huisnummer:", fg="white", bg="#4E96D2", anchor="e")
    label_huisnr.grid(row=7, column=0, padx=5, pady=5, sticky="e")

    entry_huisnr = ttk.Entry(patientform, textvariable=patient_huisnr, style="Padded.TEntry")
    entry_huisnr.grid(row=7, column=1, padx=5, pady=5, sticky="ew")

    label_postcode = Label(patientform, text="Postcode:", fg="white", bg="#4E96D2", anchor="e")
    label_postcode.grid(row=8, column=0, padx=5, pady=5, sticky="e")

    entry_postcode = ttk.Entry(patientform, textvariable=patient_postcode, style="Padded.TEntry")
    entry_postcode.grid(row=8, column=1, padx=5, pady=5, sticky="ew")

    label_woonplaats = Label(patientform, text="Woonplaats:", fg="white", bg="#4E96D2", anchor="e")
    label_woonplaats.grid(row=9, column=0, padx=5, pady=5, sticky="e")

    entry_woonplaats = ttk.Entry(patientform, textvariable=patient_woonplaats, style="Padded.TEntry")
    entry_woonplaats.grid(row=9, column=1, padx=5, pady=5, sticky="ew")

    label_mobiel = Label(patientform, text="Mobiel:", fg="white", bg="#4E96D2", anchor="e")
    label_mobiel.grid(row=10, column=0, padx=5, pady=5, sticky="e")

    entry_mobiel = ttk.Entry(patientform, textvariable=patient_mobiel, style="Padded.TEntry")
    entry_mobiel.grid(row=10, column=1, padx=5, pady=5, sticky="ew")


def reset_patient_data():
    """
    Leegt alle patiëntgegevens.
    """
    patient_voornaam.set("")
    patient_tussenvoegsel.set("")
    patient_achternaam.set("")
    patient_straat.set("")
    patient_huisnr.set("")
    patient_postcode.set("")
    patient_woonplaats.set("")
    patient_mobiel.set("")


def login():
    """
    Verwerkt de inlogpoging van de gebruiker. Controleert of de ingevoerde
    gegevens geldig zijn en vergelijkt deze met de gegevens in de database.
    Als de inloggegevens correct zijn, wordt het dashboardscherm weergegeven.
    """
    login_email_value = login_email.get().strip()
    login_password_value = login_password.get()

    if login_email_value == "" or login_password_value == "":
        show_status("Vul uw e-mailadres en wachtwoord in.")
        return

    accounts = fetch_accounts()

    if len(accounts) == 0:
        show_status("Er zijn nog geen gebruikers geregistreerd.")
        return

    for account in accounts:
        if (
            account["email"] == login_email_value
            and account["password"] == login_password_value
        ):
            show_dashboard_screen()
            return

    show_status("Ongeldige inloggegevens.")
    login_password.set("")


def logout():
    """
    Logt de gebruiker uit, reset de patiëntgegevens en toont het inlogscherm.
    """
    show_login_screen("U bent succesvol uitgelogd.")
    reset_patient_data()


def register():
    """
    Verwerkt de registratie van een nieuwe gebruiker. Controleert of de
    ingevoerde gegevens geldig zijn en slaat de gebruiker op in de database.
    """
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

    accounts = fetch_accounts()

    for account in accounts:
        if account["email"] == register_email_value:
            show_status("Dit e-mailadres is al geregistreerd.")
            return

    if not save_user(register_email_value, register_password_value):
        return

    login_email.set(register_email_value)
    login_password.set("")

    register_email.set("")
    register_email_repeat.set("")
    register_password.set("")
    register_password_repeat.set("")

    show_login_screen("Registratie succesvol! U kunt nu inloggen.",  focus_password=True)


root = Tk()

style = ttk.Style()
style.configure("Padded.TEntry", padding=4)
style.configure("Padded.TCombobox", padding=4)

root.configure(bg="#4E96D2")

login_email = StringVar()
login_password = StringVar()

register_email = StringVar()
register_email_repeat = StringVar()
register_password = StringVar()
register_password_repeat = StringVar()

patient_voornaam = StringVar()
patient_tussenvoegsel = StringVar()
patient_achternaam = StringVar()
patient_straat = StringVar()
patient_huisnr = StringVar()
patient_postcode = StringVar()
patient_woonplaats = StringVar()
patient_mobiel = StringVar()

show_login_screen()

"""DEFAULT LOGIN CREDENTIALS FOR TESTING PURPOSES"""
login_email.set("john@doe.com")
login_password.set("test")

create_database_tables()

root.mainloop()