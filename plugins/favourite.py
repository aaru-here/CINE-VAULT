from pyrogram import Client, filters
from database.mongo import media_collection


@Client.on_message(filters.command("favorite"))
async def favorite(_, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "❌ Usage:\n/favorite title"
        )

    title = " ".join(message.command[1:])

    result = await media_collection.update_one(
        {
            "user_id": message.from_user.id,
            "title": title
        },
        {
            "$set": {
                "favorite": True
            }
        }
    )

    if result.modified_count == 0:
        return await message.reply_text(
            "❌ Item not found."
        )

    await message.reply_text(
        f"❤️ Added to favorites\n\n🎬 {title}"
    )