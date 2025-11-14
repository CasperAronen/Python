from flask import Flask, request
import math
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Morjes annappa numero!"

@app.route("/<int:number>", methods=["GET"])
def numero(number):
    if number <= 1:
        return f"{number} ei ole alkuluku!"

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return f"{number} ei ole alkuluku"

    return f"{number} on alkuluku"

if __name__ == "__main__":
    app.run(debug=True)
