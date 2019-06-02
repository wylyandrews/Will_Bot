import discord
from bot_credentials import CLIENT_ID, TOKEN
from process_messages import second_process

client = discord.Client()


ping = "<@" + CLIENT_ID + ">"


@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game(name="Making a bot"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if ping in message.content:
        await process_message(message)
        await second_process(message)
        

async def process_message(message):
    if "Hello there." in message.content:
        await message.channel.send("General Kenobi!")


client.run(TOKEN)
