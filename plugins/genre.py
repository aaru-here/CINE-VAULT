from pyrogram import Client, filters
from database.mongo import media_collection


@Client.on_message(filters.command("genre"))
async def genre(_, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "❌ Usage:\n/genre Sci-Fi"
        )

    genre = " ".join(message.command[1:]).lower()

    cursor = media_collection.find(
        {
            "user_id": message.from_user.id,
            "genre": genre
        }
    )

    items = []

    async for item in cursor:
        items.append(item["title"])

    if not items:
        return await message.reply_text(
            f"❌ No items found in {genre} genre."
        )

    text = f"""
━━━━━━━━━━━━━━━━━━
🎭 {genre.upper()} COLLECTION
━━━━━━━━━━━━━━━━━━

"""

    for i, title in enumerate(items, 1):
        text += f"{i}. 🎬 {title}\n"

    await message.reply_text(text)