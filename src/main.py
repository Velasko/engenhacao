import os
from telethon import TelegramClient, events

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
bot_token = os.getenv('bot_token')

with TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token) as bot:

    @bot.on(events.NewMessage(pattern=r'/ping', from_users=(180673062,)))
    async def ping(event):
        await event.reply("pong")

    @bot.on(events.ChatAction)
    async def chat_action(event):
        if event.user_joined:
            await event.reply(file="/var/engenhacao/welcome-to-hell.mp4")

   bot.run_until_disconnected()
