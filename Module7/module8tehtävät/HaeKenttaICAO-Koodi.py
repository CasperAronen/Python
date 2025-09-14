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
koodi = input("Hae lentokentta ja siejantikunta icao koodilla: ")
def haeKenttaIdent(koodi):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{koodi}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    rivi = kursori.fetchone()
    if rivi:
        print(rivi)
    else:
        print("Kenttää ei löytynyt")
haeKenttaIdent(koodi)