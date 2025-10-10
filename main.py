import random
import tkinter as tk
import customtkinter as ctk #Designhoz
from tkinter import messagebox
from customtkinter import * #Designhoz
from PIL import Image #Designhoz

#Design elemek
set_appearance_mode("dark")

betuk = ['A)', 'B)', 'C)', 'D)']

#Eső négy kérdés
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

#Második két kérdés



# Harmadik két kérdés
with open("kerdesek_valaszok_03.txt", "r", encoding="utf-8") as file_3:
    
    kerdes_03 = []
    valaszok_03 = []
    megoldas_3 = []

    for sor_3 in file_3:
        sor_3 = sor_3.strip().split(";")
        if len(sor_3) == 3:
            kerdes_03.append(sor_3[0])
            valaszok_03.append(sor_3[1].split())
            megoldas_3.append(sor_3[2])

# Tesztelés:            
#print(f"{kerdes_03[0]}")
#for i in range(4):
#    print(f"{betuk[i]}{valaszok_03[0][i]}")
#print(f"{megoldas_3[0]}")


def kerdesek_ablak():
    foablak.withdraw()

    uj_ablak = CTkToplevel()
    uj_ablak.title("Játék!")
    uj_ablak.geometry("600x500")

    kerdes_1_4 = random.randint(0, len(kerdes_01) - 1 ) 

    krd_lbl = tk.Label(uj_ablak, text=kerdes_01[kerdes_1_4], font=("Arial", 12))
    krd_lbl.pack(padx=20, pady=20)

    for i in range(4):
        vlsz_btn = tk.Button(uj_ablak, text=betuk[i] + valaszok_01[kerdes_1_4][i])
        vlsz_btn.pack()

# Főablak
foablak = ctk.CTk()
foablak.title("Legyen Ön is mérnökinfós! :)")
foablak.geometry("800x600")

lbl = CTkLabel(foablak, text="Legyen Ön is mérnökinfós kvízjáték.\nFeladat 7 helyes válasz megadás.\nKezdődhet a játék?")
lbl.pack(padx=20, pady=20)

# Gomb
gomb_1 = CTkButton(foablak, text="Kezdjünk hozzá!", command=kerdesek_ablak)
gomb_1.pack(pady=50)

# Futtatás
foablak.mainloop()

