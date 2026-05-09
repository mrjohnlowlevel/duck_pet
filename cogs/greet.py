import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Events in classes need the @commands.Cog.listener() decorator
    @commands.Cog.listener()
    async def on_ready(self):
        print('! Greetings Cog loaded !')

    # Commands in classes use @commands.command()
    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}! I am now class-based.')

# This function is required for the bot to load the Cog
async def setup(bot):
    await bot.add_cog(Greetings(bot))