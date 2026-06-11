from pyrogram import Client, filters
from database.mongo import media_collection


@Client.on_message(filters.command("achievements"))
async def achievements(_, message):

    user_id = message.from_user.id

    count = await media_collection.count_documents(
        {"user_id": user_id}
    )

    if count < 10:
        badge = "🌱 Beginner Collector"
    elif count < 100:
        badge = "🎬 Movie Lover"
    elif count < 500:
        badge = "🔥 Master Collector"
    elif count < 1000:
        badge = "👑 Legend Collector"
    else:
        badge = "💎 Cine God"

    await message.reply_text(
        f"""
━━━━━━━━━━━━━━━━━━
🏆 ACHIEVEMENTS
━━━━━━━━━━━━━━━━━━

📚 Total Collection : {count}

🏅 Badge :
{badge}

━━━━━━━━━━━━━━━━━━
"""
    )