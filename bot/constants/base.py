#!/usr/bin/env python3
# bot/constants/base.py
'''
Base constant file required for the bot to boot.
'''

# LIBRARIES AND MODULES

from pathlib import Path
import re # I HATE REGEX -spark

## pypkg

import bot.constants.toml as toml_config

# CONSTANTS

# this feels very cursed -ad
# it 100% is -spark

extensions = []

_cogs = list(Path('bot/cogs').iterdir())
_regex = lambda i : re.sub('[/\\\\]', '.', re.sub('.py$','',str(i.relative_to('bot/cogs'))))
# i don't understand a single letter of that regex so if this breaks please tell ad not me -spark
_ignored_files = ('__pycache__', '__init__.py', 'base.py')
_disabled_cogs = toml_config.disabled_cogs

for i in _cogs:
  if i.name in _ignored_files or i.name in _disabled_cogs:
    continue
  elif i.is_file() and str(i)[-3:] == ".py":
    extensions.append(f"bot.cogs.{_regex(i)}")
  elif i.is_dir():
    for j in i.iterdir():
      _cogs.append(j)
