#!/usr/bin/python3
# bot/cogs/cat.py

# LIBRARIES AND MODULES

from io import BytesIO
import requests

## pycord
from discord.ext import commands
import discord


# CLASSES

class CatCommand(commands.Cog):
    '''
    handles the cat command(s)
    '''
    def __init__(self, bot):
        self.bot = bot

    async def _cat(self, ctx):
        catapi = "https://cataas.com/cat"
        response = requests.get(catapi)
        image = BytesIO(response.content)
        image.seek(0)
        await ctx.respond(file=discord.File(image, filename="image.png"))

    #COMMANDS

    @commands.slash_command(name="cat", description="sends a random cat image")
    async def slash_cat(self, ctx):
        await self._cat(ctx)

    @commands.command()
    async def cat(self, ctx):
        await self._cat(ctx)


# FUNCTIONS

def setup(bot):
  '''
  adds cat cog to the bot
  '''

  bot.add_cog(CatCommand(bot))
