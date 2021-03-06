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
        name="Simply linking of stories",
        value="Just mention any FFN or AO3 story link in your message to get the bot's response.",
        inline=False
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
    """to return about embed about hs bot from ffn
    """
    embed = Embed(
                title="About Honeysuckle v1.1.2",
                description="First built in March 2020 by **inPursuitOfMagic**, this bot aims to \
                            faciliate easy linking of fanfiction stories in discord servers. \
                            \n Since then, it has gotten a few redesigns and a major overhaul in August'20, Jan'21 and recently in June'21. \n\n",
                        color=0xF450AF
            )
    embed.add_field(
        name="The Honeysuckle bot is now part of the HBEG fanfiction project. Join our support community here:",
        value=HONEYSUCKLE_SUPPORT_SERVER_URL,
        inline=False
    )

    return embed


def get_embeds_ffn(list_of_dicts_of_metadata):
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
        embed.set_author(name=data['author_name'])

        # add fields one by one
        if data['status'] == 'Complete':
            embed.add_field(
            name = 'Status',
            value = data['status'], 
            inline=True)
        else:
            embed.add_field(
            name = 'Last Updated:',
            value = data['updated'], 
            inline=True)
        
        embed.add_field(
            name='Length',
            value=str(data['num_chapters']) +
            " chapter(s) with "+str(data['num_words'])+" words", inline=True)

        if data['genres'] and not data['characters']:
            embed.add_field(name=f"Genres:", 
                        value=f"{data['genres']}", inline=False)
        elif data['characters'] and not data['genres']:
           embed.add_field(name=f"Genres:", 
                        value=f"{data['genres']}", inline=True)  
        else:
            embed.add_field(name=f"Genres:", 
                        value=f"{data['genres']}", inline=True)
            embed.add_field(name=f"Characters:",
                        value=str(data['characters']), inline=True)

        embed.add_field(name=f"Rated:",
                        value=f"{data['rated']}", inline=False)

        if data['thumb_image']:
            embed.set_thumbnail(
                url=f"https://www.fanfiction.net{data['thumb_image']}")

        embed.add_field(name="\u200b", # magic of zero-width whitespace character ;)
                value="Want to support Honeysuckle? [ Buy me a beer :beer: ](https://www.buymeacoffee.com/hbeg)",
                inline=False)
        
        embeds_list.append(embed)
    
    return embeds_list



def get_embeds_ao3(list_of_dicts_of_metadata):
    """
    to get embeds list from list of dicts of story metadata from ao3
    """
    embeds_list = []
    for data in list_of_dicts_of_metadata:
        embed = Embed(
            title= data['title'],
            url= data['link'],
            description= data['summary'],
            colour=Colour(0x272b28)
        )
        embed.set_author(name=data['authors'])

        embed.add_field(
            name = 'Status',
            value = data['status'], 
            inline=True)
        
        embed.add_field(
            name = 'Rating',
            value = data['rating'], 
            inline=True)
        
        embed.add_field(
            name = 'Language',
            value = data['language'], 
            inline=True)
        
        embed.add_field(
            name='Length',
            value=str(data['nchapters']) +
            " chapter(s) with "+str(data['words'])+" words", 
            inline=True)
        
        embed.add_field(
            name = 'Published',
            value = data['date_published'], 
            inline=True)

        embed.add_field(
            name = 'Updated',
            value = data['date_updated'], 
            inline=True)

        embed.add_field(
            name = 'Characters',
            value = data['characters'], 
            inline=True)
        
        embed.add_field(
            name = 'Categories',
            value = data['categories'], 
            inline=True)

        embed.add_field(
            name = 'Relationships',
            value = data['relationships'], 
            inline=True)

        embed.add_field(
            name = 'Warnings',
            value = data['warnings'], 
            inline=True)

        stats = f"Kudos: {data['kudos']}, Bookmarks: {data['bookmarks']}"
        embed.add_field(
            name = 'Stats',
            value = stats, 
            inline=True)

        embed.add_field(name="\u200b", # magic of zero-width whitespace character ;)
                value="Want to support Honeysuckle? [ Buy me a beer :beer: ](https://www.buymeacoffee.com/hbeg)",
                inline=False)
                
        embeds_list.append(embed)
    
    return embeds_list


