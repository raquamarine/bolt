#!/usr/bin/env python3
# bot/constants/moderation.py
'''
Permission mappings for moderation commands.

Used by moderation cogs to check for required permissions.
'''

# CONSTANTS

perm_map = {
  "ban": "ban_members",
  "kick": "kick_members",
  "timeout": "moderate_members",
}

un_perm_map = {
  "unban": "ban_members",
  "untimeout": "moderate_members",
}