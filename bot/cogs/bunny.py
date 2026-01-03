#!/usr/bin/python3
# bot/cogs/bunny.py

# LIBRARIES AND MODULES

from io import BytesIO
import requests

## pycord

from discord.ext import commands
import discord

# pypkg

import bot.utils as utils
import bot.console as console


# CLASSES

class Bunny(commands.Cog):
    '''
    handles the bunny command(s)
    '''

    def __init__(self, bot):
        self.bot = bot

    async def _bunny(self, ctx):
        user = ctx.author

        api = "https://rabbit-api-two.vercel.app/api/random"
        data = requests.get(api).json()

        image_url = data["url"] # it sends json with the bread and link instead of only the image
        response = requests.get(image_url)

        image = BytesIO(response.content)
        image.seek(0)

        console.log(f"bnuy image requested by {user} ({user.id})", "LOG")

        await utils.say(ctx, file=discord.File(image, filename="image.png"))  # type: ignore

    # COMMANDS

    @commands.command()
    async def bunny(self, ctx):
        await self._bunny(ctx)

    @commands.slash_command(name="bunny", description="sends a random bunny image")
    async def slash_bunny(self, ctx):
        await self._bunny(ctx)


# FUNCTIONS

def setup(bot):
    '''
    adds bunny cog to the bot
    '''

    bot.add_cog(Bunny(bot))
