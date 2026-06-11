from pyrogram import Client, filters
from datetime import datetime
from database.mongo import media_collection


@Client.on_message(filters.command("monthly"))
async def monthly(_, message):

    user_id = message.from_user.id

    cursor = media_collection.find({"user_id": user_id})

    total = 0
    movies = 0
    series = 0
    anime = 0

    genres = {}

    async for item in cursor:

        total += 1

        if item["type"] == "movie":
            movies += 1
        elif item["type"] == "series":
            series += 1
        elif item["type"] == "anime":
            anime += 1

        g = item.get("genre", "unknown")
        genres[g] = genres.get(g, 0) + 1

    top_genre = max(genres, key=genres.get) if genres else "N/A"

    text = f"""
━━━━━━━━━━━━━━━━━━
📅 MONTHLY RECAP
━━━━━━━━━━━━━━━━━━

📚 Total Added : {total}

🎬 Movies : {movies}
📺 Series : {series}
🌸 Anime : {anime}

🎭 Top Genre : {top_genre}

━━━━━━━━━━━━━━━━━━
💚 Keep building your collection!
"""

    await message.reply_text(text)