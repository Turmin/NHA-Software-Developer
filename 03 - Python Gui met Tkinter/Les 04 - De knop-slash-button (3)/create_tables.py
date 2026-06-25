import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')

    sqlite_create_persoon_query = '''
        CREATE TABLE IF NOT EXISTS `persoon` (
            `idpersoon` INTEGER PRIMARY KEY AUTOINCREMENT,
            `voornaam` VARCHAR(45) NOT NULL,
            `tussenvoegsel` VARCHAR(45) NULL,
            `achternaam` VARCHAR(255) NOT NULL,
            `mobiel` VARCHAR(23) NOT NULL);
    '''

    sqlite_create_adres_query = '''
        CREATE TABLE IF NOT EXISTS `adres` (
            `idadres` INTEGER PRIMARY KEY AUTOINCREMENT,
            `straat` VARCHAR(45) NOT NULL,
            `huisnr` VARCHAR(45) NOT NULL,
            `postcode` VARCHAR(45) NOT NULL,
            `woonplaats` VARCHAR(45) NOT NULL,
            `idpersoon` INTEGER NOT NULL);
    '''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_persoon_query)
    cursor.execute(sqlite_create_adres_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")