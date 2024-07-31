# bot/intents.py

import nextcord

def get_intents():
    intents = nextcord.Intents.all()
    intents.guilds = True
    intents.members = True
    intents.bans = True
    intents.emojis = True
    intents.integrations = True
    intents.webhooks = True
    intents.invites = True
    intents.voice_states = True
    intents.messages = True
    intents.guild_messages = True
    intents.dm_messages = True
    intents.reactions = True
    intents.guild_reactions = True
    intents.dm_reactions = True
    intents.typing = True
    intents.guild_typing = True
    intents.dm_typing = True
    intents.presences = True
    return intents
