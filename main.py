import random
import tkinter as tk
import sys
import customtkinter as ctk #Designhoz
from tkinter import messagebox
#from customtkinter import * #Designhoz
from PIL import Image #Designhoz

#Design elemek
#set_appearance_mode("dark")

betuk = ['A)', 'B)', 'C)', 'D)']
kerdesek_14 = 0
kerdes_1_4 = 0

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

# Főablak
foablak = ctk.CTk()
foablak.title("Legyen Ön is mérnökinfós! :)")
foablak.geometry("800x600")

lbl = ctk.CTkLabel(foablak, text="Legyen Ön is mérnökinfós kvízjáték.\nFeladat 7 helyes válasz megadás.\nKezdődhet a játék?")
lbl.pack(padx=20, pady=20)

eredmeny = ctk.CTkLabel(foablak, text="", font=("Arial", 12))
eredmeny.pack(pady=10)

def kerdesek_ablak():
    global kerdes_1_4, kerdesek_14
    foablak.withdraw()

    uj_ablak = ctk.CTkToplevel()
    uj_ablak.title("Játék!")
    uj_ablak.geometry("600x500")

    helyes_e_lbl = ctk.CTkLabel(uj_ablak, text="", font=("Arial", 12))
    helyes_e_lbl.pack(pady=10)

    kov_btn = ctk.CTkButton(uj_ablak, text="Következő kérdés", command=lambda: kov_kerdes(uj_ablak), state="disabled")
    kov_btn.pack(pady=10)

    def kerdes_14_mt():
        global kerdes_1_4, vlsz_btn, gombok

        kerdes_1_4 = random.randint(0, len(kerdes_01) - 1 )
        krd = kerdes_01[kerdes_1_4]
        krd_lbl = ctk.CTkLabel(uj_ablak, text=krd, font=("Arial", 12))
        krd_lbl.pack(padx=20, pady=20)

        gombok = []
        for i in range(4):
            btn_sz = valaszok_01[kerdes_1_4][i]
            vlsz_btn = ctk.CTkButton(uj_ablak, text=betuk[i] + btn_sz, 
                                 command=lambda txt=btn_sz: (krd_ell(txt, kov_btn), gomb_sz(vlsz_btn.cget("text"))))
            gombok.append(vlsz_btn)
            vlsz_btn.pack(pady=5)

        def gomb_sz(text):
            {"text"}

        kov_btn.configure(state="disabled")
        helyes_e_lbl.configure(text="")

    def krd_ell(vlsz_btn_sz, kovetkezo_gomb):
        helyes_idx = megoldas_1[kerdes_1_4]

        if vlsz_btn_sz == helyes_idx:
            helyes_e_lbl.configure(text="Helyes!")
            kovetkezo_gomb.configure(state="normal")
        else:
            helyes_e_lbl.configure(text="Helytelen!")
            show_msgbox()

    def kov_kerdes():
        global kerdesek_14
        kerdesek_14 += 1
        if kerdesek_14 < 4:
            kerdes_14_mt()
        else:
            pass

    def show_msgbox():
        box = ctk.CTkToplevel(uj_ablak)
        box.title("Vége a játéknak.")
        box.geometry("300x150")
        box.grab_set()

        ctk.CTkLabel(box, text="A válasz helytelen, a játéknak vége.", font=("Arial", 12)).pack(pady=20)
        ctk.CTkButton(box, text="Új játék", command=lambda: (box.destroy())).pack(side=ctk.LEFT, padx=20)
        ctk.CTkButton(box, text="Kilépés", command=lambda: (box.destroy(), uj_ablak.destroy(), sys.exit())).pack(side=ctk.RIGHT, padx=20)

    kerdes_14_mt()


start_btn = ctk.CTkButton(foablak, text="Kezdjünk hozzá!", command=kerdesek_ablak)
start_btn.pack(pady=50)

foablak.mainloop()

