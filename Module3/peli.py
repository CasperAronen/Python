import random

satNum = random.randint(1, 10)

arvaus = int(input("Anna satunnainen numero 1-10 "))
while arvaus != satNum:
    if arvaus < satNum:
        arvaus = int(input("Arvaus liian pieni, arvaa uudelleen: "))
    elif arvaus > satNum:
        arvaus = int(input("Arvaus liian suuri, arvaa uudelleen: "))

print("Arvaus oikein! Numero oli:", satNum)
