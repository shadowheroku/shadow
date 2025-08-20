import asyncio
from pyrogram import idle
from mo-main.Powers import telethon_app, pyrogram_app

async def run():
    # Both are already started in __init__.py; just idle on Pyrogram
    print("✅ Telethon and Pyrogram bots initialized")
    await idle()
    await pyrogram_app.stop()
    await telethon_app.disconnect()
