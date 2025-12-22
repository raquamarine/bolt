#!/usr/bin/env python3
# bot/markdown/markdown.py
'''
paired with the md files in bot/markdown.
'''

# LIBRARIES AND MODULES

from pathlib import Path
from bot.constants.base import prefix
from dataclasses import dataclass, field

# DATA CLASSES

'''
format:
* path: Path = Path("bot/markdown/FILE.md")
* other variables as needed, with type annotations
* find_and_replace: dict = {"find": "replace"}
'''

@dataclass(frozen=False)
class Help:
  # TODO: make the links come from config
  path: Path = Path("bot/markdown/help.md")
  repo_link: str = "https://github.com/sparkhere-sys/bolt"
  support_server_link: str = "https://discord.gg/hF6mgCE3gT"

  find_and_replace: dict = field(default_factory=dict)
  
  def __post_init__(self):
    if not self.find_and_replace:
      self.find_and_replace.update({
        "{prefix}": prefix,
        "{support}": f"<{self.support_server_link}>",
        "{repo}": f"Bolt is open source! You can find the code at <{self.repo_link}>",
      })

@dataclass(frozen=False)
class Invite:
  # TODO: make the links come from config
  path: Path = Path("bot/markdown/invite.md")
  invite_link: str = "https://sparkhere-sys.github.io/bolt"
  support_server_link: str = "https://discord.gg/hF6mgCE3gT"

  find_and_replace: dict = field(default_factory=dict)

  def __post_init__(self):
    if not self.find_and_replace:
      self.find_and_replace.update({
        "{invite}": f"<{self.invite_link}>",
        "{support}": f"<{self.support_server_link}>",
      })