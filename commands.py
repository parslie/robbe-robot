import discord
import staben


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
            - A source code command, that links to the repository where Robbe Robot lives.
            - A dice command, so that users can get a random number.
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


class Echo:
    name = "echo"
    detailed_name = "echo (text)"
    desc = "Echos what you specify"
    detailed_desc = "Echos what you specify"

    async def execute(user, channel, parameters):
        if len(parameters) == 1:
            embed = discord.Embed(title = parameters[0])
            await channel.send(embed=embed)
        else:
            pass


cmds = {Help.name: Help,
        Plans.name: Plans,
        Staben.name: Staben,
        Echo.name: Echo}
