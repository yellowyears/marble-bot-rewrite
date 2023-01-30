import discord
import os
from dotenv import load_dotenv

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print("Bot is ready")


load_dotenv()
token = os.getenv("TOKEN")
client.run(token)
