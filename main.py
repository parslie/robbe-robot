import discord
import random
import texts

cmd_prefix = "!"

def process_command(message):
    pass

class BotClient(discord.Client):
    async def on_ready(self):
        print("Logged in as", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if len(message.content) > 0 and message.content[0] == cmd_prefix:
            message_split = message.content[1:].split(" ")
            command = message_split[0]
            parameters = message_split[1:]
            await self.on_command(message.author, message.channel, command, parameters)

    async def on_command(self, user, channel, command, parameters):
        if command == "help":
            if len(parameters) == 0:
                help_text = ""

                for cmd,help in texts.help.items():
                    help_text += "**" + cmd + "** - " + help + "\n"

                await self.send_embed(channel, title = "Robbe Robot commands", description = help_text)
            elif len(parameters) == 1:
                await self.send_embed(channel, title = "Help for " + parameters[0], description = texts.help.get(parameters[0]))
        elif command == "plans":
            await self.send_embed(channel, title = "Plans for Robbe Robot", description = texts.plans)

    async def send_embed(self, channel, title=None, description=None):
        embed = discord.Embed(title=title, description=description)
        await channel.send(embed=embed)


client = BotClient()
client.run("ODAyMjQzNzA1NzMzMzgyMTU1.YAsZrA.EiHf5HglwCRB1d1ups7VpZCvizQ")
