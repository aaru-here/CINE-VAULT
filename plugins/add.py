from pyrogram import Client, filters
from database.mongo import media_collection


async def add_media(message, media_type):

    name = message.text.split(None, 1)

    if len(name) < 2:
        return await message.reply_text(
            f"❌ Usage:\n/{media_type} <name>"
        )

    title = name[1]

    data = {
        "user_id": message.from_user.id,
        "title": title,
        "type": media_type
    }

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

    await media_collection.insert_one(data)

    await message.reply_text(
        f"✅ Successfully added:\n\n🎬 {title}"
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