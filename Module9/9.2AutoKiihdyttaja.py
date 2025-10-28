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

a1 = Auto("ABC-123", 142)

a1.kiihdyta(30)
a1.kiihdyta(70)
print(a1.kiihdyta(50))
print(a1.kiihdyta(-200))

print(a1.tieto())

