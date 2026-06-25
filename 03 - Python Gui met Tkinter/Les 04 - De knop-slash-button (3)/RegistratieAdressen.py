"""
Python Gui met Tkinter - Les 4 - De knop/ Button (3)

1. Creëer een applicatie onder de naam “RegistratieAdressen”.
2. Maak een connectie met een SQLite-database.
3. Maak een adressentabel.
4. Maak een formulier dat in de database adressen kan toevoegen.
"""

from tkinter import Tk, Frame, Button, Label, ttk, StringVar, FLAT
import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent / "database.db"
table = None

def database_connection():
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        return connection

    except sqlite3.Error as error:
        print("Fout opgetreden bij verbinden met database:", error)
        return None

def database_close(connection):
    if connection:
        connection.close()

def create_database_tables(connection):
    sqlite_create_persoon_query = '''
        CREATE TABLE IF NOT EXISTS persoon (
            idpersoon INTEGER PRIMARY KEY AUTOINCREMENT,
            voornaam VARCHAR(45) NOT NULL,
            tussenvoegsel VARCHAR(45) NULL,
            achternaam VARCHAR(255) NOT NULL,
            mobiel VARCHAR(23) NOT NULL);
    '''

    sqlite_create_adres_query = '''
        CREATE TABLE IF NOT EXISTS adres (
            idadres INTEGER PRIMARY KEY AUTOINCREMENT,
            straat VARCHAR(45) NOT NULL,
            huisnr VARCHAR(45) NOT NULL,
            postcode VARCHAR(45) NOT NULL,
            woonplaats VARCHAR(45) NOT NULL,
            idpersoon INTEGER NULL);
    '''

    if connection:
        cursor = connection.cursor()
        cursor.execute(sqlite_create_persoon_query)
        cursor.execute(sqlite_create_adres_query)
        connection.commit()
        print("SQLite tabellen zijn aangemaakt indien deze nog niet bestonden.")
    
        cursor.close()

def insert_data():
    register_straat_value = register_straat.get().strip()
    register_huisnr_value = register_huisnr.get()
    register_postcode_value = register_postcode.get().strip()
    register_woonplaats_value = register_woonplaats.get()

    if (
        register_straat_value == ""
        or register_huisnr_value == ""
        or register_postcode_value == ""
        or register_woonplaats_value == ""
    ):
        show_status("Vul alle velden in.")
        return

    connection = database_connection()

    if not connection:
        return False

    try:
        cursor = connection.cursor()

        cursor.execute(
            """INSERT INTO adres (
                straat,
                huisnr,
                postcode,
                woonplaats
            ) VALUES (?, ?, ?, ?)""",
            (
                register_straat_value,
                register_huisnr_value,
                register_postcode_value,
                register_woonplaats_value
            )
        )

        connection.commit()
        refresh_table()
        show_status("Gegevens zijn succesvol opgeslagen!", success=True)
        return True

    except sqlite3.Error as error:
        show_status("Fout bij opslaan van de gegevens")
        print("Fout bij opslaan van de gegevens:", error)
        return False

    finally:
        cursor.close()
        database_close(connection)

def fetch_data():
    connection = database_connection()

    if not connection:
        return []

    try:
        cursor = connection.cursor()

        cursor.execute(
            """SELECT
                idadres,  
                straat,
                huisnr,
                postcode,
                woonplaats
            FROM
                adres
            ORDER BY idadres DESC
            """
        )
        resultaat = cursor.fetchall()

        return resultaat

    except sqlite3.Error as error:
        show_status("Fout bij ophalen van de gegevens")
        print("Fout bij ophalen van de gegevens:", error)
        return []

    finally:
        cursor.close()
        database_close(connection)

def create_data_table():
    global table

    kolommen = {
        "id": {"titel": "ID", "breedte": 50, "stretch": False},
        "straat": {"titel": "straat", "breedte": 100, "stretch": True},
        "huisnr": {"titel": "huisnr", "breedte": 100, "stretch": True},
        "postcode": {"titel": "postcode", "breedte": 100, "stretch": True},
        "woonplaats": {"titel": "woonplaats", "breedte": 100, "stretch": True},
    }

    table_frame = Frame(root)
    table_frame.pack(fill="both", expand=True, padx=20, pady=20)

    table = ttk.Treeview(
        table_frame,
        columns=list(kolommen.keys()),
        show="headings"
    )

    for kolom, opties in kolommen.items():
        table.heading(kolom, text=opties["titel"])
        table.column(
            kolom,
            width=opties["breedte"],
            stretch=opties["stretch"]
        )

    table.pack(fill="both", expand=True)

def refresh_table():
    global table

    persoon_data = fetch_data()

    if not persoon_data:
        return

    if table is None:
        create_data_table()

    for item in table.get_children():
        table.delete(item)

    for row in persoon_data:
        table.insert("", "end", values=row)

def show_status(message, success=False):
    if success:
        status_label.config(text=message, bg="#d4edda", fg="#155724")
    else:
        status_label.config(text=message, bg="#f8d7da", fg="#721c24")

    status_label.grid()

root = Tk()
root.title("Registratie formulier")
root.geometry("600x400")
root.configure(bg="#4E96D2")

style = ttk.Style()
style.configure("Padded.TEntry", padding=4)

register_straat = StringVar()
register_huisnr = StringVar()
register_postcode = StringVar()
register_woonplaats = StringVar()

registerform = Frame(root, bg="#4E96D2")
registerform.pack(padx=10, pady=10, fill="both", expand=True)

registerform.columnconfigure(0, weight=0)
registerform.columnconfigure(1, weight=1)

Label(registerform, text="Registratie formulier", bg="#4E96D2", fg="white", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=(0, 15), sticky="ew")

status_label = Label(registerform, text="", bg="#f8d7da", bd=1, fg="#721c24", font=("Arial", 10), padx=8, pady=4, anchor="w")
status_label.grid(row=0, column=0, columnspan=2, padx=5, pady=(0, 10), sticky="ew")
status_label.grid_remove()

label_straat = Label(registerform, text="Straat:", fg="white", bg="#4E96D2", anchor="e")
label_straat.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_straat = ttk.Entry(registerform, textvariable=register_straat, style="Padded.TEntry")
entry_straat.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

label_huisnr = Label(registerform, text="Huisnummer:", fg="white", bg="#4E96D2", anchor="e")
label_huisnr.grid(row=2, column=0, padx=5, pady=5, sticky="e")

entry_huisnr = ttk.Entry(registerform, textvariable=register_huisnr, style="Padded.TEntry")
entry_huisnr.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

label_postcode = Label(registerform, text="Postcode:", fg="white", bg="#4E96D2", anchor="e")
label_postcode.grid(row=3, column=0, padx=5, pady=5, sticky="e")

entry_postcode = ttk.Entry(registerform, textvariable=register_postcode, style="Padded.TEntry")
entry_postcode.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

label_woonplaats = Label(registerform, text="Woonplaats:", fg="white", bg="#4E96D2", anchor="e")
label_woonplaats.grid(row=4, column=0, padx=5, pady=5, sticky="e")

entry_woonplaats = ttk.Entry(registerform, textvariable=register_woonplaats, style="Padded.TEntry")
entry_woonplaats.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

buttons = Frame(registerform, bg="#4E96D2")
buttons.grid(row=6, column=1, padx=5, pady=10, sticky="w")

button_register = Button(buttons, text="Sla gegevens op in de database", fg="white", bg="#1E5593", relief=FLAT, command=insert_data, padx=10, pady=5)
button_register.grid(row=0, column=0, padx=(0, 5))

connection = database_connection()

if connection:
    create_database_tables(connection)
    database_close(connection)
    refresh_table()
else:
    show_status("Kan geen verbinding maken met de database.")

root.mainloop()