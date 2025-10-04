import tkinter as tk
from tkinter import messagebox

def gombra_katt():
    messagebox.showinfo("Üzenet", "Megnyomtad a gombot!")

# Főablak
ablak = tk.Tk()
ablak.title("Egyszerű játék ablak")
ablak.geometry("300x200")

# Gomb
gomb = tk.Button(ablak, text="Kattints rám!", command=gombra_katt)
gomb.pack(pady=50)

# Futtatás
ablak.mainloop()
