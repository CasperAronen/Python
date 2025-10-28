class Hissi:
    def __init__(self, alinkerros=0, ylinkerros=10):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.nykykerros= 0
        self.paamaara = None

    def siirry_kerrokseen(self):
        h = int(input("Valitse kerros 1-10: "))
        if self.alinkerros <= h <= self.ylinkerros:
            self.paamaara = h
            print(f"Haluttu kerros {self.paamaara}")
        else:
            print(f"Virheellinen kerros")

    def kerros_ylos(self, muutos=1):
        if self.nykykerros + muutos <= self.ylinkerros:
            self.nykykerros += muutos
            print(f"Hissi nousi kerrokseen {self.nykykerros}")


    def kerros_alas(self, muutos=1):
        if self.nykykerros - muutos >= self.alinkerros:
            self.nykykerros -= muutos
            print(f"Hissi laski kerrokseen {self.nykykerros}")

class Talo:
    def __init__(self, hissienMaara=4):
        self.hissit = [Hissi() for _ in range(hissienMaara)]
        self.hissienMaara = hissienMaara

    def aja_hissia(self):
        self.tiettyHissi = int(input(f"Mikä hissi 1-{self.hissienMaara}: "))
        if 1 <= self.tiettyHissi <= self.hissienMaara:
            return self.hissit[self.tiettyHissi - 1]
        else:
            print(f"Hissiä {self.tiettyHissi} ei ole olemassa")
            return None


TalonHissit = Talo(hissienMaara=4)
valitseHissi = TalonHissit.aja_hissia()

if valitseHissi:
    print(f"Valittu hissi {TalonHissit.tiettyHissi}")
    valitseHissi.nykykerros = 0
    valitseHissi.siirry_kerrokseen()

    if valitseHissi.paamaara is not None:
        while valitseHissi.nykykerros < valitseHissi.paamaara:
            valitseHissi.kerros_ylos()

        while valitseHissi.nykykerros > valitseHissi.alinkerros:
            valitseHissi.kerros_alas()

