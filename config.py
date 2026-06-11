from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("YOUR_API_ID"))
API_HASH = getenv("YOUR_API_HASH")

BOT_TOKEN = getenv("7846024262:AAHIfNat1VoAELqJ8Vz3ELsl_GPA_HzCDsI")

MONGO_URI = getenv("mongodb+srv://preetiguptaa067_db_user:preetiguptaa067_db_user@cluster0.36ux9u2.mongodb.net/?appName=Cluster0")

TMDB_API_KEY = getenv("408ea9fa3a07ca9e4b51b390c17c7de8")

OWNER_ID = int(getenv("8789995472"))