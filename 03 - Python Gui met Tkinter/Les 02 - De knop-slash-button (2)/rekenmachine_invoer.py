"""
Python Gui met Tkinter - Les 2 - De knop/button (2)
"""

from tkinter import Tk, Frame, BOTH, Label, Button, Entry, StringVar, messagebox

def show_message(operator):
    try:
        nummer_1 = float(getal_1_var.get())
        nummer_2 = float(getal_2_var.get())

        if operator == "+":
            uitkomst = nummer_1 + nummer_2
        elif operator == "-":
            uitkomst = nummer_1 - nummer_2
        elif operator == "*":
            uitkomst = nummer_1 * nummer_2
        elif operator == "/":
            uitkomst = nummer_1 / nummer_2

        uitkomst_label.config(text=f"Uitkomst: {uitkomst}")
        messagebox.showinfo("Info", f"De uitkomst is: {uitkomst}")

    except ValueError:
        messagebox.showerror("Fout", "Voer twee geldige getallen in.")
    except ZeroDivisionError:
        messagebox.showerror("Fout", "Delen door nul kan niet.")

root = Tk()
root.title("Rekenmachine")
root.geometry("400x600")
root.configure(bg="#1E5593")

getal_1_var = StringVar()
getal_2_var = StringVar()

frame = Frame(root, bg="#4E96D2")
frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

Label(frame, text="Rekenmachine", bg="#4E96D2", fg="white", font=("Arial", 14)).pack(pady=20)

Label(frame, text="Voer het eerste getal in:", bg="#4E96D2", fg="white", font=("Arial", 14)).pack(pady=(10,2))
getal_1_entry = Entry(frame, textvariable=getal_1_var, font=("Arial", 12))
getal_1_entry.pack(pady=(0,10))

Label(frame, text="Voer het tweede getal in:", bg="#4E96D2", fg="white", font=("Arial", 14)).pack(pady=(10,2))
getal_2_entry = Entry(frame, textvariable=getal_2_var, font=("Arial", 12))
getal_2_entry.pack(pady=(0,10))

uitkomst_label = Label(frame, text="", bg="#4E96D2", fg="white", font=("Arial", 14))
uitkomst_label.pack(pady=4)

button_frame = Frame(frame, bg="#4E96D2")
button_frame.pack(pady=10)

Button(button_frame, text="+", width=10, font=("Arial", 12), command=lambda: show_message("+")).grid(row=0, column=0, padx=5, pady=5)
Button(button_frame, text="-", width=10, font=("Arial", 12), command=lambda: show_message("-")).grid(row=0, column=1, padx=5, pady=5)
Button(button_frame, text="×", width=10, font=("Arial", 12), command=lambda: show_message("*")).grid(row=1, column=0, padx=5, pady=5)
Button(button_frame, text="÷", width=10, font=("Arial", 12), command=lambda: show_message("/")).grid(row=1, column=1, padx=5, pady=5)

root.mainloop()