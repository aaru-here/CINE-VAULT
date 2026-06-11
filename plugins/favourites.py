from pyrogram import Client, filters
from database.mongo import media_collection


@Client.on_message(filters.command("favorites"))
async def favorites(_, message):

    items = media_collection.find(
        {
            "user_id": message.from_user.id,
            "favorite": True
        }
    )

    text = """
━━━━━━━━━━━━━━━━━━
❤️ Favorite Collection
━━━━━━━━━━━━━━━━━━

"""

    count = 0

    async for item in items:

        count += 1

        text += f"{count}. 🎬 {item['title']}\n"

    if count == 0:
        return await message.reply_text(
            "❌ No favorites found."
        )

    await message.reply_text(text)