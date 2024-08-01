import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
import time

class Utilites(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xfd9d63
        
    @nextcord.slash_command(description="Replies with bot latency.")
    async def ping(self, interation: Interaction):
        latency = int(self.bot.latency * 1000)
        await interation.response.send_message(f"Pong! My latency is {latency}ms.")
        
def setup(bot):
    bot.add_cog(Utilites(bot))