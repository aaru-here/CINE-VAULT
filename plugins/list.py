from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.mongo import media_collection
from utils.image_generator import create_collection_image

ITEMS_PER_PAGE = 8


def paginate_items(items, page):

    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE

    return items[start:end]


@Client.on_message(filters.command("list"))
async def list_media(_, message):

    user_id = message.from_user.id

    page = 1

    if len(message.command) > 1:
        try:
            page = int(message.command[1])
        except:
            page = 1

    cursor = media_collection.find({"user_id": user_id})

    items = []
    movies = 0
    series = 0
    anime = 0
    favorites = 0

    async for item in cursor:

        items.append(item)

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

    total_pages = (len(items) // ITEMS_PER_PAGE) + 1

    page_items = paginate_items(items, page)

    titles = [f"🎬 {i['title']}" for i in page_items]

    image_path = create_collection_image(
        movies,
        series,
        anime,
        favorites,
        titles,
        page
    )

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "⬅️ Previous",
                    callback_data=f"list_{page-1}"
                ),
                InlineKeyboardButton(
                    "➡️ Next",
                    callback_data=f"list_{page+1}"
                )
            ]
        ]
    )

    await message.reply_photo(
        photo=image_path,
        caption=f"💚 Page {page}/{total_pages}",
        reply_markup=buttons
    )