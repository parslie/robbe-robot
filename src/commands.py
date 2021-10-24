from discord import Colour, Embed, User, TextChannel, Client, colour

cmds = dict()

###############
# Command bases 

class Command:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    async def execute(self, client: Client, channel: TextChannel, user: User, args: list[str]):
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

    async def execute(self, client: Client, channel: TextChannel, user: User, args: list[str]):
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

    async def execute(self, client: Client, channel: TextChannel, user: User, args: list[str]):
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
        self.bind_mode('call', self.call)
        self.bind_mode('list', self.list)

        self.games = dict()
        # TODO: load in saved games dictionary

    async def add(self, client: Client, channel: TextChannel, user: User, args: list[str]):
        if len(args) != 2:
            embed = Embed('ERROR: the mode "add" needs exactly 2 arguments!', colour=Colour.red())
            await channel.send(embed=embed)

        else:  # Add user to game list
            game = args[0]
            user_to_add = args[1]
            game_list = self.games.get(game, [])

            if user_to_add not in game_list:
                game_list.append(user_to_add)
                self.games[game] = game_list

    async def remove(self, client: Client, channel: TextChannel, user: User, args: list[str]):
        if len(args) != 2:
            embed = Embed('ERROR: the mode "remove" needs exactly 2 arguments!', colour=Colour.red())
            await channel.send(embed=embed)

        else:  # Remove user from game list
            game = args[0]
            user_to_rem = args[1]
            game_list = self.games.get(game, [])

            if user_to_rem in game_list:
                game_list.remove(user_to_rem)
                self.games[game] = game_list

    async def call(self, client: Client, channel: TextChannel, user: User, args: list[str]):
        if len(args) != 1:
            embed = Embed('ERROR: the mode "call" needs exactly 1 arguments!', colour=Colour.red())
            await channel.send(embed=embed)
        
        else:  # Call for all epic gamers to game
            game = args[0]
            game_list = self.games.get(game, [])

            if game_list:
                txt = f'Calling all epic gamers to play **{game}**!\n'
                for user_to_call in game_list:
                    txt += f'{user_to_call} '

                await channel.send(content=txt)

    async def list(self, client: Client, channel: TextChannel, user: User, args: list[str]):
        if len(args) != 0:
            embed = Embed('ERROR: the mode "list" needs exactly 0 arguments!', colour=Colour.red())
            await channel.send(embed=embed)

        else:  # Print all game lists
            txt = ''
            for game, game_list in self.games.items():
                txt += f'**{game}** - '
                for user_to_list in game_list:
                    txt += f'{user_to_list} '
                txt += '\n'

            embed = Embed(title='Game Lists', description=txt, colour=Colour.green())
            await channel.send(embed=embed)
