from pyrogram import Client, filters
from database.mongo import media_collection


@Client.on_message(filters.command("status"))
async def status(_, message):

    if len(message.command) < 3:
        return await message.reply_text(
            "❌ Usage:\n/status title Completed"
        )

    title = message.command[1]
    status_text = " ".join(message.command[2:])

    result = await media_collection.update_one(
        {
            "user_id": message.from_user.id,
            "title": title
        },
        {
            "$set": {
                "status": status_text
            }
        }
    )

    if result.modified_count == 0:
        return await message.reply_text(
            "❌ Item not found."
        )

    await message.reply_text(
        "👀 Status updated."
    )