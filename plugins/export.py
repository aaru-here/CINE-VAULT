from pyrogram import Client, filters
from database.mongo import media_collection
import json


@Client.on_message(filters.command("export"))
async def export(_, message):

    user_id = message.from_user.id

    data = []

    async for item in media_collection.find({"user_id": user_id}):
        item.pop("_id", None)
        data.append(item)

    if not data:
        return await message.reply_text("❌ Nothing to export.")

    file_name = f"{user_id}_collection.json"

    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

    await message.reply_document(
        file_name,
        caption="📤 Your collection backup"
    )