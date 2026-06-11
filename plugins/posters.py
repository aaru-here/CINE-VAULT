from pyrogram import Client, filters
from database.mongo import media_collection
from utils.poster_generator import fetch_posters, create_grid


@Client.on_message(filters.command("posters"))
async def posters(_, message):

    items = []

    async for item in media_collection.find(
        {"user_id": message.from_user.id}
    ):
        items.append(item)

    if not items:
        return await message.reply_text("❌ No collection found.")

    images = await fetch_posters(items)

    if not images:
        return await message.reply_text("❌ Posters not available.")

    file = create_grid(images)

    await message.reply_photo(
        photo=file,
        caption="🖼 Your Movie & Series Collection"
    )