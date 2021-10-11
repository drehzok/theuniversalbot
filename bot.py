import os
import discord

bot_token = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print(f"We have logged in as {client.user}")

@client.event
async def on_message(m):
  if m.author == client.user:
    return
  
  await m.channel.send(m.content)

client.run(bot_token)
