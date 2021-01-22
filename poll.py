import discord

class Poll():
    def __init__(self, options):
        self.options = options
        self.emojis = ["🔴","🟠","🟡","🟢","🔵","🟣","🟤","⚫","⚪"]
        
    async def send_message(self, channel):
        message = ""
        
        for i in range(len(self.options)):
            message += self.emojis[i] + " - " + self.options[i] + "\n"
           
        embed = discord.Embed(description=message)
        self.message = await channel.send(embed=embed)
    
    async def add_reactions(self):
        if not self.message:
            return

        for i in range(len(self.options)):
            await self.message.add_reaction(self.emojis[i])
