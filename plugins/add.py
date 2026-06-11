from pyrogram import Client, filters
from database.mongo import media_collection


async def add_media(message, media_type):

    if len(message.command) < 2:
        return await message.reply_text(
            f"❌ Usage:\n/add{media_type} title | genre (optional)"
        )

    parts = message.text.split(" ", 2)

    title = parts[1]
    genre = parts[2].lower() if len(parts) > 2 else "unknown"

    already = await media_collection.find_one(
        {
            "user_id": message.from_user.id,
            "title": title
        }
    )

    if already:
        return await message.reply_text(
            "⚠️ Already exists in your collection."
        )

    data = {
        "user_id": message.from_user.id,
        "title": title,
        "type": media_type,
        "genre": genre,

        "favorite": False,
        "note": "",
        "status": "Plan To Watch",
        "rewatch_count": 0
    }

    await media_collection.insert_one(data)

    await message.reply_text(
        f"""
✅ Added Successfully

🎬 Title : {title}
🎭 Genre : {genre}
📂 Type : {media_type}
"""
    )


@Client.on_message(filters.command("addmovie"))
async def add_movie(_, message):
    await add_media(message, "movie")


@Client.on_message(filters.command("addseries"))
async def add_series(_, message):
    await add_media(message, "series")


@Client.on_message(filters.command("addanime"))
async def add_anime(_, message):
    await add_media(message, "anime")