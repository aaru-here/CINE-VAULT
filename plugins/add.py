from pyrogram import Client, filters
from database.mongo import media_collection


async def add_media(message, media_type):

    if len(message.command) < 2:
        return await message.reply_text(
            f"❌ Usage:\n/add{media_type} title"
        )

    title = " ".join(message.command[1:])

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
        "favorite": False,
        "note": "",
        "status": "Plan To Watch",
        "rewatch_count": 0
    }

    await media_collection.insert_one(data)

    await message.reply_text(
        f"✅ Added Successfully\n\n🎬 {title}"
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