

async def second_process(message):
    if "This is getting out of hand." in message.content:
        await message.channel.send("Now there are two of them!")
