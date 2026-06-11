import aiohttp
from PIL import Image
import io

TMDB_IMAGE = "https://image.tmdb.org/t/p/w500"


async def fetch_posters(items):

    images = []

    async with aiohttp.ClientSession() as session:

        for item in items[:9]:

            if not item.get("poster_path"):
                continue

            url = TMDB_IMAGE + item["poster_path"]

            async with session.get(url) as resp:
                img_data = await resp.read()

            images.append(img_data)

    return images


def create_grid(images):

    canvas = Image.new("RGB", (900, 900), "black")

    size = 300
    x = 0
    y = 0

    for img_bytes in images:

        img = Image.open(io.BytesIO(img_bytes))
        img = img.resize((size, size))

        canvas.paste(img, (x, y))

        x += size
        if x >= 900:
            x = 0
            y += size

    path = "posters.png"
    canvas.save(path)

    return path