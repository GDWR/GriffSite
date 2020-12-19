import httpx


async def getImageOfTheDay():
    url = f"http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()

    return data

