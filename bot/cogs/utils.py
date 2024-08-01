import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
import datetime

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xfd9d63
        self.start_time = datetime.datetime.now(datetime.timezone.utc)


    # Stats command 
    @nextcord.slash_command(description="Replies with bot stats.")
    async def stats(self, interaction: nextcord.Interaction):
        
        total_users = sum(guild.member_count for guild in self.bot.guilds)
        latency = int(self.bot.latency * 1000)
        
        now = datetime.datetime.now(datetime.timezone.utc)
        uptime_duration = now - self.start_time
        uptime_seconds = int(uptime_duration.total_seconds())
        
        days, remainder = divmod(uptime_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        uptime_str = f"{days}d {hours}h {minutes}m {seconds}s"
        
        embed = nextcord.Embed(title="Stats", color=self.color)
        embed.add_field(name="Name", value=self.bot.user.mention, inline=False)
        embed.add_field(name="ID", value=self.bot.user.id, inline=False)
        embed.add_field(name="Ping", value=f"{latency}ms", inline=False)
        embed.add_field(name="Uptime", value=uptime_str, inline=False)
        embed.add_field(name="Total Users", value=total_users, inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar)
                
        await interaction.response.send_message(embed=embed)
        
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

    # User command
    @nextcord.slash_command(description="Gets user information.")
    async def user(self, interaction: Interaction, member: Member = None):
        
        if member is None:
            
            member = interaction.user
            
        mention = member.mention
        id = member.id
        creation = f"<t:{int(member.created_at.timestamp())}:R>"
        join_date = f"<t:{int(member.joined_at.timestamp())}:R>"
        roles = ", ".join([role.mention for role in member.roles[1:]])
        top_role = member.top_role.mention
        status = member.status
        
        avatar = member.avatar.url
        
        embed = nextcord.Embed(
            title="User",
            color=self.color
        )
        embed.add_field(
            name="Name",
            value=mention
        )
        embed.add_field(
            name="ID",
            value=id
        )
        embed.add_field(
            name="Creation",
            value=creation
        )
        embed.add_field(
            name="Joined",
            value=join_date
        )
        embed.add_field(
            name="Top Role",
            value=top_role
        )
        embed.add_field(
            name="Status",
            value=status
        )
        embed.add_field(
            name="Roles",
            value=roles
        )
        embed.set_thumbnail(url=avatar)
        
        await interaction.response.send_message(embed=embed)
    
    # Avatar command
    @nextcord.slash_command(description="Gets user's avatar.")
    async def avatar(self, interaction: Interaction, member: Member = None):
        
        if member is None:
            
            member = interaction.user
        
        user = member.name    
        avatar = member.avatar.url
        
        embed = nextcord.Embed(
            title=f"@{user}'s Avatar",
            color=self.color
        )
        embed.set_image(url=avatar)
        
        await interaction.response.send_message(embed=embed)
        

def setup(bot):
    bot.add_cog(Utilities(bot))
