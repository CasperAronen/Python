from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='casper',
    password='password',
    autocommit=True,
    collation='utf8mb3_general_ci'
)

@app.route("/", methods=["GET"])
def home():
    return "Morjes! Anna ICAO-koodi URL:iin, esim. /EFHK"

@app.route("/<icao>", methods=["GET"])
def saa_icao(icao):
    if len(icao) != 4:
        return jsonify({"error": f"{icao} ei ole toimiva ICAO-koodi – täsmälleen 4 merkkiä!"}), 400

    kursori = yhteys.cursor()
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao.upper(),))
    rivi = kursori.fetchone()

    if rivi:
        tulos = {
            "icao": icao.upper(),
            "nimi": rivi[0],
            "kunta": rivi[1]
        }
        return jsonify(tulos)
    else:
        return jsonify({"error": f"Koodilla {icao.upper()} ei löytynyt kenttää."}), 404

if __name__ == "__main__":
    app.run(debug=True)
