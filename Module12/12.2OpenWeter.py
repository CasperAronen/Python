import requests
def hae_saa(paikkakunta, api_avain):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_avain}&units=metric&lang=fi"
    vastaus = requests.get(url)

    if vastaus.status_code == 200:
        data = vastaus.json()
        lampotila = data["main"]["temp"]
        kuvaus = data["weather"][0]["description"]
        print(f"Sää {kuvaus} Lämpötila: {lampotila:.1f} °C")
    else:
        print("Paikakuntaa ei ole")


def main():
    api_avain = "d30584acdebabbaac4f71f647db7a77e"
    paikkakunta = input("Anna paikkakunnan nimi: ")
    hae_saa(paikkakunta, api_avain)


main()
