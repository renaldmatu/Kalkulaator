Kategooriad = ("Toit", "Transport", "Meelelahutus", "Muu")

kirjed = []

kirje = {
    "summa": 12.50,
    "kategooria": "Toit",
    "kirjeldus": "Lõuna",
    "tyyp": "kulu"
}

def lisa_kulu_tulu(summa, kategooria, kirjeldus, tyyp):
    kirje = {
        "summa": summa,
        "kategooria": kategooria,
        "kirjeldus": kirjeldus,
        "tyyp": tyyp
    }
    kirjed.append(kirje)
    
def unikaalsed_kategooriad(jarjend):
    kategooriad = set()
    for kirje in jarjend:
        kategooriad.add(kirje["kategooria"])
    return kategooriad
    
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
