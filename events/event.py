

from typing import List
from pydantic import BaseModel

from events.params.event_param import EventParam
from subscribers.clients.client_interface import ClientInterface

class Event:  
     """ Define on what condition will be trigger """
     def handle(self, param: EventParam):
         pass
     
     """Define subscribers """
     def subscribers(self) -> List[ClientInterface]:
          pass
         