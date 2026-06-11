from pyrogram import Client, filters
from database.mongo import media_collection


@Client.on_message(filters.command("remove"))
async def remove_media(_, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "❌ Usage:\n/remove movie name"
        )

    title = " ".join(message.command[1:])

    result = await media_collection.delete_one(
        {
            "user_id": message.from_user.id,
            "title": title
        }
    )

    if result.deleted_count == 0:
        return await message.reply_text(
            "❌ Item not found."
        )

    await message.reply_text(
        f"✅ Removed:\n\n🎬 {title}"
    )