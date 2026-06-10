from pyrogram import Client
from pyrogram.types import Message
import os

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]

app = Client(
    "musicbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def start(_, message: Message):
    if message.text == "/start":
        await message.reply("✅ Music Bot Online")

app.run()
