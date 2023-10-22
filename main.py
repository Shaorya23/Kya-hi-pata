import os
import json
import string
import base64
import discord, aiohttp
from discord.ext import commands, tasks
from discord import Permissions
import requests
from colorama import Fore
import asyncio
import requests
import logging
import sys
import random
from random import randint
from threading import Thread
import threading
import subprocess
import requests
import time
import datetime
from time import sleep
from discord import Color, Embed
import colorama
from colorama import Fore, Style
import urllib.parse
import urllib.request
import re
import io
from itertools import cycle

colorama.init()

intents = discord.Intents.default()
intents.guilds = True
intents.typing = True
intents.presences = True
intents.dm_messages = True
intents.messages = True
intents.members = True


client = commands.Bot(description='THIS SELFBOT IS CREATED BY STEVE PAPA', command_prefix='>', self_bot=True, intents=intents)
header = {"Authorization": f'Bot {"Token"}'}

Token = "ACCOUNT_TOKEN"

# YAHA SE SHURU

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(
        name='ID HOSTED HAI KID | .gg/sp1it ',
        url='https://youtube.com/'))

# COMMANDS HAI KID 

@client.command()
async def massban(ctx):
    await ctx.message.delete()
    await asyncio.sleep(2)
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason="STEVE PAPA AAYE THE")
        except:
            pass
    await asyncio.sleep(2)

@client.command()
async def prune(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  try:
            await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)

  except:
            print(f"{Fore:RED}[! ERROR AAGYA ]")



client.run(Token ,bot=False)