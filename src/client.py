import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Signed in as {self.user}!')