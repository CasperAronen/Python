import random
def Noppa():
    return random.randint(1, 6)

heitto = Noppa()
while heitto != 6:
    print("Heitit:", heitto)
    heitto = Noppa()

print("Heitit:", heitto)
