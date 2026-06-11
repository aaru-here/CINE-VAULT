from pyrogram import Client, filters
from database.mongo import media_collection


@Client.on_message(filters.command("note"))
async def note(_, message):

    if len(message.command) < 3:
        return await message.reply_text(
            "❌ Usage:\n/note title your note"
        )

    title = message.command[1]
    note_text = " ".join(message.command[2:])

    result = await media_collection.update_one(
        {
            "user_id": message.from_user.id,
            "title": title
        },
        {
            "$set": {
                "note": note_text
            }
        }
    )

    if result.modified_count == 0:
        return await message.reply_text(
            "❌ Item not found."
        )

    await message.reply_text(
        "📝 Note saved successfully."
    )