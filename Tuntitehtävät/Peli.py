hahmot = ["Seppo", "Jarmo", "Jaakko"]
ajoneuvot = ["Bussi", "Auto", "Pyörä"]
print("Tervetuloa peliini")
while True:
    try:
        for i in hahmot:
            print(i)
        hnPut = input("Valitse hahmosi: ")
        if hnPut in hahmot:
            print("Valitsit", hnPut)
            print("Pelimme sankari", hnPut, "päätti eräänä kauniina perjantai")
            print("Käymään hakemaan alkosta vähäsen jano juomaa")
            print("Muttei hän keksinyt millä mennä hakemaan alkosta juotavaa")
            print("Millä hänen pitäisi mennä alkoon vai pitäisikö jäädä himaan")
            for a in ajoneuvot:
                print(a)
            aInput = input("Valitse ajoneuvosi")
            if aInput in ajoneuvot == "Bussi":
                print("Valitsit", aInput)
                print("kaupungin sankari", hnPut, "valitsi ajoneuvokseen", aInput)
                break
            elif aInput in ajoneuvot == "Auto":
                print("Valitsit", aInput)
                print("kaupungin saknari", hnPut, "valitsi ajoneuvokseen", aInput)
                break
            elif aInput in ajoneuvot == "Pyörä":
                print("Valitsit", aInput)
                print("Kaupungin sankari", hnPut, "valitsi ajoneuvokseen", aInput)
                break
        else:
            print("Osaatko kirjoittaa")
            print("Tuosta hyvästä peli loppuu")
            exit()
    except ValueError:
        print("Oho")