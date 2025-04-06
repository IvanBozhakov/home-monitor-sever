
from typing import List
from events.warning import WarningEvent
from .condition import Condition
from ..params.message import Message


class Scheduler:
    def __init__(self, conditions: List[Condition]):
        self.__conditions = conditions

    def on_true(self, event: WarningEvent):
        messages = [str(condition) for condition in self.__conditions if condition.check()]
        
        if messages: 
            event.handle(Message(''.join(messages)))

