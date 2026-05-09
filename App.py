import discord
import os
from pathlib import Path
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


class DuckBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='?', intents=intents)

    async def setup_hook(self):
        cogs_path = Path("./cogs")
        for cog_file in cogs_path.glob("*.py"):
            if cog_file.stem != "__init__":
                await self.load_extension(f"cogs.{cog_file.stem}")
                print(f"Loaded Cog: cog.{cog_file.stem}")


if __name__ == "__main__":
    bot_token = os.getenv('BOT_TOKEN')

    bot = DuckBot()
    bot.run(bot_token)