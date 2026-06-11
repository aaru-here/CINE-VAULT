from pyrogram import Client, filters
from database.mongo import media_collection
from random import choice


@Client.on_message(filters.command("recommend"))
async def recommend(_, message):

    items = []

    async for item in media_collection.find(
        {"user_id": message.from_user.id}
    ):
        items.append(item)

    if not items:
        return await message.reply_text("❌ No data found.")

    selected = choice(items)

    await message.reply_text(
        f"""
🤖 Recommendation for you

🎬 {selected['title']}
🎭 Genre : {selected.get('genre', 'unknown')}
📂 Type : {selected['type']}
"""
    )