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
import aiohttp

TMDB_API_KEY = "YOUR_API_KEY"


async def get_trailer(title: str):

    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}"

    async with aiohttp.ClientSession() as session:

        async with session.get(search_url) as resp:
            data = await resp.json()

        if not data.get("results"):
            return None

        movie_id = data["results"][0]["id"]

        video_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={TMDB_API_KEY}"

        async with session.get(video_url) as resp:
            videos = await resp.json()

        for v in videos.get("results", []):
            if v["type"] == "Trailer" and v["site"] == "YouTube":
                return f"https://www.youtube.com/watch?v={v['key']}"

    return None