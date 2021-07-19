import discord
import asyncio
from discord.ext.commands import command, Cog
from brain import receiver

class AdminCog(Cog):
    def __init__(self, bot):
        self.bot = bot


    @command('ping')
    async def ping(self, ctx):
        message = await ctx.send("pong")
        await message.add_reaction('👋🏼')


    @command('noreply')
    async def about(self, ctx):
        """send a fic embed without a reply to another person's message"""
        async with ctx.typing():
            await asyncio.sleep(1)
        
        text = ctx.message.content

        # see if message has any links or not
        embeds_to_send = receiver.process_message(text)
        if embeds_to_send:
            async with ctx.message.channel.typing():
                for embed in embeds_to_send:
                    await ctx.send(embed=embed)
    

        

def setup(bot):
    bot.add_cog(AdminCog(bot))