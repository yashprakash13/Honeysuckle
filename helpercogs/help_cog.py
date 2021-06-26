import discord
import re
from discord.ext.commands import command, Cog

from botutils.embeds import get_help_embed, get_about_embed


class HelpCog(Cog):
    def __init__(self, bot):
        self.bot = bot


    @command('helphs')
    async def help(self, ctx):
    
        embed_help = get_help_embed()
        message = await ctx.send(embed=embed_help)
        await message.add_reaction('❤️')


    @command('abouths')
    async def about(self, ctx):
    
        embed_about = get_about_embed()
        message = await ctx.send(embed=embed_about)
        await message.add_reaction('ℹ')

        

def setup(bot):
    bot.add_cog(HelpCog(bot))
