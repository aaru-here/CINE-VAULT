from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_TEXT = """
─────────────────────────
│ 🎬 ᴡєʟᴄσϻє ᴛσ ˹˹ ᴄɪηєᴠᴧυʟᴛ ˼˼ │
─────────────────────────

❖ ʏσυʀ ᴘєʀsσηᴧʟ ϻσᴠɪє ᴧηᴅ sєʀɪєs ϻᴧηᴧɢєʀ ❖

╭⎋ 🎥 ϻσᴠɪєs
├⊚ 📺 sєʀɪєs
├⊚ 🌸 ᴧηɪϻє
╰⊚ ❤️ ғᴧᴠσʀɪᴛєs

─────────────────────────
❍ ᴘσᴡєʀєᴅ ʙʏ » ˹ ᴄɪηєᴠᴧυʟᴛ ˼
─────────────────────────
"""


@Client.on_message(filters.command("start"))
async def start(_, message):

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🎬 Movies", callback_data="movies"),
                InlineKeyboardButton("📺 Series", callback_data="series")
            ],
            [
                InlineKeyboardButton("🌸 Anime", callback_data="anime"),
                InlineKeyboardButton("❓ Help", callback_data="help")
            ]
        ]
    )

    await message.reply_text(
        START_TEXT,
        reply_markup=buttons
    )