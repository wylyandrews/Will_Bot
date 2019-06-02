import discord
from bot_credentials import CLIENT_ID, TOKEN
from process_messages import second_process
from Handlers import *

if __name__ == "__main__":

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
            await PrequelHandler.handle_messages(message)
            await DNDHandler.handle_messages(message)


    client.run(TOKEN)

