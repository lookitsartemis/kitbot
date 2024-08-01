import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xfd9d63

    # Ping command 
    @nextcord.slash_command(description="Replies with bot latency.")
    async def ping(self, interaction: Interaction):
        latency = int(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! My latency is {latency}ms.")
        
    # Server command
    @nextcord.slash_command(description="Gets server information.")
    async def server(self, interaction: Interaction):
        server = interaction.guild
        name = server.name
        member_count = server.member_count
        owner = server.owner.mention
        icon = server.icon.url if server.icon else None
        text_channels = len(server.text_channels)
        voice_channels = len(server.voice_channels)
        roles = len(server.roles)
        creation_timestamp = f"<t:{int(server.created_at.timestamp())}>"
        boost_level = server.premium_tier
        number_of_boosts = server.premium_subscription_count

        embed = nextcord.Embed(
            title="Server Information",
            color=self.color
        )
        embed.add_field(
            name="Name",
            value=name,
            inline=True
        )
        embed.add_field(
            name="Owner",
            value=owner,
            inline=True
        )
        embed.add_field(
            name="Members",
            value=member_count,
            inline=True
        )
        embed.add_field(
            name="Creation Date",
            value=creation_timestamp,
            inline=True
        )
        embed.add_field(
            name="Boost Level",
            value=boost_level,
            inline=True
        )
        embed.add_field(
            name="Number of Boosts",
            value=number_of_boosts,
            inline=True
        )
        embed.add_field(
            name="Text Channels",
            value=text_channels,
            inline=True
        )
        embed.add_field(
            name="Voice Channels",
            value=voice_channels,
            inline=True
        )
        embed.add_field(
            name="Roles",
            value=roles,
            inline=True
        )
        if icon:
            embed.set_thumbnail(url=icon)

        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Utilities(bot))
