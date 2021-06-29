from discord import Embed, Colour
from botutils.constants import DOCS_URL, HONEYSUCKLE_SUPPORT_SERVER_URL, ALL_METADATA_KEYS

def get_help_embed():
    """to return help embed
    """
    embed = Embed(
            title="How to Use Honeysuckle",
            description="Command to link stories from ffnet and ao3",
            color=0xF1948A
        )

    embed.add_field(
        name="Ffnet links:",
        value="`.ff [fic name]` \
        \n **Example:**\n`.ff the lost horcrux`",
        inline=False
    )
    
    embed.add_field(
        name="AO3 links:",
        value="`.ao3 [fic name]` \
        \n **Like:**\n`.ao3 from ruin`",
        inline=False
    )

    return embed

    

def get_about_embed():
    """to return about embed about hs bot
    """
    embed = Embed(
                title="About Honeysuckle v1.1.2",
                description="First built in March 2020 by **inPursuitOfMagic**, this bot aims to \
                            faciliate easy linking of fanfiction stories in discord servers. \
                            \n Since then, it has gotten a few redesigns and a major overhaul in August'20, Jan'21 and recently in June'21. \n\n \
                            To read the full documentation of the bot, please visit: [Documentation.](%s)" % DOCS_URL,
                        color=0xF450AF
            )
    embed.add_field(
        name="Join the bot support server:",
        value=HONEYSUCKLE_SUPPORT_SERVER_URL,
        inline=False
    )

    return embed


def get_embeds(list_of_dicts_of_metadata):
    """
    to get embeds list from list of dicts of story metadata
    """
    embeds_list = []
    for data in list_of_dicts_of_metadata:
        if data == "Not found.":
            continue
        embed = Embed(
            title= data['title'],
            url= data['link'],
            description= data['summary'],
            colour=Colour(0x272b28)
        )
        del data['title']
        del data['link']
        del data['summary']
        for key in data:
            embed.add_field(
            name = key,
            value = data[key], 
            inline=True)
        embeds_list.append(embed)
    
    return embeds_list


