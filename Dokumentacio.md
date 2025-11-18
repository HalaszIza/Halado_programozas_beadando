# 🧠 Haladó Programozás Beadandó  

## 🎮 Kvízjáték: „Legyen Ön is mérnökinfós! :)”

### main.py
- Modulok és könyvtárak
  - `customtkinter (ctk):` Modernebb és testreszabhatóbb Tkinter GUI komponensekhez.
  - `PIL (Pillow) Image:` Képek betöltéséhez és kezeléséhez.
  - `krd13.py:` A következő blokk kódját tartalmazó saját modul.

- Változók
    - `betuk`: A lehetséges válaszok sorszámozásához használt betűsorozat (['A)', 'B)', 'C)', 'D)']).
    - Lista változók a kérdések, válaszok és helyes válaszok tárolására: `kerdes_01`, `valaszok_01`, `megoldas_1`.

- Adatbeolvasás
    - A `kerdesek_valaszok_01.txt` fájl beolvasása.
    - A beolvasott adatok három listába kerülnek, amelyeket később a játék kérdéseinek és válaszainak megjelenítéséhez használnak.

- Főablak felépítés
    - Főablak (`foablak`) létrehozása, címmel és 800x600 pixeles mérettel
    - Háttérkép (`nje_logo.png`) betöltése és CTkImage objektummá alakítása, majd a címke (`lbl`) háttereként beállítása.
    - Szöveges label, amely tájékoztat a játékról és a témáról, valamint a célról (7 helyes válasz teljesítése).
    - Eredménycímke (`eredmeny`), melyhez később az eredmény vagy visszajelzés írható.
    - Indító gomb (`start_btn`), amely elindítja a kérdések megjelenítését, meghívva a `krd13.kerdesek13_ablak` függvényt. Ennek paraméterei az előkészített kérdés, válasz és megoldás listák, valamint a válasz betűk.

- Futtatás
    - Végül a főablak fő eseményhurokja (`mainloop()`) elindul, ezzel a GUI interaktívvá válik.
    - Fontos, hogy mindig a `main.py`-ból indítsuk el a programot, hogy gond nélkül tudjuk a játékot játszani.

## krd13.py
- Modulok és könyvtárak
    - `random:` A random kérdések generálásához.
    - `sys:` A rendszer leállításához kell importálni.
    - `customtkinter (ctk):` Modernebb és testreszabhatóbb Tkinter GUI komponensekhez.
    - `PIL (Pillow) Image:` Képek betöltéséhez és kezeléséhez.
    - `krd45.py` a következő blokk (4–5. kérdés) kódját tartalmazó saját modul.
    - Kérdésadatbázis betöltése a második blokkhoz.(`kerdesek_valaszok_02.txt`) → kerdes_02, valaszok_02, megoldas_2 listák (ezek később lesznek használva a krd45 modulban).

- Globális változók a függvényben
    - `kerdesek_13:` hány kérdésre válaszolt helyesen ebben a blokkban (0–3).
    - `kerdes_1_3:` az aktuálisan kiválasztott kérdés indexe a kerdes_01 listában.

- Ablak felépítése
    - A főablak elrejtése (`foablak.withdraw()`).
    - Új CTkToplevel ablak létrehozása, címe: "Játék!".
    - **Felső részen:** `helyes_e_lbl:` "Helyes!" vagy "Helytelen!" üzenet.
    - **Alatta:** "Következő kérdés" gomb, eleinte letiltva

- Fontosabb belső függvények
    - `kerdes_13_mt()` – új kérdés megjelenítése
        - Eltávolítja az előző kérdés labelt és gombokat (ha léteznek).
        - Véletlenszerűen kiválaszt egy kérdést (random.randint(0, len-1)).
        - Létrehozza a kérdés CTkLabel-t narancssárga háttérrel.

    - `krd_ell(vlsz_btn_sz, kovetkezo_gomb)` – válasz ellenőrzése
        - `vlsz_btn_sz:` a kiválasztott válasz szövege (a betű nélkül).
        - Megkeresi a helyes választ: megoldas_1[kerdes_1_3].
        - **Ha egyezik:** "Helyes!", zöldre színezi a gombot,  engedélyezi a Következő gombot.
        - **Ha nem:** "Helytelen!", pirosra színezi a gombot, meghívja a show_msgbox()-ot (játék vége).
        - Minden gombot letilt, a Következő gombot engedélyezi.

    - `kov_kerdes()`
            - Ha még nincs meg a 3 helyes válasz, új kérdést ad (`kerdes_13_mt()`)
            - Ha megvan a 3 kérdés: `kov_blokkbox()` meghívása

    - `kov_blokkbox()` – blokk vége, továbbhaladás
            - Elrejti az aktuális játékablakot
            - Ha `kerdesek_13` = 0 külön ablak: "Egyik kérdésre sem tudtál helyesen válaszolni" → Új játék / Kilépés gombok
            - Ha `kerdesek_13` > 0: **Gratuláló ablak:** "Eddig 3/7, csak így tovább!". **Tovább gomb:** meghívja a `krd45.kerdesek45_ablak(...)`-ot és átadja a már betöltött második blokk adatait + ugyanazt a betuk listát.

    - `show_msgbox()` – azonnali játék vége hibás válasznál
        - **Kis felugró ablak:** "A válasz helytelen, a játéknak vége 😥"
        - **Gombok:** Új játék (újraindítja az 1–3. blokkot) vagy Kilépés (`sys.exit()`)

## krd45.py

- Adatbeolvasás
    - A `kerdesek_valaszok_01.txt` fájl beolvasása. Célja, hogyha a játékos valamelyik kérdést elrontja, akkor visszaugorjon az első ódblokkhoz.
    - A `kerdesek_valaszok_03.txt` fájl beolvasása a harmadik kódblokkhoz.
    - A beolvasott adatok három listába kerülnek, amelyeket később a játék kérdéseinek és válaszainak megjelenítéséhez használnak.

- Fontosabb belső függvények
    - Funkcióban ugyanazok, mint az előzőnél csak az elnevezések mások utalva arra hogy a második kérdésblokkba tartozó adatokat haszálja a rendszer.

## krd67.py

- Adatbeolvasás
    - A `kerdesek_valaszok_01.txt` fájl beolvasása. Célja, hogyha a játékos valamelyik kérdést elrontja, akkor visszaugorjon az első ódblokkhoz.

- Fontosabb belső függvények
    - Funkcióban ugyanazok, mint az előzőnél csak az elnevezések mások utalva arra hogy a második kérdésblokkba tartozó adatokat haszálja a rendszer.
    - Sikeres teljesítés esetén nincs tovább, ez a játék vége.
    - A győzelmi ablak (`show_exitbox()`) pozitív hangvételű és nagyobb betűkkel kiemelt
    - Hibás válasz esetén is ugyanúgy vissza lehet menni az elejére (`krd13`)

## kerdesek_valaszok_01.txt, kerdesek_valaszok_02.txt, kerdesek_valaszok_03.txt

- txt felépítése:
    - Ezekben a fájlokban vannak a 3 kérdéscsoport kérdései. A kérdeé válaszok és megoldás pontosvesszővel, a 4 válaszlehetőség pedig szóközzel van elválasztva mindne esetben.