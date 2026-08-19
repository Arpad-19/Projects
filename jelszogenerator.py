'''
import random
import string

def jelszo_generalas(hossz):
    karakterek = string.ascii_letters + string.digits + string.punctuation

    jelszo = "".join(random.choice(karakterek) for _ in range(hossz))
    return jelszo

try:
    hossz = int(input("Add meg a jelszó hosszát: "))

    if hossz < 4:
        print("A jelszó hossza legyen legalább 4 karakter!")
    else:
        print("Generált jelszó:", jelszo_generalas(hossz))

except ValueError:
    print("Kérlek, egy érvényes számot adj meg!")
'''

import secrets
import string

def eros_jelszo(hossz=16):
    karakterek = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(karakterek) for _ in range(hossz))

print("Generált jelszó:", eros_jelszo())