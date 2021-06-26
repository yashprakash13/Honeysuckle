import discord
from discord.utils import get
from discord.ext.commands import Bot
import re
from bs4 import BeautifulSoup
import requests
import os
import cloudscraper
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
from discord import Embed, Colour
from dotenv import load_dotenv

load_dotenv()  

