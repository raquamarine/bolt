#!/usr/bin/python3
# bot/cogs/dog.py

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

class Dog(commands.Cog):
    '''
    handles the dog command(s)
    '''

    def __init__(self, bot):
        self.bot = bot

    async def _dog(self, ctx):
        user = ctx.author

        api = "https://dog.ceo/api/breeds/image/random"
        data = requests.get(api).json()

        image_url = data["message"]
        response = requests.get(image_url)

        image = BytesIO(response.content)
        image.seek(0)

        console.log(f"Dog image requested by {user} ({user.id})", "LOG")

        await utils.say(ctx, file=discord.File(image, filename="image.png"))  # type: ignore

    # COMMANDS

    @commands.command()
    async def dog(self, ctx):
        await self._dog(ctx)

    @commands.slash_command(name="dog", description="sends a random dog image")
    async def slash_dog(self, ctx):
        await self._dog(ctx)


# FUNCTIONS

def setup(bot):
    '''
    adds dog cog to the bot
    '''

    bot.add_cog(Dog(bot))
