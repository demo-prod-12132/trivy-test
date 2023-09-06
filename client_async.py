import asyncio
import time
from random import choice

import aiohttp
from config import CFG
from helpers import timetracked

NUMBER_OF_REQUESTS = 10
ROMAN_NUMBERS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]


async def get_decimal_from_roman(session, roman: str):
    url = CFG["backend"]["backend_base_url"] + \
        CFG["backend"]["translator_endpoint"]+f"/{roman}"

    async with session.get(url) as resp:
        decimal = await resp.text()
        return decimal


async def translate():
    async with aiohttp.ClientSession() as session:
        for i in range(NUMBER_OF_REQUESTS):
            roman = choice(ROMAN_NUMBERS)
            decimal = await get_decimal_from_roman(session, roman)
            print(f"[T{i}] Roman: {roman} Decimal: {decimal}")


@timetracked
def run_translation():
    asyncio.run(translate())


if __name__ == "__main__":
    run_translation()
