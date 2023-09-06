import random
import time
import requests
from config import CFG
from helpers import timetracked

NUMBER_OF_REQUESTS = 10
ROMAN_NUMBERS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
BATCH_SIZE = 4

def create_database(db_name: str):
    url = CFG["backend"]["backend_base_url"] + \
        CFG["backend"]["database_endpoint"]+f"/create/{db_name}"
    resp = requests.post(url)

    if resp.status_code == 200:
        return resp.text

    return f"Request failure. HTTP code: {resp.status_code}"


def get_decimal_from_roman(roman: str):
    url = CFG["backend"]["backend_base_url"] + \
        CFG["backend"]["translator_endpoint"]+f"/{roman}"
    resp = requests.get(url)

    if resp.status_code == 200:
        return resp.text

    return f"Request failure. HTTP code: {resp.status_code}"


def get_batch_decimal_from_roman(romans: list[str]):
    url = CFG["backend"]["backend_base_url"] + \
        CFG["backend"]["translator_endpoint"]+f"/batch"
    resp = requests.get(url, json={"romans": romans})

    if resp.status_code == 200:
        return resp.text

    return f"Request failure. HTTP code: {resp.status_code}"


@timetracked
def translate():
    for i in range(NUMBER_OF_REQUESTS):
        roman = random.choice(ROMAN_NUMBERS)
        decimal = get_decimal_from_roman(roman)
        print(f"[T{i}] Roman: {roman} Decimal: {decimal}")


def batch_translate():
    for i in range(NUMBER_OF_REQUESTS):
        romans = random.choices(ROMAN_NUMBERS, k=BATCH_SIZE)
        decimals = get_batch_decimal_from_roman(romans)
        print(f"[T{i}] Roman numbers: {romans} Decimal numbers: {decimals}")


if __name__ == "__main__":
    print("Enter DB name: ")
    db_name = input()
    create_database(db_name)
    translate()
