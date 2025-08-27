pHalkaisija = float(input("Anna ensimmäisen pyöreän pizzan halkaisija (cm): "))
pizzaHinta = float(input("Anna ensimmäisen pizzan hinta: "))
pHalkaisija2 = float(input("Anna toisen pyöreän pizzan halkaisija (cm): "))
pizzaHinta2 = float(input("Anna toisen pizzan hinta: "))

def YksioHinta():
    nelioMetri = ((pHalkaisija * pHalkaisija) * 3.14) / 4
    nelioMetri2 = ((pHalkaisija2 * pHalkaisija2) * 3.14) / 4
    pVertailu = pizzaHinta/nelioMetri
    pVertailu2 = pizzaHinta / nelioMetri2
    return pVertailu, pVertailu2
hinta1, hinta2 = YksioHinta()

if hinta1 < hinta2:
    print(f"Ensimmäisen pizzan yksilöhinta on parempi {hinta1:.1}€")
elif hinta2 < hinta1:
    print(f"Toisen pizzan hinta on parempi {hinta2:.1}€")