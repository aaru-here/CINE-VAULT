from pyrogram import Client, filters

HELP_TEXT = """
━━━━━━━━━━━━━━━━━━
❖ ᴄɪηєᴠᴧυʟᴛ ʜєʟᴘ ϻєηυ ❖
━━━━━━━━━━━━━━━━━━

🎬 Media Commands

➻ /addmovie
➻ /addseries
➻ /addanime

🔍 Search Commands

➻ /details
➻ /search

📚 Collection Commands

➻ /list
➻ /remove

━━━━━━━━━━━━━━━━━━
"""


@Client.on_message(filters.command("help"))
async def help_cmd(_, message):
    await message.reply_text(HELP_TEXT)