#!/usr/bin/python3
# bot/cogs/fox.py

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

class Fox(commands.Cog):
    '''
    handles the fox command(s)
    '''

    def __init__(self, bot):
        self.bot = bot

    async def _fox(self, ctx):
        user = ctx.author

        api = "https://randomfox.ca/floof/"
        data = requests.get(api).json()

        image_url = data["image"]
        response = requests.get(image_url)

        image = BytesIO(response.content)
        image.seek(0)

        console.log(f"fox image requested by {user} ({user.id})", "LOG")

        await utils.say(ctx, file=discord.File(image, filename="image.png"))  # type: ignore

    # COMMANDS

    @commands.command()
    async def fox(self, ctx):
        await self._fox(ctx)

    @commands.slash_command(name="fox", description="sends a random fox image")
    async def slash_fox(self, ctx):
        await self._fox(ctx)


# FUNCTIONS

def setup(bot):
    '''
    adds fox cog to the bot
    '''

    bot.add_cog(Fox(bot))
