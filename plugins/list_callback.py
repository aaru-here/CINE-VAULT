from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from database.mongo import media_collection
from utils.image_generator import create_collection_image


ITEMS_PER_PAGE = 8


def paginate(items, page):
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    return items[start:end]


@Client.on_callback_query(filters.regex("list_"))
async def list_callback(_, query: CallbackQuery):

    user_id = query.from_user.id
    page = int(query.data.split("_")[1])

    if page < 1:
        return await query.answer("No previous page", show_alert=True)

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

    total_pages = (len(items) // ITEMS_PER_PAGE) + 1

    if page > total_pages:
        return await query.answer("No more pages", show_alert=True)

    page_items = paginate(items, page)

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
                InlineKeyboardButton("⬅️ Previous", callback_data=f"list_{page-1}"),
                InlineKeyboardButton("➡️ Next", callback_data=f"list_{page+1}")
            ]
        ]
    )

    await query.message.edit_media(
        media=InputMediaPhoto(image_path, caption=f"💚 Page {page}/{total_pages}"),
        reply_markup=buttons
    )