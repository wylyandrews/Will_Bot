import random

from Handlers.base_handler import BaseHandler


class DNDHandler(BaseHandler):

    @classmethod
    async def handle_messages(cls, message=None):

        await cls.roll(message)

    @classmethod
    async def roll(cls, message):
        if "roll" in message.content:
            position = message.content.index("roll")
            position += len("roll")
            new_message = message.content[position:]
            split_message = new_message.split()
            for part in split_message:
                if len(part) >= 2 and part[0] == "d" and part[1:].isdigit() and int(part[1:]) != 0:
                    die = int(part[1:])
                    break
            else:
                die = 20

            answer = random.randint(1, die)
            await message.channel.send("Your d" + str(die) + " roll is: " + str(answer))
