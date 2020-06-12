"""
This module is the heart and entry-point of the syllabot.
"""


import os

from dotenv import load_dotenv
import json
import requests

from discord.ext.commands import Bot
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv("TOKEN")
BOT_PREFIX = os.getenv("PREFIX")
client = Bot(command_prefix=BOT_PREFIX)

FILES_URL = os.getenv("SYLLABI_FILES")

@client.event
async def on_ready():
    print("Logged in as " + client.user.name)


def get_syllabi():
    """
    Gets all syllabi from RichAguil/HunterCS_CourseSyllabi.

    HACK depends on RichAguil/HunterCS_CourseSyllabi pdfs to only be
         syllabi pdfs, this shouldn't matter too much with filters
         augmented on top of this
    """
    res = requests.get(FILES_URL)
    files = json.loads(res.text)["tree"]
    relevant_files = filter(lambda file: file["path"].endswith(".pdf"), files)
    return map(lambda file: {"file": file["path"].split("/")[-1], "url": file["url"]}, relevant_files)

@client.command()
async def ping(ctx):
    """Ping pong is a great game."""
    await ctx.send("Pong!")


def main():
    """Execute helpful information about program and then start bot."""
    r = get_syllabi()
    for i in r:
        print(i)
    # client.run(TOKEN)


if __name__ == '__main__':
    main()
