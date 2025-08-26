sukupuoli = input("Anna sukupuolesi (Mies vai Nainen): ").lower()
hemoglobiini = int(input("Anna hemoglobiini arvosi: "))

if sukupuoli == "mies":
    if hemoglobiini > 195:
        print("Hemoglobiini arvosi ovat korkeat (M)")
        exit()
    elif hemoglobiini < 134:
        print("Hemoglobiini arvosi ovat matalat (M)")
        exit()
    else:
        print("Hemoglobiini arvosi ovat tasaiset (M)")
        exit()
elif sukupuoli == "nainen":
    if hemoglobiini > 175:
        print("Hemoglobiini arvosi ovat korkeat (N)")
        exit()
    elif hemoglobiini < 117:
        print("Hemoglobiini arvosi ovat matalat (N)")
        exit()
    else:
        print("Hemoglobiini arvosi ovat tasaiset (N)")
        exit()
else:
    print("Virheellinen vastaus")