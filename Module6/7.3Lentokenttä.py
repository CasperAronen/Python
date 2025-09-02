Lentokentta = ["Helsinki"]
ICAOkoodi = ["09001"]

def Valinta():
    valitse = input("Haluatko lisätä tai hakea lentokenttää vaikko lopettaa(uusi, valinta, lopeta): ").lower()
    return valitse
while True:
    toiminto = Valinta()
    if toiminto == "uusi":
        lentokentta = input("Minkä nimisen lentokentän haluat lisätä: ")
        Lentokentta.append(lentokentta)
        koodi = (input("Anna ICAO-koodi "))
        ICAOkoodi.append(koodi)
    elif toiminto == "valinta":
        haku = input("Hae lentokenttä ICAO-koodilla: ")
        if haku in ICAOkoodi:
            index = ICAOkoodi.index(haku)
            print(f"Löytyi: {Lentokentta[index]} (ICAO: {ICAOkoodi[index]})")
        else:
            print(f"Lentokenttää ei löytynyt")
    elif toiminto == "lopeta":
        print("Ohjelma loppuu babaiiii")
        break
    else:
        print("Virheellinen inputti (forgor mikä input suomeksi oli)")