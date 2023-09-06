import sqlite3 as db
import services
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Roman Translator"


@app.route("/translator/<roman_number>")
def translate(roman_number: str):
    return str(services.from_roman_to_decimal(roman_number))


@app.route("/translator/batch")
def batch_translate():
    romans = request.get_json()["romans"]
    decimals = [services.from_roman_to_decimal(roman) for roman in romans]
    return str(decimals)


@app.route("/database/create/<db_name>")
def create_translation_database(db_name: str):
    with db.connect(db_name + ".db") as conn:
        print(f"{db_name} created.")
        print(db.version)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
