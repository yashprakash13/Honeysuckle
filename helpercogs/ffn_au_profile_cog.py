from botutils.embeds import FFNAUProfileEmbedMaker
from brain.ffn_brain.ffn_au_profile import FFNAuProfiler
import re
from discord.ext.commands import command, Cog
import asyncio

class FFNAuProfileCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command('au')
    async def au_profile(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(1)
        
        # get the message
        query = ctx.message.content
        query = query[query.index('.au')+3: ]

        # send it to au profiler to extract bio and story details
        all_au_data = FFNAuProfiler(query)
        au_link, au_name, au_intro_line, au_names_ids_tuple, au_story_details = all_au_data.get_all_metadata_for_embed_generation()
        if not au_link or not au_name or not au_intro_line or not au_names_ids_tuple or not au_story_details:
            return
        
        # get embeds
        try:
            ffn_au_embedmaker_obj = FFNAUProfileEmbedMaker(au_link, au_name, au_intro_line, au_names_ids_tuple, au_story_details)
            embed_au = ffn_au_embedmaker_obj.get_embed_page() # get first page of embed
            page_limit = ffn_au_embedmaker_obj.get_page_limit()
    
            message = await ctx.send(embed=embed_au)
            await message.add_reaction('⏮')
            await message.add_reaction('◀')
            await message.add_reaction('▶')
            await message.add_reaction('⏭')

            def check(reaction, user):
                return user == ctx.author

            page = 0
            reaction = None

            while True:
                if str(reaction) == '⏮':
                    page = 1
                    embed_pg = ffn_au_embedmaker_obj.get_embed_page(page)
                    await message.edit(embed=embed_pg)
                elif str(reaction) == '◀':
                    if page > 1:
                        page -= 1
                        embed_pg = ffn_au_embedmaker_obj.get_embed_page(page)
                        await message.edit(embed=embed_pg)
                elif str(reaction) == '▶':
                    if page < page_limit:
                        page += 1
                        embed_pg = ffn_au_embedmaker_obj.get_embed_page(page)
                        await message.edit(embed=embed_pg)
                elif str(reaction) == '⏭':
                    page = page_limit
                    embed_pg = ffn_au_embedmaker_obj.get_embed_page(page)
                    await message.edit(embed=embed_pg)

                reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
                await message.remove_reaction(reaction, user)
        except Exception as e:
            pass
        finally:
            try:
                await message.clear_reactions()
            except UnboundLocalError:
                pass  
        


def setup(bot):
    bot.add_cog(FFNAuProfileCog(bot))
