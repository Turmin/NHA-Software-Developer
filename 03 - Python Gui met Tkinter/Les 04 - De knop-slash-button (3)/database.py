import sqlite3
from pathlib import Path

try:
    sqliteConnection = sqlite3.connect(Path(__file__).parent / 'SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Database created and succesfully connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite database version is : ", record)
    cursor.close()
except sqlite3.Error as error:
    print("Error while connection to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")