import hashlib

# "adatbázis" (memóriában tároljuk)
felhasznalok = {}

def md5_hash(szoveg):
    return hashlib.md5(szoveg.encode()).hexdigest()


def regisztracio():
    felhasznalo = input("Új felhasználónév: ").strip()
    jelszo = input("Új jelszó: ").strip()

    if felhasznalo in felhasznalok:
        print("❌ Ez a felhasználónév már létezik!")
        return

    felhasznalok[felhasznalo] = md5_hash(jelszo)
    print("✅ Sikeres regisztráció!")


def bejelentkezes():
    felhasznalo = input("Felhasználónév: ").strip()
    jelszo = input("Jelszó: ").strip()

    if felhasznalo not in felhasznalok:
        print("❌ Nincs ilyen felhasználó!")
        return

    if felhasznalok[felhasznalo] == md5_hash(jelszo):
        print("✅ Sikeres bejelentkezés!")
    else:
        print("❌ Hibás jelszó!")


# --- fő program ---
while True:
    print("\n=== MENÜ ===")
    print("1 - Regisztráció")
    print("2 - Bejelentkezés")
    print("3 - Kilépés")

    valasztas = input("Válassz: ")

    if valasztas == "1":
        regisztracio()
    elif valasztas == "2":
        bejelentkezes()
    elif valasztas == "3":
        print("Kilépés...")
        break
    else:
        print("❌ Érvénytelen választás!")