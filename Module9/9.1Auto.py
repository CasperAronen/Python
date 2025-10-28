class Auto:

    def __init__(self, rekisteriN, huippuN):
        self.rekisteriN = rekisteriN
        self.huippuN = huippuN
        self.Nnopeus = 0
        self.matka = 0

    def tieto(self):
        return f"Auton rekisteri numero {self.rekisteriN}. Auton huippunopeus {self.huippuN}Km/h. Auton tämänhetkinen nopeus {self.Nnopeus}. Auton kuljettu matka {self.matka}."

a1 = Auto("ABC-123", "142")

print(a1.tieto())

