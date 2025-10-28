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


hissi = Hissi()
hissi.nykykerros = 0


hissi.siirry_kerrokseen()
while hissi.nykykerros < hissi.paamaara:
    hissi.kerros_ylos()

print(f"Saavuit kerrokseen {hissi.nykykerros}")

while hissi.nykykerros > hissi.alinkerros:
    hissi.kerros_alas()

print(f"Palasit alimpaan kerrokseen {hissi.nykykerros}")