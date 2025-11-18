import random
import tkinter as tk
import sys
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
from customtkinter import CTkImage
import krd13


betuk = ['A)', 'B)', 'C)', 'D)']

#Eső három kérdés
with open("kerdesek_valaszok_01.txt", "r", encoding="utf-8") as file_1:
    
    kerdes_01 = []
    valaszok_01 = []
    megoldas_1 = []

    for sor_1 in file_1:
        sor_1 = sor_1.strip().split(";")
        if len(sor_1) == 3:
            kerdes_01.append(sor_1[0])
            valaszok_01.append(sor_1[1].split())
            megoldas_1.append(sor_1[2])

# Tesztelés:            
#print(f"{kerdes_01[0]}")
#for i in range(4):
#    print(f"{betuk[i]}{valaszok_01[0][i]}")
#print(f"{megoldas_1[0]}")

# Főablak
foablak = ctk.CTk()
foablak.title("Legyen Ön is mérnökinfós!")
foablak.geometry("800x600")

pil_image = Image.open("Images/nje_logo.png")
bg_image = CTkImage(light_image=pil_image, size=(800, 600))

lbl = ctk.CTkLabel(foablak, text="Legyen Ön is mérnökinfós kvízjáték!\n\nFeladat 7 helyes válasz megadása.\nAz első 3 kérdés Neumann Jánosról fog szólni.\nAz utána következő négy pedig a Hálózatbiztonsági és üzemeltetési-és\n Ipari informatika specializációról.\n\
                   \nKezdődhet a játék?😜", font=("Apostol", 18, "bold"), image=bg_image, text_color="#A32F2F")
lbl.pack(padx=20, pady=20)
lbl.place(relx=0, rely=0, relwidth=1, relheight=1)
lbl.lower()

eredmeny = ctk.CTkLabel(foablak, text="", font=("Apostol", 12))
eredmeny.pack(pady=10)

start_btn = ctk.CTkButton(foablak, text="Kezdjünk hozzá!", command=lambda: krd13.kerdesek13_ablak(foablak, kerdes_01, valaszok_01, megoldas_1, betuk))
start_btn.pack(pady=50)
start_btn.place(relx=0.5, rely=0.7, anchor="center")

foablak.mainloop()

