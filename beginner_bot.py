import discord
from bot_credentials import *
client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game(name="Making a bot"))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "<@" + CLIENT_ID + ">" in message.content:
        await process_message(message)
    else:
        await message.channel.send("Error. No trigger on: " + message.content)
        

async def process_message(message):
    if "Hello there." in message.content:
        await message.channel.send("General Kenobi!")
    else:
        await message.channel.send("I didn't quite catch that.")
        
client.run(TOKEN)
