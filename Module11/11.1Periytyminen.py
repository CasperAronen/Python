class Julkaisu:
    def __init__(self, nimi, kirjoittaja):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivut):
        Julkaisu.__init__(self, nimi, kirjoittaja)
        self.sivut = sivut

    def tulosta_tiedot(self):
        print(f"Teoksen kirjoittaja: {self.kirjoittaja} Teos: {self.nimi} sivut: {self.sivut}")

class Lehti(Julkaisu):
    def __init__(self, nimi, kirjoittaja):
        Julkaisu.__init__(self, nimi, kirjoittaja)

    def tulosta_tiedot(self):
        print(f"Lehden nimi: {self.nimi}, paakirjoittaja {self.kirjoittaja}")



kirja1 = Kirja("Hannun kirja", "Jaakko kivi", 500)
lehti1 = Lehti("retu lehti", "Peka tomu")

kirja1.tulosta_tiedot()
print()
lehti1.tulosta_tiedot()