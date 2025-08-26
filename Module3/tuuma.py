maara = int(input("Anna tuumien määrä: "))
tuuma = 2.54
while maara:
    if 0 < maara:
        muuntaja = maara * tuuma
        print(f"Tuumat muutettu senttimetreiksi: {muuntaja:.2f}")
        maara = int(input("Anna tuumien määrä: "))
    else:
        break