import discord
from commands import cmds

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

            cmd = cmds.get(command)
            if cmd != None:
                await cmd.execute(message.author, message.channel, parameters)


client = BotClient()
client.run("ODAyMjQzNzA1NzMzMzgyMTU1.YAsZrA.EiHf5HglwCRB1d1ups7VpZCvizQ")
