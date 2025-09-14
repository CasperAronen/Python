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
def hae_lentokentta():
    kursori=yhteys.cursor()
    kursori.execute("SELECT ident, name FROM airport LIMIT 5")

def haeKenttaIdent(ident):
    sql = f"SELECT * FROM airport WHERE ident = '{ident}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    rivi = kursori.fetchall()
    print(rivi)

def muokkaaNimi(uusi_nimi, ident):
    sql = f"UPDATE airport SET name = '{uusi_nimi}' WHERE ident = '{ident}' LIMIT 1"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    if kursori.rowcount == 1:
        print("Ubdate")

muokkaaNimi("00KS", "Kivi")
haeKenttaIdent("00A")