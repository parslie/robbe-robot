import discord
import staben
import random


class Help:
    name = "help"
    detailed_name = "help [cmd]"
    desc = "Displays available commands"
    detailed_desc = "Displays available commands, one of which can be specified"

    async def execute(user, channel, parameters):
        if len(parameters) == 0:
            text = ""
            for cmd in cmds.values():
                text += "**{}** - {}\n".format(cmd.detailed_name, cmd.desc)
            
            embed = discord.Embed(title = "Robbe Robot commands", description = text)
            await channel.send(embed=embed)
        elif len(parameters) == 1:
            cmd = cmds.get(parameters[0])
            embed = discord.Embed(title = "Help for {}".format(cmd.name), description = cmd.detailed_desc)
            await channel.send(embed=embed)
        else:
            pass


class Plans:
    name = "plans"
    detailed_name = "plans"
    desc = "Displays what plans exist for this bot"
    detailed_desc = "Displays what plans exist for this bot"

    async def execute(user, channel, parameters):
        if len(parameters) == 0:
            plans = """- A poll command, so that users can vote between up to 9 different things.
            - A video command, so that users can show videos in a voice channel.
            - A music command, so that users can play music in a voice channel.
            - A react command, so that users can react in certain ways via custom reaction images.
            - A counter command, so that users can create counters with specific titles. (e.g. Andröv Death counter)
            - A mcdonken command, so that Ronald McDonald can read your soul and decide what you should eat."""
            embed = discord.Embed(title = "Plans for Robbe Robot", description = plans)
            await channel.send(embed=embed)
        else:
            pass


class Staben:
    name = "staben"
    detailed_name = "staben"
    desc = "Invokes the power of STABEN!"
    detailed_desc = "Invokeds the power of STABEN... in the form of quotes!"

    async def execute(user, channel, parameters):
        if len(parameters) == 0:
            quote = staben.get_quote()
            embed = discord.Embed(title = quote)
            await channel.send(embed=embed)
        else:
            pass


class Source:
    name = "source"
    detailed_name = "source"
    desc = "Links to the repository of this bot"
    detailed_desc = "Links to the repository where Robbe Robot lives"

    async def execute(user, channel, parameters):
        if len(parameters) == 0:
            embed = discord.Embed(title = "Robbe Robot's residence", url = "https://github.com/Parslie/robbe-robot", description = "This is where Robbe Robot lives and spends most of his time!")
            await channel.send(embed=embed)
        else:
            pass


class Dice:
    name = "dice"
    detailed_name = "dice (SIZE)"
    desc = "Rolls a dice of variable size"
    detailed_desc = "Rolls a dice of variable size. If a size is not specified, it will default to a six-sided die"

    async def execute(user, channel, parameters):
        sides = 6

        if len(parameters) == 1:
            sides = int(parameters[0]) # TODO: add exception-handling
        if len(parameters) <= 1:
            value = random.randint(1, sides)
            embed = discord.Embed(title = "Robbe rolled a {}".format(value)) # TODO: replace with user name
            await channel.send(embed=embed)


cmds = {Help.name: Help,
        Plans.name: Plans,
        Staben.name: Staben,
        Source.name: Source,
        Dice.name: Dice}
