import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    if __name__ == "__main__":
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                cog_name = f"cogs.{filename[:-3]}"

                try:
                    await bot.load_extension(cog_name)
                except TypeError:
                    print(f"ERROR: You are trying to load a cog ({cog_name})which does not inherit from commands.Cog!")
                except commands.CommandError:
                    print(f"ERROR: The cog ({cog_name}) could not be loaded!")
                except discord.ClientException:
                    print(f"ERROR: The cog ({cog_name}) is already loaded!")
                else:
                    print(f"Cog {cog_name} loaded successfully!")

    print("Marble Bot is loaded")


load_dotenv()
token = os.getenv("TOKEN")

bot.run(token)
