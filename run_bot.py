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
from brain import receiver

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



@bot.event
async def on_message(message):
    """ Command to search and find the fanfiction by searching on google
    """
    # To see if commnds need to be executed too
    await bot.process_commands(message)
    
    # get the message 
    msg = message.content.lower()

    # Do not reply to self
    if message.author == bot.user:
        return  
    # Do not reply to any other bot
    if message.author.bot:
        return 

    # see if message has any links or not
    embeds_to_send = receiver.process_message(msg)
    if embeds_to_send:
        async with message.channel.typing():
            for embed in embeds_to_send:
                try:
                    await message.reply(embed=embed, mention_author=False)
                except:
                    await message.reply(embed=embed)
    


# run the bot
loop_bot_status.start()
bot.load_extension("helpercogs.help_cog")
bot.load_extension("helpercogs.gsearch_cog")
bot.run(TOKEN)
