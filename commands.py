import discord
import staben
import random


class Help:
    name = "help"
    parameters = "[CMD]"
    description = "Displays all available commands, one of which can be specified."
    usage = """**CMD** - The command you want help with."""

    async def execute(user, channel, parameters):
        if len(parameters) == 0:
            text = ""

            for cmd in cmds.values():
                text += "**{}**".format(cmd.name)
                if len(cmd.parameters) != 0:
                    text += " **{}**".format(cmd.parameters)
                text += " - {}\n".format(cmd.description)

            embed = discord.Embed(title = "Robbe Robot commands", description = text)
            await channel.send(embed=embed)
        elif len(parameters) == 1:
            cmd = cmds.get(parameters[0])
            if cmd != None:
                text = "{}\n\n{}".format(cmd.usage, cmd.description)
                embed = discord.Embed(title = "{} {}".format(cmd.name, cmd.parameters), description = text)
                await channel.send(embed=embed)



class Plans:
    name = "plans" 
    parameters = ""
    description = "Displays what plans exist for this bot"
    usage = ""

    async def execute(user, channel, parameters):
        if len(parameters) == 0:
            plans = """- A poll command, so that users can vote between up to 9 different things.
            - A video command, so that users can show videos in a voice channel.
            - A music command, so that users can play music in a voice channel.
            - A react command, so that users can react in certain ways via custom reaction images.
            - A counter command, so that users can create counters with specific titles. (e.g. Andröv Death counter)
            - A mcdonken command, so that Ronald McDonald can read your soul and decide what you should eat.
            - Better help messages. Describes how to use it and highlights words, etc.
            - An erik command, so that users can PÖHÖHÖHÖ to their hearts content."""
            embed = discord.Embed(title = "Plans for Robbe Robot", description = plans)
            await channel.send(embed=embed)
        else:
            pass


class Staben:
    name = "staben"
    parameters = ""
    description = "Invokes the power of STABEN!"
    usage = ""

    async def execute(user, channel, parameters):
        if len(parameters) == 0:
            quote = staben.get_quote()
            embed = discord.Embed(title = quote)
            await channel.send(embed=embed)
        else:
            pass


class Source:
    name = "source"
    parameters = ""
    description = "Links to the repository of this bot"
    usage = ""

    async def execute(user, channel, parameters):
        if len(parameters) == 0:
            embed = discord.Embed(title = "Robbe Robot's residence", url = "https://github.com/Parslie/robbe-robot", description = "This is where Robbe Robot lives and spends most of his time!")
            await channel.send(embed=embed)
        else:
            pass


class Dice:
    name = "dice"
    parameters = "[SIDES]"
    description = "Rolls a die of variable size."
    usage = "**SIDES** - The amount of sides of the die"

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
