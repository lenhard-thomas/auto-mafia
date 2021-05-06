import os
import discord
import typing
from discord.ext import commands
from discord.ext import tasks

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
  print("Mafia bot is ready.")

token = os.environ.get("MAFIA_TEST_TOKEN")
client.run(token)
