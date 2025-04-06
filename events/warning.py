from typing import List
from subscribers.clients.client_interface import ClientInterface
from .event import Event
from subscribers import registry as subscriberRegistry
from .params.message import Message


class WarningEvent(Event):
     def handle(self, param: Message) -> None:
         for subscriber in self.subscribers():
            subscriber.echo("Warning! " + str(param))
     
     def subscribers(self) -> List[ClientInterface]:
         return [
             subscriberRegistry['telegram'],
         ]