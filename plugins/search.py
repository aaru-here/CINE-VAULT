from pyrogram import Client, filters
from utils.tmdb import search_media


@Client.on_message(filters.command("search"))
async def search_cmd(_, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "❌ Usage:\n/search movie name"
        )

    query = " ".join(message.command[1:])

    result = await search_media(query)

    if not result:
        return await message.reply_text(
            "❌ No results found."
        )

    title = (
        result.get("title")
        or result.get("name")
    )

    await message.reply_text(
        f"🎬 Result Found:\n\n{title}"
    )