#!/usr/bin/env python3
# bot/utils.py
'''
Utility functions for the bot.
These are used throughout the bot's codebase.

This file is a collection of functions that are useful in multiple places,
not specific to any single cog or module.
In layman's terms, this is just a group of functions that don't belong anywhere else,
because DRY.
'''

# LIBRARIES AND MODULES

from typing import Any
from dotenv import load_dotenv
import os

## pycord

import discord
from discord.ext import commands

## pypkg

from bot.constants.config import env_path, units

# FUNCTIONS

def get_env_var(var: str, default: Any, required=True, from_dot_env=True) -> Any:
  '''
  Retrieves an environment variable from a .env file.

  ### Parameters
  * var (str): the name of the variable to retrieve
  * default (Any): the default value to return if the variable is not found
  * required (bool): whether the variable is required. if True and the variable is not found, raises
                     an error. default: True
  * from_dot_env (bool): whether to load the variable from a .env file. default: True

  ### Returns
  Any: the value of the environment variable, or the default value if not found

  ### Raises
  * FileNotFoundError: if from_dot_env is True and the .env file does not exist and the variable is required
  * ValueError: if the variable is not found and is required
  '''
  
  if from_dot_env:
    if not env_path.exists():
      if required:
        raise FileNotFoundError(f"fatal: No .env file found, please create one including {var}")
      else:
        return default
    
    load_dotenv(dotenv_path=env_path)

  val = os.getenv(var, default)
  if val is None and required:
    raise ValueError(f"fatal: Required variable ({var}) not found in .env file.")
    
  return val

def parse_duration(duration: str) -> int | bool | None: # the return type annotations are back now. screw me i guess. -spark
  '''
  Parses a string (e.g. "1h30m") into a duration in seconds.

  # Parameters
  * duration (str): the duration string to parse

  # Returns
  int | bool | None: the duration in seconds (int), False if invalid, or None if empty
  '''
  # no, we're not using regex. regex makes me have an aneurysm. -spark

  duration = duration.strip().lower()

  if not duration:
    return None
  
  total_seconds = 0
  num = ''

  for char in duration:
    if char.isdigit():
      num += char
    elif char in units:
      if not num:
        return False # meaning invalid
      
      total_seconds += int(num) * units[char]
      num = ''

  return total_seconds if total_seconds > 0 else False

async def say(ctx: commands.Context | discord.ApplicationContext, msg: str = "", ephemeral=False, file = discord.File | None):
  '''
  This function is a coroutine.

  A wrapper to send messages in both regular and application contexts.
  
  Wraps both ctx.send() and ctx.respond().

  ### Parameters
  * ctx (discord.ApplicationContext | commands.Context): the context to send the message in
  * msg (str): the message to send. default: ""
  * ephemeral (bool): whether the message should be ephemeral (only for application contexts). default: False
  * file (discord.File | None): a file to send with the message. default: None

  ### Returns
  it doesn't return anything.

  ### Raises
  nothing.
  '''

  if isinstance(ctx, discord.ApplicationContext):
    await ctx.respond(msg, ephemeral=ephemeral, file=file)
  else:
    await ctx.send(msg, file=file)

async def assert_guild(ctx: commands.Context | discord.ApplicationContext) -> bool:
  '''
  This function is a coroutine.

  Asserts that the context is in a guild.

  ### Parameters
  * ctx (discord.ApplicationContext | commands.Context): the context to check

  ### Returns
  * bool: True if in a guild, False otherwise

  ### Raises
  nothing.
  '''
  # spark: i despise this function

  return ctx.guild is not None
