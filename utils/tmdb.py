import aiohttp
from config import TMDB_API_KEY

BASE_URL = "https://api.themoviedb.org/3"


async def search_media(query):

    url = (
        f"{BASE_URL}/search/multi"
        f"?api_key={TMDB_API_KEY}"
        f"&query={query}"
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            data = await response.json()

            results = data.get("results")

            if not results:
                return None

            return results[0]