from abc import ABC, abstractmethod

class ClientInterface(ABC):
    """
    This is the interface (abstract class) for All clinents who want to be subscribed
    """

    @abstractmethod
    def echo(self, message: str) -> bool:
        """
        Send a message to a Client
        """
        pass