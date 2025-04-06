from abc import ABC, abstractmethod

class EventParam(ABC):
    @abstractmethod
    def __str__(self):
        pass