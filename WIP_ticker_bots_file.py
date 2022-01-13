import discord
import asyncio
import time
import json
import requests

from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix="!")

BOTSLEEP=30
BOTPAIR="XRP_USDT"
BOTFIAT="USD"

async def background_loop():
      await client.wait_until_ready()
      while not client.is_closed():
            try:
                  # Get all pairs from CryptoBridge exchange
                  tok_response = requests.get(url='https://api.crypto-bridge.org/api/v1/ticker')
                  tok_response.close()
                  tok_data = tok_response.json()

                  for line in tok_data:
                        if line["id"] == BOTPAIR:
                              lst = line["last"]
                              percent = line["percentChange"]
                  #        vol = line["volume"]
                  #        ask = line["ask"]

                  # Get fiat value versus BTC
                  #fiat_response = requests.get(url='https://blockchain.info/it/ticker')
                  #fiat_response.close()
                  #fiat_data = fiat_response.json()
              
                  # Get the last price for selected fiat and calculate the value of the token in fiat.
                  #btcfia = fiat_data[BOTFIAT]["last"]
                  #tokfia = round(float(lst) * float(btcfia), 2)
                  tokfia = round(float(lst), 2)
                  # Calculate the token volume
                  #tokvol = round(float(vol) / float(ask), 3)

                  # Grab the first half of the pair
                  #toksym = BOTPAIR.split('_', 1)[0]

                  #playing = []
                  #playing.append('฿ ' + str(lst) + ' BTC')
                  playing = '$' + str(tokfia) + ' '+ percent+ '%'# + ' ' + BOTFIAT
                  ## add MEX - BFX 

                  #playing.append('฿ ' + str(vol) + ' VOL 24h')
                  #playing.append(toksym + ' ' + str(tokvol) + ' VOL 24h')

                  # This loop is there to space out the request to the API for an avarage of 5 minutes.
                  #for time in range(5):
                  #print(time)
                  #for play in playing:
                  
                  # The magical update of the playing bot status happens here!
                  await client.change_presence(activity=discord.Game(name=playing))
                  # This is the time the bot will sleep between playing statuses
                  await asyncio.sleep(int(BOTSLEEP))
            except:
                  pass

client.loop.create_task(background_loop())
client.run(client.run('<YOUR_DISCORD_BOT_TOKEN>'))