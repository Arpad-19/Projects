
import hashlib

def hash_generalas(szoveg):
    # szöveget byte-okra alakítjuk
    byte_szoveg = szoveg.encode('utf-8')

    # SHA-256 hash létrehozása
    hash_obj = hashlib.md5(byte_szoveg)

    # hexadecimális formátum
    return hash_obj.hexdigest()


# --- program indul ---
szoveg = input("Add meg a szöveget: ")

eredmeny = hash_generalas(szoveg)

print("\n🔐 Hash érték (MD5):")
print(eredmeny)


import hashlib
import itertools
import string

def md5_hash(szoveg):
    return hashlib.md5(szoveg.encode()).hexdigest()


# --- cél hash (amit "feltörünk") ---
cel = input("Add meg a MD5 hash-t: ")

karakterek = string.ascii_lowercase  # csak kisbetűk (egyszerűsítés)

print("\n🧱 Brute force indul...\n")

talalat = False

# 1-től 4 karakterig próbálkozunk
for hossz in range(1, 64):
    for kombinacio in itertools.product(karakterek, repeat=hossz):
        probal = "".join(kombinacio)

        if md5_hash(probal) == cel:
            print("🔓 Megtalált jelszó:", probal)
            talalat = True
            break

    if talalat:
        break

if not talalat:
    print("❌ Nem találtam meg (vagy túl hosszú/komplex)")