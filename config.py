from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("YOUR_API_ID"))
API_HASH = getenv("YOUR_API_HASH")

BOT_TOKEN = getenv("YOUR_BOT_TOKEN")

MONGO_URI = getenv("YOUR_MONGO_URI")

TMDB_API_KEY = getenv("YOUR_TMDB_API_KEY")

OWNER_ID = int(getenv("OWNER_ID"))