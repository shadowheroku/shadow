import os

class Config:
    API_ID = int(os.getenv("API_ID", 12345))
    API_HASH = os.getenv("API_HASH", "your_api_hash")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
    OWNER_ID = int(os.getenv("OWNER_ID", 123456789))
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", -1001234567890))
    SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "123456789").split()))
