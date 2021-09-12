import discord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'mom':
            await message.channel.send('HAHAHAHA YOUR MOM HAS A MASSIVE WILLY')
        if message.content == 'ping':
            await message.channel.send('PING PONG MOTHERFUCKER')


client = MyClient()
client.run(token)
