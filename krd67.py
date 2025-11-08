import random
import tkinter as tk
import sys
import customtkinter as ctk #Designhoz
from tkinter import messagebox
#from customtkinter import * #Designhoz
from PIL import Image, ImageTk #Designhoz
from customtkinter import CTkImage
#import krd45

#6-7 kérdés
def kerdesek67_ablak(kerdes_03, valaszok_03, megoldas_3, betuk):
    global kerdes_6_7
    global kerdesek_67

    kerdesek_67 = 0
    kerdes_6_7  = 0

    uj_ablak = tk.Toplevel()
    uj_ablak.title("Játék!")
    uj_ablak.geometry("600x500")

    helyes_e_lbl = tk.Label(uj_ablak, text="", font=("Arial", 12))
    helyes_e_lbl.pack(pady=10)

    kov_btn = tk.Button(uj_ablak, text="Következő kérdés", command=lambda: kov_kerdes(), state="disabled")
    kov_btn.pack(pady=10)

    #Következő 2 kérdés
    def kerdes_67_mt():
        global kerdes_6_7
        global vlsz_btn
        global gombok
        global krd_lbl

        if 'krd_lbl' in globals():
            krd_lbl.destroy()

        if 'gombok' in globals():
            for btn in gombok:
                btn.destroy()

        kerdes_6_7 = random.randint(0, len(kerdes_03) - 1)
        krd = kerdes_03[kerdes_6_7]
        krd_lbl = tk.Label(uj_ablak, text=krd, font=("Arial", 12))
        krd_lbl.pack(padx=20, pady=20)

        gombok = []
        for i in range(4):
            btn_sz = valaszok_03[kerdes_6_7][i]
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
        helyes_idx = megoldas_3[kerdes_6_7]

        if vlsz_btn_sz == helyes_idx:
            helyes_e_lbl.configure(text="Helyes!")
            kovetkezo_gomb.configure(state="normal")
        else:
            helyes_e_lbl.configure(text="Helytelen!")
            show_msgbox()

        for vlsz_btn in gombok:
            vlsz_btn.configure(state="disabled")
        kov_btn.configure(state="normal")

    def kov_kerdes():
        global kerdesek_67
        kerdesek_67 += 1

        if kerdesek_67 < 3:
            kerdes_67_mt()
        else:
            show_exitbox()

    def show_msgbox():
        box = ctk.CTkToplevel(uj_ablak)
        box.title("Vége a játéknak.")
        box.geometry("300x150")
        box.grab_set()

        ctk.CTkLabel(box, text="A válasz helytelen, a játéknak vége.", font=("Arial", 12)).pack(pady=20)
        ctk.CTkButton(box, text="Új játék", command=lambda: (box.destroy())).pack(side=ctk.LEFT, padx=20)
        ctk.CTkButton(box, text="Kilépés", command=lambda: (box.destroy(), uj_ablak.destroy(), sys.exit())).pack(side=ctk.RIGHT, padx=20)

    def show_exitbox():
        box = tk.Toplevel(uj_ablak)
        box.title("Vége a játéknak.")
        box.geometry("300x150")
        box.grab_set()

        tk.Label(box, text="Minden kérdésre helyesen válaszoltál, a játéknak vége.", font=("Arial", 12)).pack(pady=20)

        tk.Button(box, text="Új játék", command=lambda: (box.destroy())).pack(side=tk.LEFT, padx=20)
        tk.Button(box, text="Kilépés", command=lambda: (box.destroy(), uj_ablak.destroy(), sys.exit())).pack(side=tk.RIGHT, padx=20)

    kerdes_67_mt()
