"""
Python Gui met Tkinter - Les 8 - Menu
"""

from tkinter import Tk, Text, BOTH, END, Menu, filedialog, messagebox

current_file_path = None

def update_title():
    if current_file_path:
        file_name = current_file_path.split("/")[-1]
        root.title(f"{file_name} - Tekst Editor")
    else:
        root.title("Nieuw bestand - Tekst Editor")

def new_file():
    global current_file_path

    text_editor.delete("1.0", END)
    current_file_path = None
    update_title()

def open_file():
    global current_file_path

    file_path = filedialog.askopenfilename(
        title="Open bestand",
        filetypes=[
            ("Tekstbestanden", "*.txt"),
            ("Alle bestanden", "*.*")
        ]
    )

    if not file_path:
        return

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    text_editor.delete("1.0", END)
    text_editor.insert("1.0", content)
    text_editor.edit_reset()

    current_file_path = file_path
    update_title()

def save_file():
    if current_file_path:
        content = text_editor.get("1.0", END)

        with open(current_file_path, "w", encoding="utf-8") as file:
            file.write(content)
    else:
        save_as_file()

def save_as_file():
    global current_file_path

    file_path = filedialog.asksaveasfilename(
        title="Opslaan als",
        defaultextension=".txt",
        filetypes=[
            ("Tekstbestanden", "*.txt"),
            ("Alle bestanden", "*.*")
        ]
    )

    if not file_path:
        return

    content = text_editor.get("1.0", END)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    current_file_path = file_path
    update_title()

def undo_text():
    try:
        text_editor.edit_undo()
    except:
        pass

def redo_text():
    try:
        text_editor.edit_redo()
    except:
        pass

def help_about():
    messagebox.showinfo(
        "Over Tekst Editor",
        "Tekst Editor\n\n"
        "Python GUI met Tkinter - Les 8\n\n"
        "Functies:\n"
        "- Nieuw bestand maken\n"
        "- Bestand openen\n"
        "- Bestand opslaan\n"
        "- Opslaan als\n"
        "- Undo en Redo"
    )


root = Tk()
root.geometry("1024x768")
root.configure(bg="#4E96D2")

text_editor = Text(root, undo=True)
text_editor.pack(fill=BOTH, expand=True)

menubar = Menu(root)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save as", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label="Undo", command=undo_text)
edit_menu.add_command(label="Redo", command=redo_text)

help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=help_about)

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)

update_title()

root.mainloop()