LukuLista=[]

def ListaLasku():
    print(sum(LukuLista))

while True:
    try:
        luku = int(input("anna luku lopeta antamalla tyhjä: "))
        LukuLista.append(luku)
    except ValueError:
        ListaLasku()




