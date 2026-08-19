'''
def caesar_titkosit(szoveg, eltolas):
    eredmeny = ""

    for karakter in szoveg:
        # nagybetűk
        if karakter.isupper():
            uj = chr((ord(karakter) - ord('A') + eltolas) % 26 + ord('A'))
            eredmeny += uj

        # kisbetűk
        elif karakter.islower():
            uj = chr((ord(karakter) - ord('a') + eltolas) % 26 + ord('a'))
            eredmeny += uj

        # nem betűk (pl. szóköz, írásjel)
        else:
            eredmeny += karakter

    return eredmeny


# --- program indul ---
szoveg = input("Add meg a titkosítandó szöveget: ")
eltolas = int(input("Add meg az eltolás mértékét (pl. 3): "))

titkositott = caesar_titkosit(szoveg, eltolas)

print("Titkosított szöveg:", titkositott)
'''

def caesar(szoveg, eltolas):
    eredmeny = ""

    for karakter in szoveg:
        if karakter.isupper():
            uj = chr((ord(karakter) - ord('A') + eltolas) % 26 + ord('A'))
            eredmeny += uj

        elif karakter.islower():
            uj = chr((ord(karakter) - ord('a') + eltolas) % 26 + ord('a'))
            eredmeny += uj

        else:
            eredmeny += karakter

    return eredmeny


def brute_force(szoveg):
    print("\n🧱 Brute force eredmények:\n")
    for i in range(26):
        print(f"{i:2d}: {caesar(szoveg, i)}")


# --- fő program ---
print("=== Caesar-kód program ===")
print("1 - Titkosítás")
print("2 - Visszafejtés")
print("3 - Brute force feltörés")

valasztas = input("\nVálassz (1/2/3): ")

if valasztas in ["1", "2"]:
    szoveg = input("Add meg a szöveget: ")
    eltolas = int(input("Add meg az eltolást: "))

    if valasztas == "1":
        print("\n🔐 Titkosított szöveg:", caesar(szoveg, eltolas))
    else:
        print("\n🔓 Visszafejtett szöveg:", caesar(szoveg, -eltolas))

elif valasztas == "3":
    szoveg = input("Add meg a titkosított szöveget: ")
    brute_force(szoveg)

else:
    print("❌ Érvénytelen választás!")