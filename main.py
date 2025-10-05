import random
import tkinter as tk
from tkinter import messagebox

#Eső négy kérdés
with open("kerdesek_valaszok_01.txt", "r", encoding="utf-8") as file_1:
    
    kerdes_01 = []
    valasz_A_01 = []
    valasz_B_01 = []
    valasz_C_01 = []
    valasz_D_01 = []

    for sor_1 in file_1:
        sor_1 = sor_1.strip().split(";")
        kerdes_01.append(sor_1[0])
        valasz_A_01.append(sor_1[1])
        valasz_B_01.append(sor_1[2])
        valasz_C_01.append(sor_1[3])
        valasz_D_01.append(sor_1[4])

# Tesztelés:            
#print(f"{kerdes_01[0]}")
#print(f"{valasz_A_01[0]} {valasz_B_01[0]} {valasz_C_01[0]} {valasz_D_01[0]}")

#Második két kérdés



# Harmadik két kérdés
with open("kerdesek_valaszok_03.txt", "r", encoding="utf-8") as file_3:
    
    kerdes_03 = []
    valasz_A_03 = []
    valasz_B_03 = []
    valasz_C_03 = []
    valasz_D_03 = []

    for sor_3 in file_3:
        sor_3 = sor_3.strip().split(";")
        kerdes_03.append(sor_3[0])
        valasz_A_03.append(sor_3[1])
        valasz_B_03.append(sor_3[2])
        valasz_C_03.append(sor_3[3])
        valasz_D_03.append(sor_3[4])

# Tesztelés:            
#print(f"{kerdes_01[0]}")
#print(f"{kerdes_03[0]}")
#print(f"{valasz_A_03[0]} {valasz_B_03[0]} {valasz_C_03[0]} {valasz_D_03[0]}")

def nyit_uj_ablak():
    foablak.withdraw()

    uj_ablak = tk.Toplevel()
    uj_ablak.title("Játék!")
    uj_ablak.geometry("600x500")

    for i in range(1):
        kerdes_1_4 = random.choice(kerdes_01)
        lbl = tk.Label(uj_ablak, text=kerdes_1_4, font=("Arial", 12))
        lbl.pack(pady=20)

    bezar = tk.Button(uj_ablak, text="Bezárás", command=uj_ablak.destroy)
    bezar.pack()

    A_btn = tk.Button(uj_ablak, text="A válasz", command=lambda: visszahozo(foablak, uj_ablak))
    A_btn.pack()

    B_btn = tk.Button(uj_ablak, text="B válasz", command=lambda: visszahozo(foablak, uj_ablak))
    B_btn.pack()

    C_btn = tk.Button(uj_ablak, text="C válasz", command=lambda: visszahozo(foablak, uj_ablak))
    C_btn.pack()

    D_btn = tk.Button(uj_ablak, text="D válasz", command=lambda: visszahozo(foablak, uj_ablak))
    D_btn.pack()

def visszahozo(foablak, uj_ablak):
    uj_ablak.destroy()  
    foablak.deiconify()

# Főablak
foablak = tk.Tk()
foablak.title("Legyen Ön is mérnökinfós! :)")
foablak.geometry("800x600")

lbl = tk.Label(foablak, text="Legyen Ön is mérnökinfós kvízjáték.\nFeladat 7 helyes válasz megadás.\nKezdődhet a játék?")
lbl.pack(padx=20, pady=20)

# Gomb
gomb_1 = tk.Button(foablak, text="Kezdjünk hozzá!", command=nyit_uj_ablak)
gomb_1.pack(pady=50)

# Futtatás
foablak.mainloop()