tunnus = "python"
salasana = "rules"
yritys = 0
Tarvaus = input("Anna käyttäjätunnus: ")
Sarvaus =  input("Anna salasana: ")

while yritys <4:
    if Sarvaus != salasana and Tarvaus != tunnus:
        yritys +=1
        print("Käyttäjätunnus tai salana on väärin")
        Tarvaus = input("Anna käyttäjätunnus: ")
        Sarvaus = input("Anna salasana: ")
    else:
        print("Tervetuloa")
        break
print("Pääsy kielletty")

