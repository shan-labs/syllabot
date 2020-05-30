"""
This module is the heart and entry-point of the syllabot.
"""


import os

from dotenv import load_dotenv

from discord.ext.commands import Bot
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv("TOKEN")
PREFIXES = os.getenv("PREFIX")
BOT_PREFIX = tuple(PREFIXES.split()) if PREFIXES else ()
client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    """Some commands when the bot has been booted up. Mostly helpful prints."""
    print("Logged in as " + client.user.name)


@client.command()
async def ping(ctx):
    """Ping pong is a great game."""
    await ctx.send("Pong!")


def main():
    """Execute helpful information about program and then start bot."""
    client.run(TOKEN)


if __name__ == '__main__':
    main()
