import random
import tkinter as tk
import sys
import customtkinter as ctk #Designhoz
from tkinter import messagebox
#from customtkinter import * #Designhoz
from PIL import Image, ImageTk #Designhoz
from customtkinter import CTkImage
import krd67



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


    kov_btn = ctk.CTkButton(uj_ablak, text="Következő kérdés", command=lambda: kov_kerdes, state="disabled")
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
            vlsz_btn = tk.Button(uj_ablak, text= betuk[i] + btn_sz, 
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
        helyes_idx = megoldas_1[kerdes_1_3]

        if vlsz_btn_sz == helyes_idx:
            helyes_e_lbl.configure(text="Helyes!")
            kovetkezo_gomb.configure(state="normal")
        else:
            helyes_e_lbl.configure(text="Helytelen!")
            show_msgbox

        for vlsz_btn in gombok:
            vlsz_btn.configure(state="disabled")
        kov_btn.configure(state="normal")

    def kov_kerdes():
        kerdesek_13 += 1
        if kerdesek_13 < 3:
            kerdes_13_mt()
        else:
            kov_blokkbox()


    def kov_blokkbox():
        global kerdesek67_ablak
        uj_ablak.withdraw()
        box = tk.Toplevel(foablak)
        box.title("3/3, nem semmi.")
        box.geometry("500x300")
        box.grab_set()

        tk.Label(box, text="Eddig 3/7, csak így tovább. A következő 2 kérdés a há.", font=("Arial", 12)).pack(pady=20)
        tk.Button(box, text="Következő kérdések.", command=lambda: (box.destroy(), kerdesek67_ablak())).pack(side=tk.RIGHT,padx=20)

    def show_msgbox():
        box = ctk.CTkToplevel(uj_ablak)
        box.title("Vége a játéknak.")
        box.geometry("300x150")
        box.grab_set()

        ctk.CTkLabel(box, text="A válasz helytelen, a játéknak vége.", font=("Arial", 12)).pack(pady=20)
        ctk.CTkButton(box, text="Új játék", command=lambda: (box.destroy())).pack(side=ctk.LEFT, padx=20)
        ctk.CTkButton(box, text="Kilépés", command=lambda: (box.destroy(), uj_ablak.destroy(), sys.exit())).pack(side=ctk.RIGHT, padx=20)


    kerdes_13_mt()




