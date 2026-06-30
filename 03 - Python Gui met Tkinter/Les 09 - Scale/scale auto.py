from tkinter import Tk, DoubleVar, Scale, Label, CENTER

def slider_changed(event):
    lbl_scale.configure(text=f"{var.get():.2f}")

root = Tk()
var = DoubleVar()
scale = Scale(root, variable = var, orient="horizontal", from_=0, to=100, resolution=1, tickinterval=10, troughcolor="blue", sliderlength=20, length=280, command=slider_changed)
scale.pack(anchor=CENTER)

lbl_scale = Label(root)
lbl_scale.pack()

root.title("Scale")
root.geometry("300x200")

root.mainloop()