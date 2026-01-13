KATEGOORIAD = ("Toit", "Transport", "Meelelahutus", "Muu")
    
def lisa_kulu_tulu(kirjed, summa, kategooria, kirjeldus, tyyp):
    if kategooria not in KATEGOORIAD:
        raise ValueError(f"Tundmatu kategooria: {kategooria}")
    if tyyp not in ("kulu", "tulu"):
        raise ValueError("Tüüp peab olema 'kulu' või 'tulu'")

    kirje = {
        "summa": float(summa),
        "kategooria": kategooria,
        "kirjeldus": kirjeldus,
        "tyyp": tyyp
    }

    kirjed.append(kirje)


def unikaalsed_kategooriad(jarjend):
    return {kirje["kategooria"] for kirje in jarjend}


def arvuta_kategooriad(jarjend):
    statistika = {}

    for kirje in jarjend:
        kat = kirje["kategooria"]
        summa = kirje["summa"]

        if kat not in statistika:
            statistika[kat] = 0

        if kirje["tyyp"] == "kulu":
            statistika[kat] -= summa
        else:
            statistika[kat] += summa

    return statistika


def kysi_summa():
    while True:
        sisend = input("Sisesta summa: ")
        try:
            return float(sisend)
        except ValueError:
            print(" Viga: palun sisesta arv (nt 12.50)")


def kysi_kategooria():
    while True:
        kategooria = input(f"Sisesta kategooria {KATEGOORIAD}: ")
        if kategooria in KATEGOORIAD:
            return kategooria
        print(" Tundmatu kategooria")


def kysi_tyyp():
    while True:
        tyyp = input("Kas tegu on kuluga või tuluga? (kulu/tulu): ").lower()
        if tyyp in ("kulu", "tulu"):
            return tyyp
        print(" Viga: sisesta 'kulu' või 'tulu'")


kirjed = []

summa = kysi_summa()
kategooria = kysi_kategooria()
kirjeldus = input("Kirjeldus: ")
tyyp = kysi_tyyp()

lisa_kulu_tulu(kirjed, summa, kategooria, kirjeldus, tyyp)

print("\nKirjed:")
for k in kirjed:
    print(k)

print("\nStatistika kategooriate kaupa:")
print(arvuta_kategooriad(kirjed))