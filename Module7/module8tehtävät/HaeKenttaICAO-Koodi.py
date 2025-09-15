import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='casper',
         password='password',
         autocommit=True,
         collation='utf8mb3_general_ci',
         )
koodi = input("Hae lentokentta ja siejantikunta icao koodilla: ").upper()
def haeKenttaIdent(koodi):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{koodi}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    rivi = kursori.fetchone()
    if rivi:
        print(f"Lentokentän nimi: {rivi[0]}")
        print(f"Sijaintikunta: {rivi[1]}")
    else:
        print("Kenttää ei löytynyt")
haeKenttaIdent(koodi)