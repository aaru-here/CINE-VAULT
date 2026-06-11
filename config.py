from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("YOUR_API_ID"))
API_HASH = getenv("YOUR_API_HASH")

BOT_TOKEN = getenv("YOUR_BOT_TOKEN")

MONGO_URI = getenv("YOUR_MONGO_URI")

TMDB_API_KEY = getenv("408ea9fa3a07ca9e4b51b390c17c7de8")

OWNER_ID = int(getenv("8789995472"))