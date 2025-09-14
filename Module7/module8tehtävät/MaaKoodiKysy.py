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
maakoodi = input("Anna maakoodi (esim. FI): ")

def haeLentokentatMaasta(maakoodi):
    sql = f'SELECT type, COUNT(*) AS maara FROM airport WHERE iso_country = %s GROUP BY type;'
    kursori = yhteys.cursor()
    kursori.execute(sql, (maakoodi,))
    tulokset = kursori.fetchall()
    if tulokset:
        for tyyppi, maara in tulokset:
            print(f"{tyyppi}: {maara} ")
    else:
        print("Annettu maakoodilla ei löydy mitään")


haeLentokentatMaasta(maakoodi)