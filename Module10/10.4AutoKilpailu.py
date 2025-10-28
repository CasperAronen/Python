import random
class Auto:
    autot = []
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

    def kulje(self, aika, maxMatka=10000):
        self.matka += self.nopeus* aika

        if self.matka >= maxMatka:
            self.matka = maxMatka
            return "Voitto"

for i in range(10):
    rekisteriN = f"ABC-{i+1}"
    huippuN = random.randint(100, 200)
    uusiAuto = Auto(rekisteriN, huippuN)
    Auto.autot.append(uusiAuto)

class Kilpailu():
    def __init__(self, nimi, pituusKm, autojenMaara=10):
        self.nimi = nimi
        self.pituusKm = pituusKm
        self.autot = []

        for i in range(autojenMaara):
            rekisteriN = f"ABC-{i+1}"
            huippuN = random.randint(100, 200)
            auto = Auto(rekisteriN, huippuN)
            self.autot.append(auto)

    def autonNopeus(self, muutos):
        for auto in Auto.autot:
            auto.kiihdyta(muutos)
    def kilpailuOhi(self):
        if KisaOhi:
            print(f"Kilpailu on ohi auto {voitto.rekisteriN} on Romu Rallin voittaja")

kisa = Kilpailu("Romu Ralli", pituusKm = 8000)

kierrosMaara=1
KisaOhi = False
while not KisaOhi:
    kierrosMaara += 1
    for auto in kisa.autot:
        SatunnainenNopeus = random.randint(-10, 15)
        auto.kiihdyta(SatunnainenNopeus)
        if auto.kulje(aika=kierrosMaara, maxMatka=kisa.pituusKm):
            voitto=auto
            KisaOhi = True
            break
        elif kierrosMaara % 10 == 0:
            print(auto.tieto())
    else:
        continue
    break

for kaikkiAutot in Auto.autot:
    print(kaikkiAutot.tieto())
kisa.kilpailuOhi()