from random import choice
from pyrogram import Client, filters
from database.mongo import media_collection


@Client.on_message(filters.command("random"))
async def random_media(_, message):

    items = []

    async for item in media_collection.find(
        {"user_id": message.from_user.id}
    ):
        items.append(item)

    if not items:
        return await message.reply_text(
            "❌ Your collection is empty."
        )

    selected = choice(items)

    await message.reply_text(
        f"""
🎲 Random Recommendation

🎬 {selected['title']}
📂 {selected['type'].capitalize()}
"""
    )