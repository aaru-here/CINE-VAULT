from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.tmdb import search_media, get_trailer
from database.mongo import media_collection


@Client.on_message(filters.command("details"))
async def details(_, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "❌ Usage:\n/details movie name"
        )

    query = " ".join(message.command[1:])

    result = await search_media(query)

    if not result:
        return await message.reply_text(
            "❌ No results found."
        )

    title = result.get("title") or result.get("name")

    overview = result.get("overview", "No description available.")
    rating = result.get("vote_average", "N/A")

    poster = (
        "https://image.tmdb.org/t/p/w500"
        + result["poster_path"]
    )

    # 🔍 user data from DB
    user_data = await media_collection.find_one(
        {
            "user_id": message.from_user.id,
            "title": title
        }
    )

    favorite = "No 🤍"
    status = "Unknown"
    note = "No note."
    rewatch_count = 0

    if user_data:
        favorite = "Yes ❤️" if user_data.get("favorite") else "No 🤍"
        status = user_data.get("status", "Unknown")
        note = user_data.get("note", "No note.")
        rewatch_count = user_data.get("rewatch_count", 0)

    caption = f"""
━━━━━━━━━━━━━━━━━━
🎬 {title}
━━━━━━━━━━━━━━━━━━

⭐ Rating : {rating}

❤️ Favorite : {favorite}
👀 Status : {status}
🔁 Rewatched : {rewatch_count}

📝 Note :

{note}

━━━━━━━━━━━━━━━━━━

📖 Story

{overview}
"""

    # 🎥 REAL TRAILER FETCH
    trailer_url = await get_trailer(title)

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🎥 Trailer",
                    url=trailer_url
                    if trailer_url
                    else f"https://youtube.com/results?search_query={title}+trailer"
                )
            ],
            [
                InlineKeyboardButton("⭐ IMDb", url="https://www.imdb.com"),
                InlineKeyboardButton("📺 TMDb", url="https://www.themoviedb.org")
            ]
        ]
    )

    await message.reply_photo(
        photo=poster,
        caption=caption,
        reply_markup=buttons
    )