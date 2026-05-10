from discord.ext import commands


class Interactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('! Interactions Cog loaded !')


    @commands.command()
    async def repeat_word(self, ctx: commands.Context, time: int, arg: str):
        for _ in range(time):
            await ctx.send(arg)


async def setup(bot):
    await bot.add_cog(Interactions(bot))