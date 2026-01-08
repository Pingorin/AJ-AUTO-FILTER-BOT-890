import random
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

# Bot Client setup
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Replies ki list
responses = [
    "hello", 
    "hello cutie", 
    "Hello Mr", 
    "hello guys", 
    "kaise ho dear"
]

# Message handler
@app.on_message(filters.text & filters.private)
async def reply_handler(client, message):
    # Agar user 'hii' bhejta hai (case insensitive)
    if message.text.lower() == "hii":
        random_reply = random.choice(responses)
        await message.reply_text(random_reply)

print("Bot start ho gaya hai...")
app.run()
