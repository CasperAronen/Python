import random

satNum = random.randint(1, 10)
arvaus = int(input("Arvaa luku 1-10 väliltä: "))

while arvaus != satNum:
        if arvaus < satNum:
            arvaus=int(input("Arvaus liian pieni arvaa uudelleen: "))
        elif arvaus > satNum:
            arvaus=int(input("Arvaus liian suuri arvaa uudelleen: "))

print("Arvaus oikein numero oli: ",satNum)