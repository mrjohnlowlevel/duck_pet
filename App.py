import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN: str = os.getenv('BOT_TOKEN')

description = """Duck Pet"""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    assert bot.user is not None

    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

@bot.command()
async def test(ctx):
    await ctx.send("Hello, World")


bot.run(TOKEN)