sukupuoli = input("Anna sukupuolesi (Mies vai Nainen): ")
hemoglobiini = int(input("Anna hemoglobiini arvosi: "))

if sukupuoli == "Mies":
    if hemoglobiini > 195:
        print("Hemoglobiini arvosi ovat korkeat (M)")
    elif hemoglobiini < 134:
        print("Hemoglobiini arvosi ovat matalat (M)")
    else:
        print("Hemoglobiini arvosi ovat tasaiset (M)")
if sukupuoli == "Nainen":
    if hemoglobiini > 175:
        print("Hemoglobiini arvosi ovat korkeat (N)")
    elif hemoglobiini < 117:
        print("Hemoglobiini arvosi ovat matalat (N)")
    else:
        print("Hemoglobiini arvosi ovat tasaiset (N)")
else:
    print("Virheellinen vastaus")