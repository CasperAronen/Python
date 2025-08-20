vuosi = int(input("Anna vuosiluku: "))

if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print("Vuosi", vuosi, "on karkaus vuosi")
else:
    print("Vuosi", vuosi, "ei ole karkausvuosi")