LukuLista=[]
MuutLista=[]
def ListaLasku():


while True:
    try:
        luku = int(input("anna luku lopeta antamalla tyhjä: "))
        LukuLista.append(luku)
        MuutLista.append(luku)
    except ValueError:
        print(LukuLista)
        print(MuutLista)
