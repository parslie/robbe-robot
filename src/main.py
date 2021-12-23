import os
from client import BotClient

if __name__ == '__main__':
    token = os.getenv('DISCORD_TOKEN')

    if token is None:
        print('ERROR: You have to set DISCORD_TOKEN in your environment variables!')
        quit(1)

    print('Signing in bot...')
    client = BotClient()
    client.run(token)