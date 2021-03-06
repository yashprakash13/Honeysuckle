import discord
import os
from dotenv import load_dotenv

load_dotenv()

STATUS_ACTIVITY_DICT = {
    '.helphs' : discord.ActivityType.listening,
    'Love the way you link!' : discord.ActivityType.playing,
    "You wish you had a mind like me, don't you?" : discord.ActivityType.playing, 
    "It's OK. You're only human, after all." : discord.ActivityType.playing
}

DOCS_URL = 'https://github.com/HBEG/Honeysuckle/blob/master/README.md'
HONEYSUCKLE_SUPPORT_SERVER_URL = "https://discord.gg/z87n86uhmy"

FFN_CHECK_STR = 'fanfiction.net/s/'
AO3_CHECK_STR = 'archiveofourown.org/works/'

# HS_API_URL_FFN = "http://localhost:8000/hsapi/ffn"
# HS_API_URL_AO3 = "http://localhost:8000/hsapi/ao3"
HS_API_URL_FFN = os.environ.get("HS_API_URL_FFN")
HS_API_URL_AO3 = os.environ.get("HS_API_URL_AO3")

ALL_METADATA_KEYS = [
    "title",
    "author_name",
    "rated",
    "summary",
    "genres",
    "num_chapters",
    "num_words",
    "status",
    "characters",
    "published",
    "updated",
    "link"
]

IS_URL_REGEX  =  r"(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:/[^\s]*)?"
