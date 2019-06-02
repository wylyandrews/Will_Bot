import random

from Handlers.base_handler import BaseHandler


class DNDHandler(BaseHandler):

    @classmethod
    async def handle_messages(cls, message=None):

        await cls.roll(message)

    @classmethod
    async def roll(cls, message):
        if "roll" in message.content:
            answer = random.randint(1, 21)
            await message.channel.send("Your roll is: " + str(answer))