import time
from random import randint


def from_roman_to_decimal(roman: str) -> int:

    translator: dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    cur: int = 0
    nxt: int = 1

    roman_size: int = len(roman)
    decimal: int = translator[roman[cur]]

    # Special case: 1 digit roman number
    if roman_size == 1:
        return decimal

    while (nxt < roman_size):

        if translator[roman[cur]] < translator[roman[nxt]]:
            decimal = decimal - \
                translator[roman[cur]] + \
                (translator[roman[nxt]] - translator[roman[cur]])
        else:
            decimal += translator[roman[nxt]]

        cur += 1
        nxt += 1

    return decimal
