import os

import httpx

key = os.environ['wordnik']

async def getWordOfTheDay():
    url = f"https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key={key}"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()

    return data

