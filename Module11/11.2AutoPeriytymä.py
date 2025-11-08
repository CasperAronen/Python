class Auto:

    def __init__(self, rekisteriN, huippuN):
        self.rekisteriN = rekisteriN
        self.huippuN = huippuN
        self.nopeus = 0
        self.matka = 0


    def kiihdyta(self, muutos ):
        self.nopeus += muutos

        if self.nopeus > self.huippuN:
            self.nopeus = self.huippuN
        elif self.nopeus < 0:
            self.nopeus = 0

        return f"Nopeus nyt {self.nopeus:.1f} km/h"

    def kulje(self, matka, aika):
        self.matka = matka + (self.nopeus* aika)
        return f"Auton {self.rekisteriN} kuljettu matka {self.matka}."

class SahkoA(Auto):
    def __init__(self, rekisteriN, huippuN, akuKapasi):
        Auto.__init__(self, rekisteriN, huippuN)
        self.akuKapasi = akuKapasi

    def tiedot(self):
        print(f"{self.rekisteriN}, {self.huippuN}Km/h, {self.akuKapasi}KwH ")

class PolttoA(Auto):
    def __init__(self, rekisteriN, huippuN, MoottoriTilavuus):
        Auto.__init__(self, rekisteriN, huippuN)
        self.MoottoriTilavuus = MoottoriTilavuus
    def tiedot(self):
        print(f"{self.rekisteriN}, {self.huippuN}Km/h, {self.MoottoriTilavuus}L ")

Sa1 = SahkoA("ABC-123", 100, "10")
Pa1 = PolttoA("ABC-321", 100, "100")

Sa1.tiedot()
Pa1.tiedot()

Sa1.kiihdyta(50)
Pa1.kiihdyta(80)

print(Sa1.kulje(0, 3))
print(Pa1.kulje(0, 3))

