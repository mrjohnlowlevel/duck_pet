import discord
from discord.ext import commands


class Sounds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('! Sounds Cog loaded !')


    @commands.command()
    async def quack(self, ctx):
        await ctx.send(f'Quack')


async def setup(bot):
    await bot.add_cog(Sounds(bot))