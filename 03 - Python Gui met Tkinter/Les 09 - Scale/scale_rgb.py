"""
Python Gui met Tkinter - Les 9 - Scale

Maak een applicatie die voor u de RGB-code voor een kleur samenstelt.
Daarvoor heeft u natuurlijk een scherm nodig. RGB heeft drie kleurcodes
nodig, dus uw applicatie heeft drie sliders. Verticaal of horizontaal,
dat maakt niet uit. Zorg ervoor dat, als u de waarden zet, een vak direct
verandert van kleur of dat u de knop gebruikt om de kleur te zetten.
"""

from tkinter import Tk, Frame, IntVar, Scale, Label, FLAT

def create_scale_widget(frame, variable, label, row):
    scale = Scale(
        frame,
        variable=variable,
        orient="horizontal",
        from_=0,
        to=255,
        resolution=1,
        tickinterval=50,
        label=label,
        length=340,
        command=update_color,

        bg=frame.cget("bg"),
        fg="white",
        troughcolor="#1E5593",
        activebackground=frame.cget("bg"),

        bd=0,
        highlightthickness=0,
        relief=FLAT
    )
    scale.grid(row=row, column=0, padx=10, pady=5)
    return scale


def update_color(event=None):
    red = red_var.get()
    green = green_var.get()
    blue = blue_var.get()

    color_code = f"#{red:02x}{green:02x}{blue:02x}"

    color_box.config(bg=color_code)
    lbl_scale.config(text=f"RGB: {red}, {green}, {blue}   HEX: {color_code}")


root = Tk()
root.title("RGB kleur kiezer - Les 9")
root.configure(bg="#4E96D2")
root.geometry("380x420")

red_var = IntVar()
green_var = IntVar()
blue_var = IntVar()

frame = Frame(root, bg=root.cget("bg"))
frame.grid(row=0, column=0, padx=10, pady=10)

red_scale = create_scale_widget(frame, red_var, "Rood", 0)
green_scale = create_scale_widget(frame, green_var, "Groen", 1)
blue_scale = create_scale_widget(frame, blue_var, "Blauw", 2)

color_box = Label(root, text="Voorbeeldkleur", width=50, height=3, bg="#000000", fg="white")
color_box.grid(row=1, column=0, padx=10, pady=10)

lbl_scale = Label(root, text="RGB: 0, 0, 0   HEX: #000000", bg=root.cget("bg"), fg="white")
lbl_scale.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()