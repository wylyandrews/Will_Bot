import random

from Handlers.base_handler import BaseHandler


class DNDHandler(BaseHandler):

    @classmethod
    async def handle_messages(cls, message=None):

        await cls.roll(message)

    @classmethod
    async def roll(cls, message):
        if "roll" in message.content.lower():
            position = message.content.lower().index("roll")
            position += len("roll")
            new_message = message.content[position:]
            split_message = new_message.split()

            has_one_rolled = False
            my_rolls = dict()
            for part in split_message:
                # search part for a die roll
                for letter in part:
                    if letter == "d":
                        index = part.index("d")

                        # find out if there's any misc. characters after the number part of the roll
                        end = len(part)

                        while index+1 < end and not part[index+1:end].isdigit():
                            end -= 1

                        # empty substring. move on to next letter
                        if not part[index+1:end].isdigit():
                            continue

                        # determine if letter is part of die command or regular word
                        if len(part) > index+1 and part[index+1:end].isdigit() and int(part[index+1:end]) != 0:
                            has_one_rolled = True
                            die = int(part[index+1:end])

                            start = 0

                            while start < index and not part[start:index].isdigit():
                                start += 1

                            if part[:index].isdigit():
                                total = int(part[:index])
                            else:
                                total = 1

                            if die not in my_rolls:
                                my_rolls[die] = total
                            else:
                                my_rolls[die] += total
                            break

            if not has_one_rolled:
                answer = random.randint(1, 20)
                await message.channel.send("Your d20 roll is: " + str(answer))
            else:
                if len(my_rolls) > 5:
                    await message.channel.send("Woah, man. I can get in trouble for rolling that much.")
                    await message.channel.send("Try something shorter.")
                else:
                    for die, total in my_rolls.items():
                        answer = 0
                        int_rolls = list()
                        my_message = "Your " + str(total) + "d" + str(die)
                        if total == 1:
                            my_message += " roll is:"
                        else:
                            my_message += " rolls are:"
                        for _ in range(total):
                            int_rolls.append(random.randint(1, die))
                            my_message += " " + str(int_rolls[_])
                            if _ != total-1:
                                my_message += " +"
                        my_message += " = " + str(sum(int_rolls))

                        if "disadvantage" in message.content.lower():
                            my_message += " ( disadvantage would make that " + str(min(int_rolls)) + " )"
                        elif "advantage" in message.content.lower():
                            my_message += " ( advantage would make that " + str(max(int_rolls)) + " )"

                        if len(my_message) >= 2000:
                            my_message = my_message[:40] + " ... " + my_message[-40:]
                        await message.channel.send(my_message)


