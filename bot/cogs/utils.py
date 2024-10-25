import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
import time

class Utilites(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xfd9d63
        self.start_time = time.time()   
        
    @nextcord.slash_command(description="Replies with bot info")
    async def bot(self, interaction: Interaction):
        
        embed = nextcord.Embed(title=" ", color=self.color, description="Goobism is love, Goobism is life.")
        
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Utilites(bot))