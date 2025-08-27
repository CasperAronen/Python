maara = int(input("Anna tuumien määrä: "))
tuuma = 2.54
while maara:
    if maara > -1:
        muuntaja = maara * tuuma
        print(f"Tuumat muutettu senttimetreiksi: {muuntaja:.2f}")
        maara = int(input("Anna tuumien määrä: "))
    else:
        print("Väärin")
        break