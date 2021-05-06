"""
The main class for our mafia bot.

This module contains a single class.  Instances of this class support an game
that can be modified.  This is the main class needed to contain information about
the game within a specific discord.

Author: Lenhard O. Thomas (lot5)
Date:   May 5, 2021
"""

from exceptions import *


class Game(object):
  """
  A class that allows flexible access to a game object.

  An object will represent a game in a discord guild, and it will store
  information about the game such as: the IDs of people playing, the IDS of
  who is voting for whom, and whether the game is intializing, running, or off.

  Attributes
    guild_id : int
      - The ID of the discord guild where this game exists

    status : str
      - Either "SIGNUP", "RUNNING", or "TERMINATED" depending on the state

    signup_list : int list
      - List of player IDs of those who are currently signed up for the game

    alive_players : int list
      - List of player IDs of those who are currently alive in the game

    dead_players : int list
      - List of player IDs of those who signed up but are now dead

    votes : int -> int list dictionary
      - Dictionary mapping ID of voted player to IDs of players voting them

    no_lynch : int list
      - List of player IDs of those who are voting to not lynch in this day cycle

    cycle : str
      - Either "DAY" or "NIGHT" depending on the cycle of the running game

    day_cycle : int (immutable)
      - The number of 24 hour cycles that make up an in-game day cycle

    night_cycle : int (immutable)
      - The number of 24 hour cycles that make up n in-game night cycle

    end_time : float
      - The time in seconds (since epoch) when the day/night cycle will end
  """

  def get_signup_list(self):
    """
    Returns the signup list.
    """
    return self._signup_list

  def __init__(self, guild_id):
    """
    Initializes a game which only occurs when the bot enters the server.

    Sets `_guild_id` to guild id, status to "TERMINATED", and sets the rest of 
    the attributes to None.

    Paramater guild_id : the id of the guild where the game exists
    Precondition : an int representing a valid discord guild ID
    """
    self._guild_id = guild_id
    self._status = "TERMINATED"
    self._signup_list = None
    self._alive_players = None
    self._dead_players = None
    self._votes = None
    self._no_lynch = None
    self._cycle = None
    self._day_cycle = None
    self._night_cycle = None

  def signup(self, id):
    """
    Adds player [id] to the signup list.

    Paramater id: the id of the player who is signing up
    Precondition: an int representing a valid discord user ID
    """
    self._signup_list.append(id)

  def dropout(self, id):
    """
    Removes player [id] from the signup list. Raises the ID_NOT_FOUND error if
    the player is not already in the signup list.

    Paramater id: the id of the player who is signing up
    Precondition: an int representing a valid discord user ID
    """
    if id not in self._signup_list:
      raise ID_NOT_FOUND()
    self._signup_list.remove()

  def vote(self, voter_id, voted_id):
    """
    Has player [voter_id] vote to lynch player [voted_id]. Raises ID_NOT_PLAYING(id)
    where id is either voter_id or voted_id depending on which id that was passed
    contains a player who did not sign up.

    Paramater voter_id: the id of the player who is voting
    Precondition: an int representing a valid discord user ID

    Paramater voted_id: the id of the player who is voted to be lynched
    Precondition: an int representing a valid discord user ID
    """
    if voter_id not in self._signup_list:
      raise ID_NOT_PLAYING("voter_id")
    if voted_id not in self._signup_list:
      raise ID_NOT_PLAYING("voted_id")
    try:
      # Unvote to make sure that player does not double vote
      self.unvote(voter_id)
    except ID_NOT_FOUND:
      # Skip ID_NOT_FOUND error because it doesn't matter in this case
      pass

    if voted_id in self._votes:
      self._votes[voted_id].append(voter_id)
    else:
      self._votes[voted_id] = [voter_id]

  def vote(self, voter_id):
    """
    Has player [voter_id] vote to not lynch any players. Raises ID_NOT_PLAYING(id)
    where id is either voter_id or voted_id depending on which id that was passed
    contains a player who did not sign up.

    Paramater voter_id: the id of the player who is voting
    Precondition: an int representing a valid discord user ID
    """
    if voter_id not in self._signup_list:
      raise ID_NOT_PLAYING("voter_id")
    if voted_id not in self._signup_list:
      raise ID_NOT_PLAYING("voted_id")
    try:
      # Unvote to make sure that player does not double vote
      self.unvote(voter_id)
    except ID_NOT_FOUND:
      # Skip ID_NOT_FOUND error because it doesn't matter in this case
      pass

    self._no_lynch.append(voter_id)

  def unvote(self, id):
    """
    Has player [id] remove their vote. Raises ID_NOT_PLAYING() if id that was passed
    contains a player who did not sign up and raises the ID_NOT_FOUND error if the player
    has not already voted for somebody.

    Paramater id: the id of the player who is removing their vote
    Precondition: an int representing a valid discord user ID
    """
    if id not in self._signup_list:
      raise ID_NOT_PLAYING()
    for voted in self._votes:
      if id in self._votes[voted]:
        self._votes[voted].remove(id)
    raise ID_NOT_FOUND()

  def display_votes(self):
    """
    Returns a nicely formated string that displays who has voted for whom.
    """

  def time(self):
    """
    Returns the time remaining in the day cycle in days, hours, and minutes of
    real time.
    """

  def cycle(self):
    """
    Changes the cycle from "DAY" to "NIGHT" or vice versa.
    """

  def start(self):
    """
    Begins the mafia game.

    Running completely automatically, the bot begins the game. This function handles
    all initialization for switching to a "RUNNING" state. It raises a NOT_ENOUGH_PLAYERS
    exception if there are fewer than three players in the signup list.
    """

  def end(self):
    """
    Ends the mafia game.

    Terminates the game by switching to the "TERMINATED" state and nullifies all
    attributes except for _guild_id. 
    """
