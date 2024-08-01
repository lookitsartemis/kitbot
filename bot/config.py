# bot/config.py

import nextcord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
COGS = ["cogs.utils"]

ACTIVITY = "goober simulator 9000"
STATUS = nextcord.Status.online