
###################################################
#
# Handler meant for test runs for ACM commands
#
###################################################

from Handlers.base_handler import BaseHandler

import random


class DNDHandler(BaseHandler):

    @classmethod
    async def handle_messages(cls, message=None):

        if "!opinion" in message.content.lower():
            await cls.opinion(message)

    @classmethod
    async def opinion(cls, message):
        # I'm just cloning the bot repo, I might test basic functions here for it.
        # the ACM bot runs differently from this one, so I can't copy 1-to-1 from here

            adjective = random.choice([
                "",
                "bold"
                "brutally honest",
                "controversial",
                "honest",
                "humble",
                "insightful",
                "off-color",
                "off-the-record",
                "perceptive",
                "true",
                "undebatable"
            ])

            opening_remarks = random.choice([
                "",
                "I believe",
                "I think",
                "I would say",

            ])
            language = random.choice([
                "Ada",
                "Basic",
                "C",
                "C#",
                "C++",
                "CSS",
                "HTML",
                "Java",
                "Javascript",
                "LambdaMOO",
                "Lisp",
                "Pascal",
                "PHP",
                "Prolog",
                "Python",
                "Ruby",
                "Swift",
                "Visual Basic"
            ])

            opinion = random.choice([
                "could use some more work.",
                "is a gift to mankind!",
                "is actually pretty good.",
                "is decent.",
                "is my favorite programming language,"
                "is the worst language created.",
                "is wonderful!",
                "needs improvements.",
                "should be banned from GitHub.",
                "shouldn't be considered a language."

            ])

            closing_remarks = random.choice([
                "",
                "Any arguments?",
                "But hey, that's just my opinion. A robbot opinion.",
                "But that's what everybody says.",
                "Do you agree?",
                "I hope you would say the same!",
                "I know it's not that popular of an opinion.",
                "I know others tend to agree."
                "Thoughts?",
                "What do you think?"
            ])

            my_opinion = "In my " + adjective + " opinion, " + \
                         opening_remarks + " " + language + " " + opinion + " " + closing_remarks

            await message.channel.send(my_opinion)
