gallon = float(input("Anna galonin määrä: "))

def BensaMuunnos():
    gallonM = gallon * 3.785
    return gallonM
while True:
    if gallon > 0:
        BensaMuunnos()
        print("Bensa muunnos:", BensaMuunnos())
        gallon = float(input("Anna galonin määrä: "))
    else:
        print("Bensa loppu idiotos")
        break