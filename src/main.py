from bottoken import token
from commands import cmds
import discord
import react

cmd_prefix = "!"


def process_command(unprocessed_cmd):
    cmd = unprocessed_cmd.split()
    cmd_name = cmd[0]
    unprocessed_arguments = cmd[1:]
    print("Processing Command:", cmd_name)
    print("Unprocessed Arguments:", unprocessed_arguments)

    arguments = []
    processed_string = ""
    for argument in unprocessed_arguments:
        if processed_string == "":
            if len(argument) >= 2 and argument[-1] == '"' and argument[0] == '"':
                # Single-worded string
                arguments.append(argument[1:-1])
            elif argument[0] == '"':
                # Beginning of string
                processed_string = argument[1:] + " "
            else:
                # Regular argument
                try:
                    argument = float(argument)
                except:
                    pass  # Argument is not a number
                arguments.append(argument)
        else:
            if argument[-1] == '"':
                # End of string
                processed_string += argument[0:-1]
                arguments.append(processed_string)
                processed_string = ""
            else:
                # Word in middle of string
                processed_string += argument + " "

    print("Processed Arguments:", arguments)
    return cmds.get(cmd_name), arguments


class BotClient(discord.Client):
    async def on_ready(self):
        print("Logged in as", self.user, "\n")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if len(message.content) > 0 and message.content[0] == cmd_prefix:
            cmd, arguments = process_command(message.content[1:])
            if cmd != None:
                await cmd.execute(self, message.author, message.channel, arguments)


if __name__ == "__main__":
    react.init()
    client = BotClient()
    client.run(token)