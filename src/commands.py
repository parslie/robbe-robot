from discord import Colour, Embed, colour

cmds = dict()

###############
# Command bases 

class Command:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    async def parse_args(self, args):
        pass

    async def execute(self, client, channel, user):
        embed = Embed(title=f'ERROR: the command "{self.name}" has not been implemented yet!', colour=Colour.red())
        await channel.send(embed=embed)


def bind_command(cls: Command):
    instance = cls()
    cmds[instance.name] = instance

#####################
# Command definitions

@bind_command
class Test(Command):
    def __init__(self):
        super().__init__('test', 'test description')


@bind_command
class Help(Command):
    def __init__(self):
        super().__init__('help', 'shows all commands and info about the bot')

    async def execute(self, client, channel, user):
        txt = ''
        for cmd in cmds.values():
            txt += f'**{cmd.name}** - {cmd.description}\n'

        embed = Embed(title='Commands and Info', description=txt, colour=Colour.green())
        await channel.send(embed=embed)