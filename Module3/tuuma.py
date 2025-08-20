maara = int(input("Anna tuumien määrä: "))
tuuma = 2.54
while maara:
    if 0 < maara:
        muuntaja = maara * tuuma
        print("Tuumat muutettu senttimetreiksi: ",muuntaja)
        maara = int(input("Anna tuumien määrä: "))
    else:
        break