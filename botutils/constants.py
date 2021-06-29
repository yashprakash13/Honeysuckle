import discord

STATUS_ACTIVITY_DICT = {
    '.helphs' : discord.ActivityType.listening,
    'Love the way you link!' : discord.ActivityType.playing,
    "You wish you had a mind like me, don't you?" : discord.ActivityType.playing, 
    "It's OK. You're only human, after all." : discord.ActivityType.playing
}

DOCS_URL = 'https://github.com/yashprakash13/Honeysuckle/blob/master/README.md'
HONEYSUCKLE_SUPPORT_SERVER_URL = "https://discord.gg/B5mXWhfzg8"

FFN_CHECK_STR = 'fanfiction.net/s/'
AO3_CHECK_STR = 'archiveofourown.org/works/'

HS_API_URL_FFN = "http://localhost:8000/hsapi/ffn"
HS_API_URL_AO3 = "http://localhost:8000/hsapi/ao3"

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