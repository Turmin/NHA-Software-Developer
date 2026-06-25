"""
Python Gui met Tkinter - Les 1 - De knop/button (1)

Maak een simpele applicatie waarin alle genoemde opties gebruikt zijn. U kunt het voorbeeld gebruiken uit “Ik leer Python GUI maken bij NHA”, paragraaf 1.4.
"""

import tkinter as tk

def show_status():
    print(checkbox_var.get())

def show_choice():
    print(choice_var.get())

root = tk.Tk()
root.title("Ik leer Python GUI maken bij NHA")
root.geometry("1024x768")
root.configure(bg="#1E5593")

frame_links = tk.Frame(root, bg="#4E96D2", width=200, height=200, relief=tk.RAISED, bd=5)
frame_links.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=40, pady=40)

tk.Label(frame_links, text="Buttons", bg="#4E96D2", fg="white", font=("Arial", 16)).pack(anchor=tk.N, pady=20)

for relief_type in [tk.FLAT, tk.GROOVE, tk.RAISED, tk.RIDGE, tk.SOLID, tk.SUNKEN]:
    tk.Button(frame_links, text="Click", cursor="question_arrow", bg="#4E96D2", fg="white", font=("Arial", 12), relief=relief_type).pack(pady=20)

frame_rechts = tk.Frame(root, bg="#1D92AA", width=200, height=200, relief=tk.RIDGE, bd=5)
frame_rechts.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=40, pady=40)

tk.Label(frame_rechts, text="Hello World", bg="#1D92AA", fg="white", font=("Arial", 16)).pack(anchor=tk.S, pady=20)

tk.Entry(frame_rechts, font=("Arial", 12)).pack(pady=20)

checkbox_var = tk.BooleanVar(value=True)

tk.Checkbutton(frame_rechts, text="Check me", bg="#1D92AA", fg="white", activebackground="#1D92AA", activeforeground="white", selectcolor="green",font=("Arial", 12), variable=checkbox_var, command=show_status).pack(pady=20)

choice_var = tk.StringVar(value="python")
choices = ["Python", "Tkinter"]

for choice in choices:
    tk.Radiobutton(frame_rechts, text=choice, bg="#1D92AA", activebackground="#1D92AA", variable=choice_var, value=choice.lower(), command=show_choice).pack()

root.mainloop()