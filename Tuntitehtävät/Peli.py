hahmot = ["Seppo", "Jarmo", "Jaakko"]
print("Tervetuloa peliini")
while True:
    try:
        for i in range(0, len(hahmot)):
            print(hahmot[i])
        hnPut = input("Valitse hahmosi: ")
        if hnPut in hahmot:
            print("Valitsit", hnPut)
            print("Pelimme sankari", hnPut, "")
        else:
            print("Osaatko kirjoittaa")
            print("Tuosta hyvästä peli loppuu")
            exit()
    except ValueError:
        print("Oho")