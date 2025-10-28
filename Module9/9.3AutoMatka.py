class Auto:

    def __init__(self, rekisteriN, huippuN, ):
        self.rekisteriN = rekisteriN
        self.huippuN = huippuN
        self.nopeus = 0
        self.matka = 0
    def tieto(self):
        return (f"Auton rekisteri numero {self.rekisteriN}."
                f" Auton huippunopeus {self.huippuN}Km/h."
                f" Auton tämänhetkinen nopeus {self.nopeus}."
                f" Auton kuljettu matka {self.matka}.")

    def kiihdyta(self, muutos ):
        self.nopeus += muutos

        if self.nopeus > self.huippuN:
            self.nopeus = self.huippuN
        elif self.nopeus < 0:
            self.nopeus = 0

        return f"Nopeus nyt {self.nopeus:.1f} km/h"

    def kulje(self, matka, aika):
        self.matka = matka + (self.nopeus* aika)
        return f"Auton kuljettu matka {self.matka}."

a1 = Auto("ABC-123", 142)
a1.kiihdyta(60)
print(a1.kulje(2000, 1.5))


print(a1.tieto())

