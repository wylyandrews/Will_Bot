from abc import ABC, abstractmethod


class BaseHandler(ABC):

    @classmethod
    @abstractmethod
    async def handle_messages(cls, message=None):
        raise NotImplementedError("Handle messages must be implemented to use this function.")
