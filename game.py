"""
The main class for our mafia bot.

This module contains a single class.  Instances of this class support an game
that can be modified.  This is the main class needed to contain information about
the game within a specific discord.

Author: Lenhard O. Thomas (lot5)
Date:   May 5, 2021
"""


class Game(object):
  """
  A class that allows flexible access to a game object.

  An object will represent a game in a discord group, and it will store
  information about the game such as: the IDs of people playing, the IDS of
  who is voting for whom, and whether the game is intializing, running, or off.

  """
