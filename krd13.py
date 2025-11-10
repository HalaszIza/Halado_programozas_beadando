import random
import tkinter as tk
import sys
import customtkinter as ctk #Designhoz
from tkinter import messagebox
#from customtkinter import * #Designhoz
from PIL import Image, ImageTk #Designhoz
from customtkinter import CTkImage
import krd45

#Második két kérdés
with open("kerdesek_valaszok_02.txt", "r", encoding="utf-8") as file_2:
    
    kerdes_02 = []
    valaszok_02 = []
    megoldas_2 = []

    for sor_2 in file_2:
        sor_2 = sor_2.strip().split(";")
        if len(sor_2) == 3:
            kerdes_02.append(sor_2[0])
            valaszok_02.append(sor_2[1].split())
            megoldas_2.append(sor_2[2])

# Tesztelés:            
#print(f"{kerdes_02[0]}")
#for i in range(4):
#    print(f"{betuk[i]}{valaszok_02[0][i]}")
#print(f"{megoldas_2[0]}")

def kerdesek13_ablak(foablak, kerdes_01, valaszok_01, megoldas_1, betuk):
    global kerdes_1_3
    global kerdesek_13
    
    kerdesek_13 = 0
    kerdes_1_3 = 0

    foablak.withdraw()

    uj_ablak = ctk.CTkToplevel()
    uj_ablak.title("Játék!")
    uj_ablak.geometry("800x600")

    pil_image = Image.open("Images/nje_logo.png")
    bg_image = CTkImage(light_image=pil_image, size=(800, 600))

    helyes_e_lbl = ctk.CTkLabel(uj_ablak, text="", font=("Arial", 12), image=bg_image)
    helyes_e_lbl.pack(pady=10)
    helyes_e_lbl.place(relx=0, rely=0, relwidth=1, relheight=1)
    helyes_e_lbl.lower()


    kov_btn = ctk.CTkButton(uj_ablak, text="Következő kérdés", command=lambda: kov_kerdes(), state="disabled")
    kov_btn.pack(pady=10)

    #1-3 kérdés
    def kerdes_13_mt():
        global kerdes_1_3
        global vlsz_btn
        global gombok
        global krd_lbl

        if 'krd_lbl' in globals():
            krd_lbl.destroy()
        if 'gombok' in globals():
            for btn in gombok:
                btn.destroy()

        kerdes_1_3 = random.randint(0, len(kerdes_01) - 1 )
        krd = kerdes_01[kerdes_1_3]
        krd_lbl = ctk.CTkLabel(uj_ablak, text=krd, font=("Arial", 12))
        krd_lbl.pack(padx=20, pady=20)

        gombok = []
        for i in range(4):
            btn_sz = valaszok_01[kerdes_1_3][i]
            vlsz_btn = ctk.CTkButton(uj_ablak, text= betuk[i] + btn_sz, 
                                    command=lambda txt=btn_sz: (krd_ell(txt, kov_btn), gomb_sz(vlsz_btn.cget("text"))))
            
            gombok.append(vlsz_btn)
            vlsz_btn.pack(pady=5)
        
        def gomb_sz(text):
            {"text"}

        kov_btn.configure(state="disabled")
        helyes_e_lbl.configure(text="")

    def krd_ell(vlsz_btn_sz, kovetkezo_gomb):
        global vlsz_btn
        global gombok
        global kerdesek_13
        helyes_idx = megoldas_1[kerdes_1_3]

        if vlsz_btn_sz == helyes_idx:
            helyes_e_lbl.configure(text="Helyes!")
            kovetkezo_gomb.configure(state="normal")
            kerdesek_13 += 1
        else:
            helyes_e_lbl.configure(text="Helytelen!")
            show_msgbox()

        for vlsz_btn in gombok:
            vlsz_btn.configure(state="disabled")
        kov_btn.configure(state="normal")

    def kov_kerdes():
        global kerdesek_13
        if kerdesek_13 < 3:
            kerdes_13_mt()
        else:
            kov_blokkbox()


    def kov_blokkbox():
        uj_ablak.withdraw()

        if kerdesek_13 == 0:
            box = ctk.CTkToplevel(foablak)
            box.title("Vége a játéknak.")
            box.geometry("300x150")
            box.grab_set()

            ctk.CTkLabel(box, text="Egyik kérdésre sem tudált helyesen válaszolni, a játéknak vége.", font=("Arial", 12)).pack(pady=20)
            ctk.CTkButton(box, text="Új játék", command=lambda: (box.destroy(), uj_ablak.destroy(), kerdesek13_ablak(foablak, kerdes_01, valaszok_01, megoldas_1, betuk))).pack(side=ctk.LEFT, padx=20)
            ctk.CTkButton(box, text="Kilépés", command=lambda: (box.destroy(), uj_ablak.destroy(), sys.exit())).pack(side=ctk.RIGHT, padx=20)

        else:
            box = ctk.CTkToplevel(foablak)
            box.geometry("500x300")
            box.grab_set()

            if kerdesek_13 == 3:
                box.title("3/3, nem semmi.")
                ctk.CTkLabel(box, text="Eddig 3/7, csak így tovább. A következő 2 kérdés a Hálózat biztonsági és üzemeltetési specializációval kapcsolatos. Sok sikert!", font=("Arial", 12)).pack(pady=20)
                ctk.CTkButton(box, text="Következő kérdések.", command=lambda: (box.destroy(), krd45.kerdesek45_ablak(foablak, kerdes_02, valaszok_02, megoldas_2, betuk))).pack(side=ctk.RIGHT,padx=20)

        
    def show_msgbox():
        box = ctk.CTkToplevel(uj_ablak)
        box.title("Vége a játéknak.")
        box.geometry("300x150")
        box.grab_set()

        ctk.CTkLabel(box, text="A válasz helytelen, a játéknak vége.", font=("Arial", 12)).pack(pady=20)
        ctk.CTkButton(box, text="Új játék", command=lambda: (box.destroy(), uj_ablak.destroy(), kerdesek13_ablak(foablak, kerdes_01, valaszok_01, megoldas_1, betuk))).pack(side=ctk.LEFT, padx=20)
        ctk.CTkButton(box, text="Kilépés", command=lambda: (box.destroy(), uj_ablak.destroy(), sys.exit())).pack(side=ctk.RIGHT, padx=20)


    kerdes_13_mt()




