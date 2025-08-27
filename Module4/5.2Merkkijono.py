LukuLista=[]
while True:
    try:
        luku = int(input("anna lukuja lopeta antamalla tyhjä: "))
        LukuLista.append(luku)
    except ValueError:
        break
LukuLista.sort(reverse=True)
print(LukuLista[0:5])



#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon
#lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta
#alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.