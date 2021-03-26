import discord
import generators
import counter
import quote
import meme

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

    async def execute(self, client, user, channel, arguments):
        print("Executing Command:", self.name, "({})".format(user.display_name), "\n")


# Random Generators 


class Donken(Command):
    def __init__(self):
       super().__init__("donken", "Reads your soul and decides your next donken meal.")

    def details(self):
        return "{} Your soul's wants change roughly once per hour.".format(self.description)

    async def execute(self, client, user, channel, arguments):
        await super().execute(client, user, channel, arguments)

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

    async def execute(self, client, user, channel, arguments):
        await super().execute(client, user, channel, arguments)

        if len(arguments) == 0: 
            value = generators.dice(6)
        elif len(arguments) == 1:
            value = generators.dice(arguments[0])
        else:
            return

        await self.send_message(channel, "{} rolled a {}!".format(user.display_name, value))


class Meme(Command):
    def __init__(self):
        super().__init__("meme", "Sends epic memes, like a boss!")

    def usage(self):
        return f"{self.name} [TYPE] (add)"

    def details(self):
        details = f"{self.description} You can add relevant new memes, like rage comics and the trollface, by writing 'add' at the end.\n\n"

        meme_types = meme.get_types()
        if len(meme_types) != 0:
            details += "Available meme types: "
            for meme_type in meme_types:
                details += f"**{meme_type}**, "
            details = details[:-2]
        else:
            details += "There are currently now memes... **forever alone**"

        return details

    async def add(self, client, user, channel, meme_type, check, timeout):
        try:
            msg = await client.wait_for("message", check=check, timeout=timeout)
            attachment = msg.attachments[0]
            attachment_bytes = await attachment.read()
            meme.add(meme_type, attachment.filename, attachment_bytes)
            await self.send_message(channel, "Successfully added meme!", f"You can add another one within {timeout} seconds...")
            await self.add(client, user, channel, meme_type, check, timeout)
        except:
            await self.send_message(channel, f"Done waiting on {user.display_name} for memes!")

    async def execute(self, client, user, channel, arguments):
        await super().execute(client, user, channel, arguments)

        def check(msg):
            return msg.channel == channel and msg.author == user and len(msg.attachments) == 1

        if len(arguments) == 1:
            meme_type = arguments[0]
            meme_img = meme.get(meme_type)
            if meme_img != None:
                await channel.send(file=meme_img)
            else:
                await self.send_message(channel, "There's no memes of that type!")
        elif len(arguments) == 2 and arguments[1] == "add":
            meme_type = arguments[0]
            timeout = 16
            await self.send_message(channel, "Waiting for a meme...", f"This will timeout in {timeout} seconds")
            await self.add(client, user, channel, meme_type, check, timeout)


class TTS(Command):
    def __init__(self):
       super().__init__("tts", "Translate swedish to tts-understable text.")

    def details(self):
        return f"{self.description} Gives Robbe Robot the ability to speak. Finally!"
    
    async def execute(self, client, user, channel, arguments):
        await super().execute(client, user, channel, arguments)

        if len(arguments) != 1: return

        to_translate = arguments[0]
        translated = generators.tts(to_translate)
        await channel.send(translated, tts=True)


class Quote(Command):
    def __init__(self):
        super().__init__("quote", "Generates a random quote from a given set.")

    def usage(self):
        return f"{self.name} [MODE] [ARGs...]"

    def details(self):
        return f"""{self.description} New quotes or sets can be added.
        
            **[MODE]** - **add, remove,** or **list**
            **[ARGs...]** - different for each mode

            **[ARGs...]** for **add** mode are **[SET] [QUOTE]**.
            **[ARGs...]** for **remove** mode are **[SET] [INDEX]**
            **[ARGs...]** for **list** modes is **[SET]**
            
            **[SET]** - The name of a set to act upon.
            **[INDEX]** - The index of the quote to act upon.
            **[QUOTE]** -  The quote to add."""
            
    async def add(self, channel, arguments):
        pass
            
    async def remove(self, channel, arguments):
        pass

    async def list(self, channel, arguments):
        pass
    
    async def show(self, channel, set_id):
        pass

    async def execute(self, client, user, channel, arguments):
        await super().execute(client, user, channel, arguments)

        if len(arguments) < 1: return

        mode = arguments[0]
        if mode == "add":
            await self.add(channel, arguments)
        elif mode == "remove":
            await self.remove(channel, arguments)
        elif mode == "list":
            await self.list(channel, arguments)
        else:
            await self.show(channel, mode)


# Voice Channel Commands


class Play(Command):
    def __init__(self):
        super().__init__("play", "Plays a video in the voice channel you're in.")
        self.queue = []

    def usage(self):
        return f"{self.name} [URL]"

    def details(self):
        return f"""{self.description}
        
        **[URL]** - The URL to the YouTube video you want to play."""

    async def execute(self, client, user, channel, arguments):
        super().execute(client, user, channel, arguments)

        if len(arguments) != 1: return

        #url = arguments[0]
        

# Misc


class Plans(Command):
    def __init__(self):
        super().__init__("plans", "Displays the plans for Robbe Robot.")
    
    async def execute(self, client, user, channel, arguments):
        await super().execute(client, user, channel, arguments)

        if len(arguments) > 0: return

        await self.send_message(channel, "Plans for Robbe Robot", \
            """- A **poll** command, so that users can vote between up to 9 different things.
            - A **video** command, so that users can show videos in a voice channel.
            - A **music** command, so that users can play music in a voice channel.""")


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

    async def execute(self, client, user, channel, arguments):
        await super().execute(client, user, channel, arguments)
        
        if len(arguments) == 0:
            await self.show_all(channel)
        elif len(arguments) == 1:
            await self.show_one(channel, arguments[0])
        else:
            return


class Counter(Command):
    def __init__(self):
        super().__init__("counter", "Manipulates and displays counter, such as the Andröv Death counter.")

    def usage(self):
        return "{} {} {}".format(self.name, "[MODE]", "[ARGs...]")

    def details(self):
        return f"""{self.description}
            
            **[MODE]** - **create, delete, increment, decrement, list,** or **show**
            **[ARGs...]** - different for each mode

            **[ARGs...]** for **list** mode does not exist.
            **[ARGs...]** for **create** mode are **[ID] [TITLE]**
            **[ARGs...]** for **all other** modes is **[ID]**
            
            **[ID]** - The ID for the counter to act upon.
            **[TITLE]** -  The name for the counter."""

    async def create(self, channel, arguments):
        if len(arguments) > 3: return
        counter_id = arguments[1]
        counter_title = arguments[2]

        if counter.create(counter_id, counter_title):
            await self.send_message(channel, "'{}' was created!".format(counter_title))
        else:
            await self.send_message(channel, "A counter with ID '{}' already exists!".format(counter_id))

    async def delete(self, channel, arguments):
        if len(arguments) > 2: return
        counter_id = arguments[1]
        counter_title = counter.get_title(counter_id)

        if counter.delete(counter_id):
            await self.send_message(channel, "'{}' was deleted!".format(counter_title))
        else:
            await self.send_message(channel, "A counter with ID '{}' does not exist!".format(counter_id))

    async def list(self, channel):
        await self.send_message(channel, "Counter IDs", counter.to_string())

    async def increment(self, channel, arguments):
        if len(arguments) > 2: return
        counter_id = arguments[1]

        if counter.increment(counter_id):
            counter_title = counter.get_title(counter_id)
            counter_value = counter.get_value(counter_id)
            await self.send_message(channel, "'{}' was incremented to {}!".format(counter_title, counter_value))
        else:
            await self.send_message(channel, "A counter with ID '{}' does not exist!".format(counter_id))

    async def decrement(self, channel, arguments):
        if len(arguments) > 2: return
        counter_id = arguments[1]

        if counter.decrement(counter_id):
            counter_title = counter.get_title(counter_id)
            counter_value = counter.get_value(counter_id)
            await self.send_message(channel, "'{}' was decremented to {}!".format(counter_title, counter_value))
        else:
            await self.send_message(channel, "A counter with ID '{}' does not exist!".format(counter_id))

    async def show(self, channel, arguments):
        counter_id = arguments[0]

        counter_title = counter.get_title(counter_id)
        counter_value = counter.get_value(counter_id)
        if counter_title != None:
            await self.send_message(channel, "{}: {}".format(counter_title, counter_value))
        else:
            await self.send_message(channel, "A counter with ID '{}' does not exist!".format(counter_id))

    async def execute(self, client, user, channel, arguments):
        await super().execute(client, user, channel, arguments)

        if len(arguments) < 1: return

        mode = arguments[0]
        if mode == "create":
            await self.create(channel, arguments)
        elif mode == "delete":
            await self.delete(channel, arguments)
        elif mode == "list":
            await self.list(channel)
        elif mode == "increment":
            await self.increment(channel, arguments)
        elif mode == "decrement":
            await self.decrement(channel, arguments)
        elif mode == "show":
            await self.show(channel, arguments)


class Source(Command):
    def __init__(self):
        super().__init__("source", "Gives the direction to Robbe Robot's residence.")

    async def execute(self, client, user, channel, arguments):
        await super().execute(client, user, channel, arguments)

        if len(arguments) > 0: return

        await self.send_message(channel, "Robbe Robot's residence", "This is where Robbe Robot lives and spends most of his time!", "https://github.com/Parslie/robbe-robot")


# Activate Commands


Help()
Counter()
Dice()
Donken()
Meme()
Plans()
#Play()
Quote()
Source()
TTS()
