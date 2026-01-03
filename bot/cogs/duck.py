#!/usr/bin/python3
# bot/cogs/duck.py

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

class Duck(commands.Cog):
    '''
    handles the duck command(s)
    '''

    def __init__(self, bot):
        self.bot = bot

    async def _duck(self, ctx):
        user = ctx.author

        api = "https://random-d.uk/api/random"
        data = requests.get(api).json()

        image_url = data["url"]
        response = requests.get(image_url)

        image = BytesIO(response.content)
        image.seek(0)

        console.log(f"Duck image requested by {user} ({user.id})", "LOG")

        await utils.say(ctx, file=discord.File(image, filename="image.png"))  # type: ignore

    # COMMANDS

    @commands.command()
    async def duck(self, ctx):
        await self._duck(ctx)

    @commands.slash_command(name="duck", description="sends a random duck image")
    async def slash_duck(self, ctx):
        await self._duck(ctx)


# FUNCTIONS

def setup(bot):
    '''
    adds duck cog to the bot
    '''

    bot.add_cog(Duck(bot))
