import os
my_secret = os.environ['token']

import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  if msg.startswith('.hi'):
    await message.channel.send("main nahi bataunga")

client.run(my_secret)