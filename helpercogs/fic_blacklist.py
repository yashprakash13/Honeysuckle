from botutils.constants import HS_API_URL_FIC_BLACKLIST, HS_API_URL_FIC_BLACKLIST_ADD_OR_MODIFY, FFN_CHECK_STR, AO3_CHECK_STR
import discord
import re
from discord.ext.commands import command, Cog
import asyncio
import requests
import json

from botutils.searchforlinks import get_ffn_url_from_query, get_ao3_url_from_query
from botutils.embeds import get_blacklist_embed

class FicBlacklistCog(Cog):
    def __init__(self, bot):
        self.bot = bot


    @command('bl')
    async def blacklist_get(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(1)

        response = requests.get(f'{HS_API_URL_FIC_BLACKLIST}')
        data = json.loads(response.text)

        embed_to_send = get_blacklist_embed(data)
        await ctx.send(embed=embed_to_send)
    

    @command('bladd')
    async def blacklist_add(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(1)
        
        query = ctx.message.content
        query = query[query.index('.bladd')+6: ]

        # extract link
        all_links = re.findall(r'(https?://[^\s]+)', query)
        if all_links is not None:
            for link in all_links:
                # get story_id
                if FFN_CHECK_STR in link:
                    try:
                        story_id = "FFN" + link[link.index('s/')+2 : link.index('/', link.index('s/')+4)]
                    except:
                        story_id = "FFN" + link[link.index('s/')+2 :]
                elif AO3_CHECK_STR in link:
                    try:
                        story_id = "AO3" + link[link.index('works/')+len('works/') : link.index('/', link.index('works/')+6)]
                    except:
                        story_id = "AO3" + link[link.index('works/')+len('works/') :]
                else:
                    return
                
                # send request to API for fic creation or vote modification 
                response = requests.get(f'{HS_API_URL_FIC_BLACKLIST_ADD_OR_MODIFY}/{story_id}')
                data = json.loads(response.text)
                if data["resp"] == "404_WRONG_URL":
                    await ctx.send("Can't add fic to blacklist. Not a FFN or AO3 URL.")
                elif data["resp"] == "200_VOTE_ADDED":
                    await ctx.send("Your vote was added.")
                elif data["resp"] == "200_STORY_AND_VOTE_ADDED":
                    await ctx.send("New story added to blacklist.")
                else:
                    print("Server error.", data)





def setup(bot):
    bot.add_cog(FicBlacklistCog(bot))
