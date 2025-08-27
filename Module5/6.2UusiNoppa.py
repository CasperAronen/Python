import random

uNoppa = int(input("Anna nopan tahkojen määrä: "))

def Unoppa():
    return random.randint(1, uNoppa)

uHeitto = Unoppa()
while uHeitto != uNoppa:
    print("Heitit:", uHeitto)
    uHeitto = Unoppa()

print("Heitit:", uHeitto)
