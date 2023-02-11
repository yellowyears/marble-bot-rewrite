from discord.ext import commands
import discord

import requests
import json
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv


class MonkeyType(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        load_dotenv()
        self.ape_key = os.getenv("APE_KEY")

    @commands.Cog.listener()
    async def on_ready(self):
        print("MonkeyType is ready")

    @commands.command()
    async def monkey_type(self, ctx, user):
        response = requests.get(f"https://api.monkeytype.com/users/{user}/profile",
                                headers={'Content-Type': 'application/json', "Authorization": f"ApeKey {self.ape_key}"})
        data = json.loads(response.content)['data']

        print(data)

        typing_stats = data['typingStats']
        personal_bests = data['personalBests']

        embed = discord.Embed(color=discord.Colour.green())
        embed.title = f"{data['name']}'s stats:"
        embed.description = f"Completed tests: **{typing_stats['completedTests']}**\n" \
                            f"Time spent typing: **{str(timedelta(seconds=round(typing_stats['timeTyping'])))}**\n\n**Personal Bests:**\n\n"

        time_30 = personal_bests['time']['30'][0]
        embed.add_field(name="Time: 30", value=f"Accuracy: **{time_30['acc']}**\n"
                                               f"Consistency: **{time_30['consistency']}**\n"
                                               f"WPM: **{time_30['wpm']}**")

        embed.timestamp = datetime.utcfromtimestamp(data['addedAt'] / 1000)
        embed.set_footer(text="User Account Created (UTC)")

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(MonkeyType(bot))
