import discord
from discord import Colour
from commands import cmds

PREFIX = '!'


def process_cmd(cmd: str):
    if ' ' not in cmd:
        return cmd, []
    name, arg_str = cmd.split(None, 1)

    args = []
    new_arg = ''
    is_quote = False
    prev_c = None

    for c in arg_str:
        if c == '"':
            # Toggle quote mode
            if not is_quote and prev_c != ' ' and prev_c != None:
                # Handle starting quotes not being preceded by a space
                return None, 'Non-space character followed up with a start quote!'
            is_quote = not is_quote
        
        elif not is_quote and c != ' ' and prev_c == '"':  
            # Handle ending quotes not followed by a space
            return None, 'End quote followed up with a non-space character!'

        elif not is_quote and c == ' ': 
            # Add previous argument
            if prev_c == ' ':
                # Skip if previous was a space too
                continue
            args.append(new_arg)
            new_arg = ''

        else: 
            # Add character to current argument
            new_arg += c
        
        prev_c = c

    # Handle unended quotes
    if is_quote:
        return None, 'Last quote not ended!'

    # Add last argument
    args.append(new_arg)

    return name, args


class Client(discord.Client):
    async def on_ready(self):
        print(f'Signed in as {self.user}!')

    async def on_message(self, msg: discord.Message):
        if msg.author == self.user:
            return  # Do not respond to self

        if msg.content and msg.content[0] == PREFIX:
            name, args = process_cmd(msg.content[1:])
            
            if name is None:
                embed = discord.Embed(title=f'ERROR: {args}', colour=Colour.red())
                await msg.channel.send(embed=embed)
            else:
                cmd = cmds.get(name, None)
                
                if cmd is None:
                    embed = discord.Embed(title=f'ERROR: the command "{name}" does not exist!', colour=Colour.red())
                    await msg.channel.send(embed=embed)
                else:
                    await cmd.parse_args(args)
                    await cmd.execute(self, msg.channel, msg.author)
