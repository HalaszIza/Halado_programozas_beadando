import random
import tkinter as tk
import sys
import customtkinter as ctk #Designhoz
from tkinter import messagebox
#from customtkinter import * #Designhoz
from PIL import Image, ImageTk #Designhoz

#Design elemek
#set_appearance_mode("dark")

betuk = ['A)', 'B)', 'C)', 'D)']
kerdesek_13 = 0
kerdes_1_3 = 0
kerdesek_45 = 0
kerdes_4_5 = 0
kerdesek_67 = 0
kerdes_6_7  = 0

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
foablak.title("Legyen Ön is mérnökinfós!")
foablak.geometry("800x600")

background_image = Image.open("Images/nje_logo.png")
image = background_image.resize((800, 600), Image.Resampling.LANCZOS)
bg_image = ImageTk.PhotoImage(image)


lbl = ctk.CTkLabel(foablak, text="Legyen Ön is mérnökinfós kvízjáték!\nFeladat 7 helyes válasz megadása.\nAz első 3 kérdés Neumann Jánosról fog szólni.\nAz utána következő négy pedig a Hálózatbiztonsági és üzemeltetési-és Ipari informatika specializációról fog szólni.\n\
                   😜Kezdődhet a játék?😜", font=("Apostol", 18), image=bg_image)
lbl.pack(padx=20, pady=20)
lbl.place(relx=0, rely=0, relwidth=1, relheight=1)
lbl.lower()


eredmeny = ctk.CTkLabel(foablak, text="", font=("Arial", 12))
eredmeny.pack(pady=10)

def kerdesek13_ablak():
    global kerdes_1_3
    global kerdesek_13
    foablak.withdraw()

    uj_ablak = ctk.CTkToplevel()
    uj_ablak.title("Játék!")
    uj_ablak.geometry("600x500")

    helyes_e_lbl = ctk.CTkLabel(uj_ablak, text="", font=("Arial", 12))
    helyes_e_lbl.pack(pady=10)

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
            vlsz_btn = ctk.CTkButton(uj_ablak, text=betuk[i] + btn_sz, 
                                 command=lambda txt=btn_sz: (krd_ell(txt, kov_btn), gomb_sz(vlsz_btn.cget("text"))))
            gombok.append(vlsz_btn)
            vlsz_btn.pack(pady=5)

        def gomb_sz(text):
            {"text"}

        kov_btn.configure(state="disabled")
        helyes_e_lbl.configure(text="")

    def krd_ell(vlsz_btn_sz, kovetkezo_gomb):
        helyes_idx = megoldas_1[kerdes_1_3]

        if vlsz_btn_sz == helyes_idx:
            helyes_e_lbl.configure(text="Helyes!")
            kovetkezo_gomb.configure(state="normal")
        else:
            helyes_e_lbl.configure(text="Helytelen!")
            show_msgbox()

    def kov_kerdes():
        global kerdesek_13
        kerdesek_13 += 1
        if kerdesek_13 < 3:
            kerdes_13_mt()
        else:
            kov_blokkbox()


    def kov_blokkbox():
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

#4-5 kérdés



#6-7 kérdés
def kerdesek67_ablak():
    global kerdes_6_7
    global kerdesek_67

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
        box = tk.Toplevel(uj_ablak)
        box.title("Vége a játéknak.")
        box.geometry("300x150")
        box.grab_set()

        tk.Label(box, text="A válasz helytelen, a játéknak vége.", font=("Arial", 12)).pack(pady=20)

        tk.Button(box, text="Új játék", command=lambda: (box.destroy())).pack(side=tk.LEFT, padx=20)
        tk.Button(box, text="Kilépés", command=lambda: (box.destroy(), uj_ablak.destroy(), sys.exit())).pack(side=tk.RIGHT, padx=20)

    def show_exitbox():
        box = tk.Toplevel(uj_ablak)
        box.title("Vége a játéknak.")
        box.geometry("300x150")
        box.grab_set()

        tk.Label(box, text="Minden kérdésre helyesen válaszoltál, a játéknak vége.", font=("Arial", 12)).pack(pady=20)

        tk.Button(box, text="Új játék", command=lambda: (box.destroy())).pack(side=tk.LEFT, padx=20)
        tk.Button(box, text="Kilépés", command=lambda: (box.destroy(), uj_ablak.destroy(), sys.exit())).pack(side=tk.RIGHT, padx=20)

    kerdes_67_mt()

start_btn = ctk.CTkButton(foablak, text="Kezdjünk hozzá!", command=kerdesek13_ablak)
start_btn.pack(pady=50)
start_btn.place(relx=0.45, rely=0.7)

foablak.mainloop()

