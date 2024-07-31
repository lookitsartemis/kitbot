# bot/main.py

import nextcord
from nextcord.ext import commands
import config
from intents import get_intents

intents = get_intents()

bot = commands.Bot(
    intents=intents,
    status=config.STATUS,
    activity=nextcord.Game(name=config.ACTIVITY)
)

for cog in config.COGS:
    bot.load_extension(cog)

@bot.event
async def on_ready():
    print()
    print(f"Logged in as {bot.user} - [{bot.application_id}].")
    print()

bot.run(config.TOKEN)
