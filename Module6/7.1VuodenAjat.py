vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")
kuukausi = int(input("Anna kuukausi numerona 1-12: "))

if kuukausi in (12, 1 ,2):
    print("Vuoden aika on ", vuodenajat[0])
elif kuukausi in (3,4,5):
    print("Vuoden aika on ", vuodenajat[1])
elif kuukausi in (6,7,8):
    print("Vuoden aika on ", vuodenajat[2])
elif kuukausi in (9,10,11):
    print("Vuoden aika on ", vuodenajat[3])
else:
    print("Virheellinen vuoden aika")
