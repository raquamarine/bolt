#!/usr/bin/env python3
# bot/console.py
'''
Logging utilities for the bot.
'''

# NOTE: this file is literally empty aside from log()
#       im not sure if console.log should be moved to utils.py
#       one less file is always nice but it WOULD break literally
#       every instance of console.log() which would need to be replaced with
#       utils.log() which i will never get used to

# LIBRARIES AND MODULES

import time # TODO: replace with datetime

# NOTE: yes we are not using logging
#       we are literally just printing to stdout
#       there is no need to make things more complicated

## pypkg

import bot.constants.colors as colors
import bot.constants.toml as toml_config

# FUNCTIONS

def log(msg, level="LOG"):
  '''
  Logs a message to the console with a given level, and formats it with colors.
  
  Example output:
  `[LOG] [Fri Sep 25 14:23:29 1970] This is a log message.`

  ### Accepted levels:
  * "LOG"
  * "INFO"
  * "WARN"
  * "ERROR"
  * "DEBUG"
  * "ERROR"
  * "FATAL"

  ### Parameters
  * msg (str): the message to log
  * level (str): the level of the log message. default: "LOG"

  ### Returns
  nothing.

  ### Raises
  nothing.
  '''

  level = level.upper()

  if level in toml_config.levels_to_ignore:
    return

  level_str = f"{colors.log_colors.get(level, '')}[{level}]{colors.reset_colors}"
  time_str = f"[{time.asctime(time.gmtime())}]" # not local time because timezones are annoying
  full = f"{level_str} {time_str} {msg}"

  print(full)