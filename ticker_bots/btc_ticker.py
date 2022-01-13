from discord.ext.commands import Bot
from discord.ext import commands
import discord

import asyncio
import requests
import json

# This script updates a bot-user's "now playing" status
                                                       
# Init Discord client
# Brings the bot-user online in the discord server
client = commands.Bot(command_prefix="!")

BOTSLEEP = 30  # API Polling Rate
BOTPAIR = "BTCUSD"

async def background_loop():
    await client.wait_until_ready()
    while not client.is_closed():
        try:
            # Fetch BTC data from BitMEX
            XBTUSD_ = requests.get(url='https://www.bitmex.com/api/v1/instrument?symbol=XBTUSD')
            XBTUSD_.close()
            XBTUSD = XBTUSD_.json()

            # Fetch BTC data from BitFinex too
            finex_ = requests.get(url='https://api-pub.bitfinex.com/v2/ticker/tBTCUSD')
            finex_.close()
            finex = finex_.json()
            
            # Update the Bot User's custom status to be the Last price from both datasets
            now_playing = '$'+str(XBTUSD[0]["lastPrice"])+' MEX $'+str(int(finex[-4]))+' BFX'

            # The magical update of the 'now playing' bot status happens here!
            await client.change_presence(activity=discord.Game(name=now_playing))
        except:
            pass
        await asyncio.sleep(int(BOTSLEEP))

client.loop.create_task(background_loop())

# Discord Bot-User Token
client.run('<YOUR_DISCORD_BOT_TOKEN>')