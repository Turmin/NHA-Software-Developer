from tkinter import Tk, DoubleVar, Scale, Label, Button, CENTER

def sel():
    selectie = 'Waarde = ' + str(var.get())
    lbl_scale.config(text=selectie)

root = Tk()
var = DoubleVar()
scale = Scale(root, variable = var, orient="horizontal", from_=0, to=100, resolution=1, tickinterval=10, troughcolor="blue", sliderlength=20, length=280)
scale.pack(anchor=CENTER)

btn_haal_waarde = Button(root, text="Haal waarde van Scale", command=sel)
btn_haal_waarde.pack(anchor=CENTER)

lbl_scale = Label(root)
lbl_scale.pack()

root.title("Scale")
root.geometry("300x200")

root.mainloop()