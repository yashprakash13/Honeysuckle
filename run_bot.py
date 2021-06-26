import discord
from discord.utils import get
from discord.ext.commands import Bot
import re
from bs4 import BeautifulSoup
import requests
import os
import time
import asyncio
from datetime import datetime
from dateutil.relativedelta import relativedelta
from discord import Embed, Colour
from discord.ext import commands, tasks
from dotenv import load_dotenv
from itertools import cycle

from botutils.constants import *

load_dotenv()  

TOKEN = os.environ.get('DISCORD_TOKEN')

bot = Bot(command_prefix='.')



STATUSES = cycle(STATUS_ACTIVITY_DICT.keys())
ACTIVITIES = cycle(STATUS_ACTIVITY_DICT.values())

@tasks.loop(seconds=1)
async def loop_bot_status():
    """
    Loop through all statuses for the bot every 13 sec
    """

    await bot.wait_until_ready()

    await bot.change_presence(
        activity=discord.Activity(
            type=next(ACTIVITIES),
            name=(next(STATUSES)).strip()
        )
    )

    await asyncio.sleep(13)


loop_bot_status.start()
bot.run(TOKEN)
