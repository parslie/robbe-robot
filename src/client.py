import discord
from discord import colour

PREFIX = '!'

class Client(discord.Client):
    async def on_ready(self):
        print(f'Signed in as {self.user}!')

    async def on_message(self, msg: discord.Message):
        if msg.author == self.user:
            return  # Do not respond to self

        if msg.content and msg.content[0] == PREFIX:
            await msg.channel.send(content=f'{msg.author} sent "{msg.content}"')
            embed = discord.Embed(title='Title', description='Description')
            await msg.channel.send(embed=embed)