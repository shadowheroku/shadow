from telethon import TelegramClient
from pyrogram import Client
from .config import Config

# Telethon client (mo-main backbone)
telethon_app = TelegramClient("telethon_bot", Config.API_ID, Config.API_HASH)
telethon_app = telethon_app.start(bot_token=Config.BOT_TOKEN)

# Pyrogram client (music features)
pyrogram_app = Client(
    "pyrogram_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)
