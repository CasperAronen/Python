LukuLista = []
jako2 = []

def jaolliset_kakkosella():
    for luku in LukuLista:
        if luku % 2 == 0:
            jako2.append(luku)

while True:
    try:
        syote = input("Anna luku, lopeta antamalla tyhjä: ")
        if syote == "":
            break
        luku = int(syote)
        LukuLista.append(luku)
    except ValueError:
        print("Syötä vain kokonaisluku tai tyhjä lopettaaksesi.")

jaolliset_kakkosella()

print("Parilliset luvut:", jako2,"Parillisten summa", sum(jako2))


