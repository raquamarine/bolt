#!/usr/bin/env python3
# bot/constants/base.py
'''
the base constant file that is required for the bot to boot.
contains the bot prefix and the extensions to load.
'''

# LIBRARIES AND MODULES

## pypkg

from bot.utils import get_env_var
from bot.constants.config import default_prefix
from pathlib import Path
import re


# CONSTANTS

prefix = get_env_var("PREFIX", default=default_prefix, required=False, from_dot_env=True)

# this feels very cursed

f = list(Path('bot/cogs').iterdir())
extensions = []
n = lambda i : re.sub('[/\\\\]','.',re.sub('.py$','',str(i.relative_to('bot/cogs'))))

for i in f:
  if i.name == '__init__.py' or i.name == '__pycache__' or i.name == 'base.py':
    pass
  elif i.is_file():
    #print(f"bot.cogs.{n(i)}")
    extensions.append(f"bot.cogs.{n(i)}")
  else:
    for j in i.iterdir():
      f.append(j)

del f # i dont trust the garbage collector -ad
del n # (i actually just want 1-letter variables i will never write descriptive variables >:) )
extensions = tuple(extensions)
