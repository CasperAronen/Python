LukuLista=[]
while True:
    try:
        luku = int(input("anna luku lopeta antamalla tyhjä: "))
        LukuLista.append(luku)
    except ValueError:
        break

print(min(LukuLista))
print(max(LukuLista))
print(LukuLista)