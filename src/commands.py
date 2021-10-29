from discord import *
from typing import List
import random
import util
import data

cmds = dict()

###############
# Command bases 

class Command:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def help(self) -> str:
        return 'N/A'

    async def execute(self, client: Client, channel: TextChannel, author: User, args: List[str]):
        await util.send_error(channel, f'The command **{self.name}** has not been implemented yet')


def bind_command(cls: Command):
    instance = cls()
    cmds[instance.name] = instance
    return cls


class ModedCommand(Command):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.modes = dict()

    def bind_mode(self, name, func):
        self.modes[name] = func

    async def execute(self, client: Client, channel: TextChannel, author: User, args: List[str]):
        if not args:
            await util.send_error(channel, f'You need to specify a mode for the command "{self.name}"')
        else:
            mode = args[0]
            
            if mode not in self.modes.keys():
                await util.send_error(channel, f'**{mode}** is not a valid mode for the command **{self.name}**')
            else:
                await self.modes[mode](client, channel, author, args[1:])

#####################
# Command definitions

@bind_command
class Help(Command):
    def __init__(self):
        super().__init__('help', 'shows all commands and info about the bot')

    def help(self) -> str:
        return '''
                Shows all commands and info about the bot. Can also show info about a specific command.
                Usage: **help [cmd]**
               '''

    async def execute(self, client: Client, channel: TextChannel, author: User, args: List[str]):
        if len(args) == 1:
            cmd_name = args[0]
            cmd = cmds.get(cmd_name)

            if cmd is None:
                await util.send_warning(channel, f'The command **{cmd_name}** does not exist!')
            else:
                await util.send_success(channel, f'Help for **{cmd_name}**', cmd.help())
        elif len(args) == 0:
            txt = ''
            for cmd in cmds.values():
                txt += f'**{cmd.name}** - {cmd.description}\n'

            embed = Embed(title='Commands and Info', description=txt, colour=Colour.green())
            await channel.send(embed=embed)
        else:
            await util.send_error(channel, f'The command **{self.name}** needs only 0 or 1 argument')

@bind_command
class Game(ModedCommand):
    def __init__(self):
        super().__init__('game', 'manages gamers and their associated games')
        self.bind_mode('add', self.add)
        self.bind_mode('remove', self.remove)
        self.bind_mode('call', self.call)
        self.bind_mode('list', self.list)

        self.games = data.load('data/game.json')

    def help(self) -> str:
        return '''
                Manages gamers and their associated games. Can be used to call everyone associated with a specific game to play.
                Usage: **game [mode]**
                Modes: **add**, **remove**, **list** and **call**

                **Add mode**:
                Associates a user with a specific game. The user is specified using their @. Multiple users can be specified at once.
                Usage: **game add [game] [user...]**
                Example: **game add minecraft @Parsie**

                **Remove mode**:
                Deassociates a user with a specific game. The user is specified using their @. Multiple users can be specified at once.
                Usage: **game remove [game] [user...]**
                Example: **game remove minecraft @Parsie**

                **List mode**:
                Lists all games and their associated gamers.
                Usage: **game list**

                **Call mode**:
                Calls all gamers associated with the specified game to play.
                Usage: **game add [game]**
                Example: **game call minecraft**
               '''

    async def add(self, client: Client, channel: TextChannel, author: User, args: List[str]):
        if len(args) < 2:
            await util.send_error(channel, 'The mode **add** needs at least 2 arguments')

        else:  # Add user to game list # TODO: add safety check to see if the users are actually users
            game = args[0]
            game_list = self.games.get(game, [])
            users = [x for x in args[1:] if x not in game_list]

            if users:  # Add all users to game list
                txt = ''
                for user in users:
                    game_list.append(user)
                    txt += f'{user} '
                self.games[game] = game_list

                data.save(self.games, 'data/game.json')
                await util.send_success(channel, f'Added users to **{game}**:', txt)

            else:  # Warn about already included users
                await util.send_warning(channel, f'All of the specified users were already in **{game}**!')

    async def remove(self, client: Client, channel: TextChannel, author: User, args: List[str]):
        if len(args) < 2:
            await util.send_error(channel, 'The mode **remove** needs at least 2 arguments')

        else:  # Remove user from game list
            game = args[0]
            game_list = self.games.get(game, [])
            users = [x for x in args[1:] if x in game_list]

            if users:  # Remove all users from game list
                txt = ''
                for user in users:
                    game_list.remove(user)
                    txt += f'{user} '

                if game_list:  # Remove game if no users are in list
                    self.games[game] = game_list
                else:
                    self.games.pop(game)

                data.save(self.games, 'data/game.json')
                await util.send_success(channel, f'Removed users from **{game}**:', txt)

            else:  # Warn about already excluded users
                await util.send_warning(channel, f'None of the specified users were in **{game}**!')

    async def call(self, client: Client, channel: TextChannel, author: User, args: List[str]):
        if len(args) != 1:
            await util.send_error(channel, 'The mode **call** needs exactly 1 arguments')
        
        else:  # Call for all epic gamers to game
            game = args[0]
            game_list = self.games.get(game, [])

            if game_list:
                txt = f'Calling all epic gamers to play **{game}**!\n'
                for user in game_list:
                    txt += f'{user} '
                await channel.send(content=txt)

            else:
                await util.send_warning(channel, f'No users have been added to **{game}**!')

    async def list(self, client: Client, channel: TextChannel, author: User, args: List[str]):
        if len(args) != 0:
            await util.send_error(channel, 'The mode **list** needs exactly 0 arguments')

        elif not self.games:  # Print warning for empty games list
            await util.send_warning(channel, 'There are no games to list!')

        else:  # Print all game lists
            txt = ''
            for game, game_list in self.games.items():
                txt += f'**{game}** - '
                for user in game_list:
                    txt += f'{user} '
                txt += '\n'
            await util.send_success(channel, 'Game Lists', txt)

@bind_command
class Quote(ModedCommand):
    def __init__(self):
        super().__init__('quote', 'categorizes and prints out quotes')
        self.bind_mode('add', self.add)
        self.bind_mode('remove', self.remove)
        self.bind_mode('print', self.print)
        self.bind_mode('list', self.list)

        self.quotes = data.load('data/quotes.json')

    def help(self):
        return '''
                Categorizes and prints out quotes.
                Usage: **quote [mode]**
                Modes: **add**, **remove**, **print** and **list**

                **Add mode:**
                Add a quote of a specific type. Multiple quotes can be added at once.
                Usage: **quote add [type] [quote...]**
                Example: **quote add staben "STABEN kan häfva en tsunami"**

                **Remove mode:**
                Remove a quote of a specific type. Multiple quotes can be removed at once.
                Usage: **quote remove [type] [index...]**
                Example: **quote remove staben 0**
                WARNING: **REMOVING A STABEN QUOTE IS SACRILEGE, AND WILL RESULT IN SEVERE PUNISHMENT**
                
                **Print mode:**
                Prints a random quote of a specific type.
                Usage: **quote print [type]**
                Example: **quote print staben**
                
                **List mode:**
                Lists all existing quote types or all quotes of a specific type.
                Usage: **quote list [type]**
                Example: **quote list**
                Example: **quote list staben**
               '''

    async def add(self, client: Client, channel: TextChannel, author: User, args: List[str]):
        if len(args) < 2:
            await util.send_error(channel, 'The mode **add** needs at least 2 arguments')

        # Add all specified quotes
        else:
            quote_type = args[0]
            new_quotes = args[1:]

            quotes = self.quotes.get(quote_type, [])
            for new_quote in new_quotes:
                quotes.append(new_quote)
            self.quotes[quote_type] = quotes

            await util.send_success(channel, f'Added **{len(new_quotes)}** new quotes of type **{quote_type}**')
            data.save(self.quotes, 'data/quotes.json')

    async def remove(self, client: Client, channel: TextChannel, author: User, args: List[str]):
        if len(args) < 2:
            await util.send_error(channel, 'The mode **remove** needs at least 2 arguments')

        # Remove all specified quotes
        else:
            quote_type = args[0]
            quote_indices = args[1:]
            quotes = self.quotes.get(quote_type, [])
            has_invalid_index = False

            # Check for invalid indices
            for i, quote_index in enumerate(quote_indices):
                if not quote_index.isnumeric() or int(quote_index) >= len(quotes):
                    has_invalid_index = True
                    break
                else:
                    quote_indices[i] = int(quote_index)

            # Remove all indices from quote list
            if not has_invalid_index:
                quote_indices.sort(reverse=True)  # Makes it remove indices from back to front
                for quote_index in quote_indices:
                    quotes.pop(quote_index)
                self.quotes[quote_type] = quotes

                await util.send_success(channel, f'Removed **{len(quote_indices)}** quote(s) of type **{quote_type}**')
                data.save(self.quotes, 'data/quotes.json')

            # Warn against invalid indices
            else:
                quotes = self.quotes.get(quote_type, [])
                await util.send_warning(channel, f'There are only **{len(quotes)}** quote(s) of type **{quote_type}**', 'You might have entered and out-of-range or non-integer index.')

    async def print(self, client: Client, channel: TextChannel, author: User, args: List[str]):
        if len(args) != 1:
            await util.send_error(channel, 'The mode **print** needs exactly 1 argument')

        # Print a random quote of a specific type
        else:
            quote_type = args[0]
            quotes = self.quotes.get(quote_type, [])

            # Warn against empty quote type
            if not quotes:
                await util.send_warning(channel, f'There are no quotes of type **{quote_type}**')

            # Get and print a random quote
            else:
                quote = random.choice(quotes)
                await util.send_success(channel, quote, f'- {quote_type}')

    async def list(self, client: Client, channel: TextChannel, author: User, args: List[str]):
        if len(args) > 1:
            await util.send_error(channel, 'The mode **list** needs 0 or 1 argument')

        # List all quotes of a specific type
        elif args:
            quote_type = args[0]
            quotes = self.quotes.get(quote_type, [])

            # Warn against empty quote type
            if not quotes:
                await util.send_warning(channel, f'There are no quotes of type **{quote_type}**')

            # Print all quotes of type
            else:
                txt = ''
                for i, quote in enumerate(quotes):
                    txt += f'**{i}:** "{quote}"\n'
                await util.send_success(channel, f'**{quote_type}** Quotes', txt)


        # List all quote types
        else: 
            txt = ''
            found_quotes = False

            # Get non-empty quote types
            for key, item in self.quotes.items():
                if item:
                    found_quotes = True
                    txt += f'**{key}** (has **{len(item)}** quotes)\n'

            # Warn against empty quote types
            if not found_quotes:
                await util.send_warning(channel, 'There are no quotes')

            # Print non-empty quote types
            else:
                await util.send_success(channel, 'Quote types', txt)
