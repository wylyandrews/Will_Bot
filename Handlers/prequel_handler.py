from Handlers.base_handler import BaseHandler


class PrequelHandler(BaseHandler):

    @classmethod
    async def handle_messages(cls, message=None):
        await cls.process_message(message)
        await cls.second_process(message)

    @classmethod
    async def process_message(cls, message):
        if "Hello there." in message.content:
            await message.channel.send("General Kenobi!")

    @classmethod
    async def second_process(cls, message):
        if "This is getting out of hand." in message.content:
            await message.channel.send("Now there are two of them!")
