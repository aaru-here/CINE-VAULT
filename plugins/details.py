from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from utils.tmdb import search_media


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
            "❌ Not found."
        )

    title = (
        result.get("title")
        or result.get("name")
    )

    overview = result.get(
        "overview",
        "No description."
    )

    rating = result.get(
        "vote_average",
        "N/A"
    )

    poster = (
        "https://image.tmdb.org/t/p/w500"
        + result["poster_path"]
    )

    caption = f"""
━━━━━━━━━━━━━━━━━━
🎬 {title}
━━━━━━━━━━━━━━━━━━

⭐ Rating : {rating}

📖 Story

{overview}
"""

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🎥 Trailer",
                    url="https://youtube.com"
                )
            ]
        ]
    )

    await message.reply_photo(
        poster,
        caption=caption,
        reply_markup=buttons
    )