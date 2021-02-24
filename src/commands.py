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

    async def send_message(self, channel, title=None, description=None):
        embed = discord.Embed(title=title, description=description)
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
       super().__init__("donken", "asdasdsdfdsafler?")
    
    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)

        if len(arguments) > 0: return

        quote = generators.donken(user.name)
        await self.send_message(channel, quote, "- Ronald McDonald")


class Dice(Command):
    def __init__(self):
       super().__init__("dice", "Asdfasdf att snacka eller?")

    def usage(self):
        return "{} **{}**".format(self.name, "[MAX]")

    def details(self):
        return self.description + "\n\n[MAX] - The amount of sides the die has. Defaults to 6."

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
    pass


class Help(Command):
    pass


class Counter(Command):
    pass


class Source(Command):
    pass


# Activate Commands


Staben()
#Help()
#Counter()
Dice()
Donken()
Erik()
#Source()