import discord
import asyncio
import json
import requests

from discord.ext.commands import Bot
from discord.ext import commands

client = commands.Bot(command_prefix="!")

BOTSLEEP=30

async def background_loop():
      await client.wait_until_ready()
      while not client.is_closed():
            try:
                  USD_ = requests.get(url='https://api.binance.com/api/v1/ticker/24hr?symbol=BNBUSDT')
                  USD_.close()
                  USD = USD_.json()

                  USD_price = round(float(USD["lastPrice"]), 3)
                  percent = round(float(USD["priceChangePercent"]), 1)

                  BTC_ = requests.get(url='https://api.binance.com/api/v1/ticker/24hr?symbol=BNBBTC')
                  BTC_.close()
                  BTC = BTC_.json()
                  
                  BTC_price = '%.8f' % float(BTC["lastPrice"])
                  playing = '$'+str(USD_price)+' '+ BTC_price

                  if percent > 0:
                        percent = ' +'+str(percent)
                  elif percent < 0:
                        percent = ' '+str(percent)
                  if percent:
                        playing = playing +percent +'%'
                  await client.change_presence(activity=discord.Game(name=playing))
                  # This is the time the bot will sleep between playing statuses
                  await asyncio.sleep(int(BOTSLEEP))
            except:
                  await asyncio.sleep(int(BOTSLEEP))
                  pass

client.loop.create_task(background_loop())
client.run('<YOUR_DISCORD_BOT_TOKEN>')