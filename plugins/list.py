from pyrogram import Client, filters
from database.mongo import media_collection
from utils.image_generator import create_collection_image


@Client.on_message(filters.command("list"))
async def list_media(_, message):

    user_id = message.from_user.id

    items_cursor = media_collection.find({"user_id": user_id})

    items = []
    movies = 0
    series = 0
    anime = 0
    favorites = 0

    async for item in items_cursor:

        items.append(item["title"])

        if item["type"] == "movie":
            movies += 1
        elif item["type"] == "series":
            series += 1
        elif item["type"] == "anime":
            anime += 1

        if item.get("favorite"):
            favorites += 1

    if not items:
        return await message.reply_text("❌ Your collection is empty.")

    # last 8 items show karenge image me
    recent_items = items[-8:]

    image_path = create_collection_image(
        movies=movies,
        series=series,
        anime=anime,
        favorites=favorites,
        items=recent_items,
        page=1
    )

    await message.reply_photo(
        photo=image_path,
        caption="💚 Your CineVault Collection"
    )