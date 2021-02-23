import discord
import quotes
import random
import counter

cmds = dict()


# TODO: remove Argument class, handle arguments directly in command classes
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
        print("Executing command:", self.name, "({})".format(user.display_name))
    
    def get_full_name(self):
        return "**{}**".format(self.name)
    
    def get_full_description(self):
        return self.description + "** (TEMPORARY DESCRIPTION)**"


###################
# Template Commands


class QuoteCommand(Command):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.prev_generated_index = -1
    
    def generate_from(self, collection):
        generated_index = self.prev_generated_index

        # TODO: make handle collections of size <= 1
        while generated_index == self.prev_generated_index:
            generated_index = random.randrange(len(collection))

        self.prev_generated_index = generated_index
        return collection[generated_index]


####################
# Generator Commands


class Staben(QuoteCommand):
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
        
        embed = discord.Embed(title = self.generate_from(quotes.staben), description = "- STABEN")
        await channel.send(embed = embed)


class Erik(QuoteCommand):
    def __init__(self):
        super().__init__("erik", "PÖHÖHÖHÖ, vad är en pekare?")
    
    def get_full_name(self):
        return "**{}**".format(self.name)
    
    def get_full_description(self):
        return self.description
    
    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)
        
        if len(arguments) > 0:
            return
        
        embed = discord.Embed(title = self.generate_from(quotes.erik), description = "- Erik")
        await channel.send(embed = embed)


class Dice(Command):
    def __init__(self):
        super().__init__("dice", "Generates a random number from 1-6, unless specified otherwise.")
        self.min_arg = Argument("min", "The minimum value the generated number can have.")
        self.max_arg = Argument("max", "The maximum value the generated number can have.")
    
    def get_full_name(self):
        return "**{} [{}] [{}]**".format(self.name, self.min_arg.name, self.max_arg.name)

    def get_full_description(self):
        return "{}\n{}\n\n{}".format(self.min_arg.to_string(), self.max_arg.to_string(), self.description)
    
    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)
        self.min_arg.set_value(arguments, 0, default = 1)
        self.max_arg.set_value(arguments, 1, default = 6)
        
        if len(arguments) > 2 and not isinstance(self.min_arg.value, (int, float)) and not isinstance(self.max_arg.value, (int, float)):
            return
        
        generated_value = random.randint(self.min_arg.value, self.max_arg.value)
        embed = discord.Embed(title = "{} rolled a {}!".format(user.display_name, generated_value))
        await channel.send(embed = embed)


#################
# Misc Commands


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
            - A mcdonken command, so that Ronald McDonald can read your soul and decide what you should eat.
            - A better counter command, that is more intuitive."""
        embed = discord.Embed(title = "Plans for Robbe Robot", description = plans)
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


class Counter(Command):
    def __init__(self):
        super().__init__("counter", "Manages counters created by the users.")
        self.mode_arg = Argument("mode", "What to do with the list. (e.g: create, delete, increment, decrement, list)")
        self.list_arg = Argument("list", "The ID of the list to use.")
        self.title_arg = Argument("name", "The name of the list to create. (only for create)")
    
    def get_full_name(self):
        return "**{} [{}] [{}] [{}]**".format(self.name, self.mode_arg.name, self.list_arg.name, self.title_arg.name)
    
    def get_full_description(self):
        return "{}\n\n{}\n{}\n{}".format(self.description, self.mode_arg.to_string(), self.list_arg.to_string(), self.title_arg.to_string())
    
    async def execute(self, user, channel, arguments):
        await super().execute(user, channel, arguments)
        self.mode_arg.set_value(arguments, 0)
        self.list_arg.set_value(arguments, 1)
        self.title_arg.set_value(arguments, 2)
        
        # TODO: create better validation checks
        if self.mode_arg.value == None:
            return
        
        # TODO: create better system for modes
        if self.mode_arg.value == "create" and self.title_arg.value != None:
            counter.create(self.list_arg.value, self.title_arg.value)
            embed = discord.Embed(title = "{} was created!".format(self.title_arg.value))
            await channel.send(embed = embed)
        elif self.mode_arg.value == "delete" and self.title_arg.value == None:
            title = counter.get_title(self.list_arg.value)
            counter.delete(self.list_arg.value)
            embed = discord.Embed(title = "{} was deleted!".format(title))
            await channel.send(embed = embed)
        elif self.mode_arg.value == "increment" and self.title_arg.value == None:
            counter.increment(self.list_arg.value)
            title = counter.get_title(self.list_arg.value)
            value = counter.get_value(self.list_arg.value)
            embed = discord.Embed(title = "{} was incremented to {}!".format(title, value))
            await channel.send(embed = embed)
        elif self.mode_arg.value == "decrement" and self.title_arg.value == None:
            counter.decrement(self.list_arg.value)
            title = counter.get_title(self.list_arg.value)
            value = counter.get_value(self.list_arg.value)
            embed = discord.Embed(title = "{} was decremented to {}!".format(title, value))
            await channel.send(embed = embed)
        elif self.mode_arg.value == "list" and self.title_arg.value == None:
            if self.list_arg.value == None:
                text = counter.to_string()
                embed = discord.Embed(title = "Counter IDs", description = text)
                await channel.send(embed = embed)
            else:
                title = counter.get_title(self.list_arg.value)
                value = counter.get_value(self.list_arg.value)
                embed = discord.Embed(title = "{}: {}".format(title, value))
                await channel.send(embed = embed)


Staben() # Högst upp. Viktigtast, ju.
Help()
Counter()
Dice()
Erik()
Plans()
Source()