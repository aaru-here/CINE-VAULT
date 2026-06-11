from pyrogram import Client, filters
from database.mongo import media_collection


@Client.on_message(filters.command("rewatch"))
async def rewatch(_, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "❌ Usage:\n/rewatch title"
        )

    title = " ".join(message.command[1:])

    result = await media_collection.update_one(
        {
            "user_id": message.from_user.id,
            "title": title
        },
        {
            "$inc": {
                "rewatch_count": 1
            }
        }
    )

    if result.modified_count == 0:
        return await message.reply_text(
            "❌ Item not found."
        )

    await message.reply_text(
        f"🔁 Rewatch count increased\n\n🎬 {title}"
    )