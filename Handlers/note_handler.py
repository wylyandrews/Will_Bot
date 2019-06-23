from Handlers.base_handler import BaseHandler


class NoteHandler(BaseHandler):
    reminder_flags = [
        "remember this",
        "remind me",
        "reminder",
    ]

    view_reminders_flags = [
        "view all reminders",
        "view all my reminders",
        "view reminders",
        "view my reminders",
    ]

    time_units = [
        "seconds",
        "minutes",
        "hours",
        "days",
        "weeks",
        "months",
        "years"
    ]
    # key relates to person
    # value relates to a dict of his reminders
    reminders = dict()

    @classmethod
    async def handle_messages(cls, message=None):

        for flag in cls.view_reminders_flags:
            if flag in message.content.lower():
                await cls.view_reminders(message)
                return

        for flag in cls.reminder_flags:
            if flag in message.content.lower():
                await cls.reminder(message)
                return

    @classmethod
    async def reminder(cls, message):
        author = message.author
        if author not in cls.reminders:
            cls.reminders[author] = list()
        cls.reminders[author].append(message.content)
        await message.channel.send("Saved your reminder...")

    @classmethod
    async def view_reminders(cls, message):
        author = message.author
        if author not in cls.reminders:
            await message.channel.send("You have no reminders to view.")
            return
        await message.channel.send(cls.reminders[author])
