import random
nopat=[]
ArpaMaara = int(input("Anna arpakuutioiden määrä: "))

for die in range(ArpaMaara):
    nopat.append(random.randint(1,6))
Nsum = sum(nopat)
print(nopat)
print("Noppien summa", Nsum)
