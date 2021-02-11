import discord
import staben
import random

cmds = dict()


class Argument:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.value = None
    
    def set_value(self, arg_list, index, default = None):
        if len(arg_list) > index:
            self.value = arg_list[index]
        else:
            self.value = default
    
    def to_string(self):
        return "**{}** - {}".format(self.name, self.description)


class Command:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
        cmds[self.name] = self
    
    async def execute(self, user, channel, arguments):
        print(self.name, "was executed by", user.display_name)
    
    def get_full_name(self):
        return "**{}**".format(self.name)
    
    def get_full_description(self):
        return self.description + "**(TEMP. DESCRIPTION)**"


class Help(Command):
    def __init__(self):
        super().__init__("help", "Displays all available commands, one of which can be specified.")
        self.cmd_arg = Argument("cmd", "The command to display help for. (optional)") 
    
    def get_full_name(self):
        return "**{} [{}]**".format(self.name, self.cmd_arg.name)
    
    def get_full_description(self):
        return "{}\n\n{}".format(self.cmd_arg.to_string(), self.description)
    
    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)
        self.cmd_arg.set_value(arguments, 0)
        
        if len(arguments) > 1:
            return
        
        if self.cmd_arg.value == None:
            text = ""

            for cmd in cmds.values():
                text += "{} - {}\n".format(cmd.get_full_name(), cmd.description)

            embed = discord.Embed(title = "Robbe Robot commands", description = text)
            await channel.send(embed = embed)
        else:
            cmd = cmds.get(self.cmd_arg.value)
            if cmd != None:
                embed = discord.Embed(title = cmd.get_full_name(), description = cmd.get_full_description())
                await channel.send(embed = embed)


class Plans(Command):
    def __init__(self):
        super().__init__("plans", "Displays the plans for Robbe Robot's future.")
    
    def get_full_name(self):
        return "**{}**".format(self.name)
    
    def get_full_description(self):
        return self.description
    
    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)
        
        if len(arguments) > 0:
            return
        
        plans = """- A poll command, so that users can vote between up to 9 different things.
            - A video command, so that users can show videos in a voice channel.
            - A music command, so that users can play music in a voice channel.
            - A react command, so that users can react in certain ways via custom reaction images.
            - A counter command, so that users can create counters with specific titles. (e.g. Andröv Death counter)
            - A mcdonken command, so that Ronald McDonald can read your soul and decide what you should eat.
            - An erik command, so that users can PÖHÖHÖHÖ to their hearts content.
            - A better command-argument system, to avoid type-convertions."""
        embed = discord.Embed(title = "Plans for Robbe Robot", description = plans)
        await channel.send(embed = embed)


class Dice(Command):
    def __init__(self):
        super().__init__("dice", "Generates a random number from 1-6, unless specified otherwise.")
        self.max_arg = Argument("max", "The max value the generated number can have.")
    
    def get_full_name(self):
        return "**{} [{}]**".format(self.name, self.max_arg.name)

    def get_full_description(self):
        return "{}\n\n{}".format(self.max_arg.to_string(), self.description)
    
    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)
        self.max_arg.set_value(arguments, 0, default = 6)
        
        if len(arguments) > 1:
            return
        
        value = random.randint(1, int(self.max_arg.value)) # TODO: add exception-handling
        embed = discord.Embed(title = "{} rolled a {}!".format(user.display_name, value))
        await channel.send(embed = embed)


class Staben(Command):
    def __init__(self):
        super().__init__("staben", "Invokes the power of STABEN!")
    
    def get_full_name(self):
        return "**{}**".format(self.name)
    
    def get_full_description(self):
        return self.description
    
    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)
        
        if len(arguments) > 0:
            return
        
        embed = discord.Embed(title = staben.get_quote())
        await channel.send(embed = embed)


class Source(Command):
    def __init__(self):
        super().__init__("source", "Links to the repository where this bot resides.")
    
    def get_full_name(self):
        return "**{}**".format(self.name)
    
    def get_full_description(self):
        return self.description
    
    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)
        
        if len(arguments) > 0:
            return
        
        embed = discord.Embed(title = "Robbe Robot's residence", url = "https://github.com/Parslie/robbe-robot", description = "This is where Robbe Robot lives and spends most of his time!")
        await channel.send(embed = embed)


Help()
Plans()
Dice()
Staben()
Source()