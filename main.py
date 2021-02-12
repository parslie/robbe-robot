import discord
from commands import cmds
from bottoken import token

cmd_prefix = "!"


def process_command(unprocessed_cmd):
    cmd = unprocessed_cmd.split()
    cmd_name = cmd[0]
    unprocessed_parameters = cmd[1:]

    # TODO: add more error-free string processing
    parameters = []
    processed_string = ""
    for parameter in unprocessed_parameters:
        if processed_string != "" and parameter[-1] == '"':
            processed_string += parameter[0:-1]
            parameters.append(processed_string)
            processed_string = ""
        elif processed_string != "":
            processed_string += parameter + " "
        elif parameter[0] == '"':
            processed_string = parameter[1:] + " "
        else:
            parameters.append(parameter)

    return cmds.get(cmd_name), parameters


class BotClient(discord.Client):
    async def on_ready(self):
        print("Logged in as", self.user, "\n")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if len(message.content) > 0 and message.content[0] == cmd_prefix:
            cmd, parameters = process_command(message.content[1:])
            if cmd != None:
                await cmd.execute(message.author, message.channel, parameters)


client = BotClient()
client.run(token)
