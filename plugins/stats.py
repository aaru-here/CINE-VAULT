from pyrogram import Client, filters
from database.mongo import media_collection


@Client.on_message(filters.command("stats"))
async def stats(_, message):

    movies = await media_collection.count_documents(
        {
            "user_id": message.from_user.id,
            "type": "movie"
        }
    )

    series = await media_collection.count_documents(
        {
            "user_id": message.from_user.id,
            "type": "series"
        }
    )

    anime = await media_collection.count_documents(
        {
            "user_id": message.from_user.id,
            "type": "anime"
        }
    )

    favorites = await media_collection.count_documents(
        {
            "user_id": message.from_user.id,
            "favorite": True
        }
    )

    total = movies + series + anime

    await message.reply_text(
        f"""
━━━━━━━━━━━━━━━━━━
📊 Collection Stats
━━━━━━━━━━━━━━━━━━

🎬 Movies : {movies}

📺 Series : {series}

🌸 Anime : {anime}

❤️ Favorites : {favorites}

📚 Total : {total}
━━━━━━━━━━━━━━━━━━
"""
    )