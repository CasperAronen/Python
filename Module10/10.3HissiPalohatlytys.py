class Hissi:
    def __init__(self,numero, alinkerros=0, ylinkerros=10):
        self.numero = numero
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
            print(f"Hissi {self.numero} nousi kerrokseen {self.nykykerros}")


    def kerros_alas(self, muutos=1):
        if self.nykykerros - muutos >= self.alinkerros:
            self.nykykerros -= muutos
            print(f"Hissi {self.numero} laski kerrokseen {self.nykykerros}")

class Talo:
    def __init__(self, hissienMaara=4):
        self.hissit = [Hissi(i + 1) for i in range(hissienMaara)]
        self.hissienMaara = hissienMaara

    def aja_hissia(self):
        self.tiettyHissi = int(input(f"Mikä hissi 1-{self.hissienMaara}: "))
        if 1 <= self.tiettyHissi <= self.hissienMaara:
            return self.hissit[self.tiettyHissi - 1]
        else:
            print(f"Hissiä {self.tiettyHissi} ei ole olemassa")
            return None
    def palohalytys(self):
        print("Palohalytys")
        for hissi in self.hissit:
           while hissi.nykykerros > hissi.alinkerros:
               hissi.kerros_alas()

TalonHissit = Talo(3)
TalonHissit.hissit[0].nykykerros = 2
TalonHissit.hissit[1].nykykerros = 4
TalonHissit.hissit[2].nykykerros = 3

TalonHissit.palohalytys()


