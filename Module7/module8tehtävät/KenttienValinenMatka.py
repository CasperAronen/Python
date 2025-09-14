import mysql.connector
from geopy.distance import geodesic
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='casper',
         password='password',
         autocommit=True,
         collation='utf8mb3_general_ci',
         )
maakoodi = input("Anna maakoodi (esim. FI): ")
maakoodi2 = input("Anna maakoodi (esim. FI): ")



def hae_koordinaatit(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    rivi = kursori.fetchone()
    return rivi if rivi else None

def laske_etaisyys(maakoodi, maakoodi2):
    koord1 = hae_koordinaatit(maakoodi)
    koord2 = hae_koordinaatit(maakoodi2)

    if not koord1 or not koord2:
        print("Toista ICAO-koodia ei löytynyt tietokannasta.")
        return

    etaisyys = geodesic(koord1, koord2).kilometers
    print(f"Lentokenttien {maakoodi} ja {maakoodi2} välinen etäisyys on {etaisyys:.2f} km")


laske_etaisyys(maakoodi, maakoodi2)