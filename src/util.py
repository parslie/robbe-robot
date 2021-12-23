from os import name
from discord import *

async def send_success(channel: TextChannel, title: str, description: str = ''):
    embed = Embed(title=title, description=description, colour=Colour.green())
    await channel.send(embed=embed)

async def send_warning(channel: TextChannel, title: str, description: str = ''):
    embed = Embed(title=title, description=description, colour=Colour.orange())
    await channel.send(embed=embed)

async def send_error(channel: TextChannel, title: str, description: str = ''):
    embed = Embed(title=title, description=description, colour=Colour.red())
    await channel.send(embed=embed)