from abc import ABC

from events.params.event_param import EventParam


class Message(EventParam):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message