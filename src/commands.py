from discord import Colour, Embed, User, TextChannel, Client

cmds = dict()

###############
# Command bases 

class Command:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    async def execute(self, client: Client, channel: TextChannel, user: User, args: list):
        embed = Embed(title=f'ERROR: the command "{self.name}" has not been implemented yet!', colour=Colour.red())
        await channel.send(embed=embed)


def bind_command(cls: Command):
    instance = cls()
    cmds[instance.name] = instance


class ModedCommand(Command):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.modes = dict()

    def bind_mode(self, name, func):
        self.modes[name] = func

    async def execute(self, client: Client, channel: TextChannel, user: User, args: list):
        if not args:
            embed = Embed(title=f'ERROR: you need to specify a mode for the command "{self.name}"!', colour=Colour.red())
            await channel.send(embed=embed)
        else:
            mode = args[0]
            
            if mode not in self.modes.keys():
                embed = Embed(title=f'ERROR: "{mode}" is not a valid mode for the command "{self.name}"!', colour=Colour.red())
                await channel.send(embed=embed)
            else:
                await self.modes[mode](client, channel, user, args[1:])

#####################
# Command definitions

@bind_command
class Help(Command):
    def __init__(self):
        super().__init__('help', 'shows all commands and info about the bot')

    async def execute(self, client: Client, channel: TextChannel, user: User, args: list):
        txt = ''
        for cmd in cmds.values():
            txt += f'**{cmd.name}** - {cmd.description}\n'

        embed = Embed(title='Commands and Info', description=txt, colour=Colour.green())
        await channel.send(embed=embed)

    
@bind_command
class Game(ModedCommand):
    def __init__(self):
        super().__init__('game', 'N/A')
        self.bind_mode('add', self.add)
        self.bind_mode('remove', self.remove)
        self.bind_mode('list', self.list)

    async def add(self, client: Client, channel: TextChannel, user: User, args: list):
        await channel.send(content='add')

    async def remove(self, client: Client, channel: TextChannel, user: User, args: list):
        await channel.send(content='remove')

    async def list(self, client: Client, channel: TextChannel, user: User, args: list):
        await channel.send(content='list')