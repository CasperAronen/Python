NimiLista = []
while True:
    try:
        syote = input("Anna nimi, lopeta antamalla tyhjä: ").lower()
        if syote == "":
            break
        if syote.isdigit():
            print("Et voi syöttää numeroa nimenä. Yritä uudelleen.")
            continue
        elif syote in NimiLista:
            print("Aiemmin syötetty nimi")
            nimi = str(syote).lower()
        else:
            print("Uusi Nimi")
            nimi = str(syote).lower()
            NimiLista.append(nimi)
    except ValueError:
        print("lmao")

print(NimiLista)
for i in range(0, len(NimiLista)):
    print(NimiLista[i])