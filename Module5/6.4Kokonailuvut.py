LukuLista=[]
MuutLista=[]
def ListaLasku():
    return print(sum(MuutLista))
while True:
    try:
        luku = int(input("anna luku lopeta antamalla tyhjä: "))
        LukuLista.append(luku)
        MuutLista.append(luku)
    except ValueError:
        ListaLasku()
        print(MuutLista)

