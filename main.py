from secret import discord_token
from client import client
import message

@client.event
async def on_ready():
    print("ThanosBot is online.")

async def on_message(message):
    await message.on_message(message)
      
client.run(discord_token)