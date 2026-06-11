from pyrogram import Client, filters
from database.mongo import media_collection


@Client.on_message(filters.command("list"))
async def list_media(_, message):

    items = media_collection.find(
        {"user_id": message.from_user.id}
    )

    text = """
━━━━━━━━━━━━━━━━━━
📚 ʏσυʀ ᴄσʟʟєᴄᴛɪση
━━━━━━━━━━━━━━━━━━

"""

    count = 0

    async for item in items:

        count += 1

        media_type = item["type"].capitalize()

        text += (
            f"{count}. 🎬 {item['title']}"
            f" ({media_type})\n"
        )

    if count == 0:
        return await message.reply_text(
            "❌ No items found."
        )

    text += "\n━━━━━━━━━━━━━━━━━━"

    await message.reply_text(text)