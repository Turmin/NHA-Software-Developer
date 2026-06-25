"""
Python Gui met Tkinter - Les 2 - De knop/button (2)

Pas de rekenmachine zo aan dat de cijfers niet ingetypt worden, maar net zoals bij een echte rekenmachine met behulp van knopjes worden ingevoerd.
"""

from tkinter import Tk, Frame, BOTH, Label, Button, messagebox

eerste_getal = None
operator = None
nieuwe_invoer = True

def lees_getal():
    tekst = getal.cget("text").replace(",", ".")

    if tekst == "":
        return 0

    return float(tekst)

def druk_cijfer(cijfer):
    global nieuwe_invoer

    huidige_tekst = getal.cget("text")

    if nieuwe_invoer or huidige_tekst == "0":
        getal.config(text=cijfer)
        nieuwe_invoer = False
    else:
        getal.config(text=huidige_tekst + cijfer)

def druk_operator(nieuwe_operator):
    global eerste_getal, operator, nieuwe_invoer

    if nieuwe_invoer and eerste_getal is not None:
        operator = nieuwe_operator
        som.config(text=f"{eerste_getal:g} {operator}")
        return

    try:
        huidig_getal = lees_getal()
    except ValueError:
        messagebox.showerror("Fout", "Ongeldig getal.")
        wissen()
        return

    if eerste_getal is None:
        eerste_getal = huidig_getal
    else:
        try:
            eerste_getal = bereken(eerste_getal, huidig_getal, operator)
        except ZeroDivisionError:
            messagebox.showerror("Fout", "Delen door nul kan niet.")
            wissen()
            return

        getal.config(text=f"{eerste_getal:g}".replace(".", ","))

    operator = nieuwe_operator
    som.config(text=f"{eerste_getal:g} {operator}")
    nieuwe_invoer = True

def bereken(getal_1, getal_2, operator):
    if operator == "+":
        return getal_1 + getal_2
    elif operator == "-":
        return getal_1 - getal_2
    elif operator == "*":
        return getal_1 * getal_2
    elif operator == "/":
        if getal_2 == 0:
            raise ZeroDivisionError
        return getal_1 / getal_2

def druk_is():
    global eerste_getal, operator, nieuwe_invoer

    if eerste_getal is None or operator is None:
        return

    if nieuwe_invoer:
        return

    try:
        tweede_getal = lees_getal()
        uitkomst = bereken(eerste_getal, tweede_getal, operator)

        som.config(text=f"{eerste_getal:g} {operator} {tweede_getal:g} =")
        getal.config(text=f"{uitkomst:g}".replace(".", ","))

        eerste_getal = None
        operator = None
        nieuwe_invoer = True

    except ZeroDivisionError:
        messagebox.showerror("Fout", "Delen door nul kan niet.")
        wissen()

    except ValueError:
        messagebox.showerror("Fout", "Ongeldig getal.")
        wissen()

def druk_komma():
    global nieuwe_invoer

    huidige_tekst = getal.cget("text")

    if nieuwe_invoer:
        getal.config(text="0,")
        nieuwe_invoer = False
    elif "," not in huidige_tekst:
        getal.config(text=huidige_tekst + ",")

def wissen():
    global eerste_getal, operator, nieuwe_invoer

    eerste_getal = None
    operator = None
    nieuwe_invoer = True

    som.config(text="")
    getal.config(text="0")

def posneg():
    waarde = float(getal.cget("text").replace(",", "."))
    waarde = -waarde
    getal.config(text=f"{waarde:g}".replace(".", ","))

def toets_indruk(event):
    toets = event.char
    toets_naam = event.keysym

    if toets_naam in ("Shift_L", "Shift_R", "Control_L", "Control_R", "Alt_L", "Alt_R"):
        return

    if toets_naam in ("Return", "KP_Enter", "equal"):
        druk_is()
        return

    if toets == "=":
        druk_is()
        return

    if toets_naam == "Escape":
        wissen()
        return

    if toets_naam == "BackSpace":
        backspace()
        return

    if toets in "0123456789":
        druk_cijfer(toets)
        return

    if toets in ",.":
        druk_komma()
        return

    if toets in "+-/":
        druk_operator(toets)
        return

    if toets in "*xX":
        druk_operator("*")
        return

def backspace():
    huidige_tekst = getal.cget("text")

    if nieuwe_invoer:
        return

    if len(huidige_tekst) > 1:
        getal.config(text=huidige_tekst[:-1])
    else:
        getal.config(text="0")

root = Tk()
root.title("Rekenmachine")
root.geometry("500x350")
root.configure(bg="#1E5593")

content_frame = Frame(root, bg="#4E96D2")
content_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

som = Label(content_frame, text="", bg="#4E96D2", fg="white", font=("Arial", 11), anchor="e")
som.pack(fill="x", pady=(20,0), padx=20)
getal = Label(content_frame, text="0", bg="#4E96D2", fg="white", font=("Arial", 18), anchor="e")
getal.pack(fill="x", pady=(0,10), padx=20)

button_frame = Frame(content_frame, bg="#4E96D2")
button_frame.pack(pady=10)

Button(button_frame, text="C", width=10, font=("Arial", 12), command=wissen).grid(row=0, column=0, padx=5, pady=5)
Button(button_frame, text="±", width=10, font=("Arial", 12), command=posneg).grid(row=0, column=1, padx=5, pady=5)
Button(button_frame, text="÷", width=10, font=("Arial", 12), command=lambda: druk_operator("/")).grid(row=0, column=2, padx=5, pady=5)
Button(button_frame, text="×", width=10, font=("Arial", 12), command=lambda: druk_operator("*")).grid(row=0, column=3, padx=5, pady=5)

Button(button_frame, text="7", width=10, font=("Arial", 12), command=lambda: druk_cijfer("7")).grid(row=1, column=0, padx=5, pady=5)
Button(button_frame, text="8", width=10, font=("Arial", 12), command=lambda: druk_cijfer("8")).grid(row=1, column=1, padx=5, pady=5)
Button(button_frame, text="9", width=10, font=("Arial", 12), command=lambda: druk_cijfer("9")).grid(row=1, column=2, padx=5, pady=5)
Button(button_frame, text="-", width=10, font=("Arial", 12), command=lambda: druk_operator("-")).grid(row=1, column=3, padx=5, pady=5)

Button(button_frame, text="4", width=10, font=("Arial", 12), command=lambda: druk_cijfer("4")).grid(row=2, column=0, padx=5, pady=5)
Button(button_frame, text="5", width=10, font=("Arial", 12), command=lambda: druk_cijfer("5")).grid(row=2, column=1, padx=5, pady=5)
Button(button_frame, text="6", width=10, font=("Arial", 12), command=lambda: druk_cijfer("6")).grid(row=2, column=2, padx=5, pady=5)
Button(button_frame, text="+", width=10, font=("Arial", 12), command=lambda: druk_operator("+")).grid(row=2, column=3, padx=5, pady=5)

Button(button_frame, text="1", width=10, font=("Arial", 12), command=lambda: druk_cijfer("1")).grid(row=3, column=0, padx=5, pady=5)
Button(button_frame, text="2", width=10, font=("Arial", 12), command=lambda: druk_cijfer("2")).grid(row=3, column=1, padx=5, pady=5)
Button(button_frame, text="3", width=10, font=("Arial", 12), command=lambda: druk_cijfer("3")).grid(row=3, column=2, padx=5, pady=5)
Button(button_frame, text="=", width=10, font=("Arial", 12), command=druk_is).grid(row=3, column=3, rowspan=2, padx=5, pady=5, sticky="ns")

Button(button_frame, text="0", width=10, font=("Arial", 12), command=lambda: druk_cijfer("0")).grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")
Button(button_frame, text=",", width=10, font=("Arial", 12), command=druk_komma).grid(row=4, column=2, padx=5, pady=5)

root.bind("<Key>", toets_indruk)

root.mainloop()