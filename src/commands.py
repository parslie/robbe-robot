import discord
import generators

cmds = dict()


class Command():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        cmds[name] = self

    def usage(self):
        return self.name

    def details(self):
        return self.description

    async def send_message(self, channel, title=None, description=None, url=None):
        embed = discord.Embed(title=title, description=description, url=url)
        await channel.send(embed=embed)

    async def execute(self, user, channel, arguments):
        print("Executing Command:", self.name, "({})".format(user.display_name), "\n")


# Random Generators 


class Staben(Command):
    def __init__(self):
       super().__init__("staben", "Invokes the power of STABEN!")
    
    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)

        if len(arguments) > 0: return

        quote = generators.staben()
        await self.send_message(channel, quote, "- STABEN")


class Erik(Command):
    def __init__(self):
       super().__init__("erik", "Tjena, har du tid att snacka eller?")
    
    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)

        if len(arguments) > 0: return

        quote = generators.erik()
        await self.send_message(channel, quote, "- Erik")


class Donken(Command):
    def __init__(self):
       super().__init__("donken", "Reads your soul and decides your next donken meal.")
    
    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)

        if len(arguments) > 0: return

        quote = generators.donken(user.name)
        await self.send_message(channel, quote, "- Ronald McDonald")


class Dice(Command):
    def __init__(self):
       super().__init__("dice", "Generates a random number from 1 to 6 or higher.")

    def usage(self):
        return "{} {}".format(self.name, "[MAX]")

    def details(self):
        return self.description + "\n\n**[MAX]** - The amount of sides the die has. Defaults to 6."

    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)

        if len(arguments) == 0: 
            value = generators.dice(6)
        elif len(arguments) == 1:
            value = generators.dice(arguments[0])
        else:
            return

        await self.send_message(channel, "{} rolled a {}!".format(user.display_name, value))


# Misc


class Plans(Command):
    def __init__(self):
        super().__init__("plans", "Displays the plans for Robbe Robot.")
    
    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)

        if len(arguments) > 0: return

        await self.send_message(channel, "Plans for Robbe Robot", \
            """- A **poll** command, so that users can vote between up to 9 different things.
            - A **video** command, so that users can show videos in a voice channel.
            - A **music** command, so that users can play music in a voice channel.
            - A **react** command, so that users can react in certain ways via custom reaction images.""")


class Help(Command):
    def __init__(self):
        super().__init__("help", "Displays all available commands for Robbe Robot.")

    async def show_all(self, channel):
        text = ""

        for cmd in cmds.values():
            text += "**{}** - {}\n".format(cmd.name, cmd.description)

        await self.send_message(channel, "Robbe Robot commands", text)

    async def show_one(self, channel, cmd_name):
        cmd = cmds.get(cmd_name)
        if cmd != None:
            await self.send_message(channel, cmd.usage(), cmd.details())

    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)
        
        if len(arguments) == 0:
            await self.show_all(channel)
        elif len(arguments) == 1:
            await self.show_one(channel, arguments[0])
        else:
            return


class Counter(Command):
    def __init__(self):
        super().__init__("counter", "Manipulates and displays counter, such as the Andröv Death counter.")


class Source(Command):
    def __init__(self):
        super().__init__("source", "Gives the direction to Robbe Robot's residence.")

    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)

        if len(arguments) > 0: return

        await self.send_message(channel, "Robbe Robot's residence", "This is where Robbe Robot lives and spends most of his time!", "https://github.com/Parslie/robbe-robot")


# Activate Commands


Staben()
Help()
#Counter()
Dice()
Donken()
Erik()
Plans()
Source()