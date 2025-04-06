from dotenv import load_dotenv
from tinydb import TinyDB
from typing import Set
import os
load_dotenv()

class Repository:
    db: TinyDB

    def __init__(self):
        self.db = TinyDB(os.getenv("DATABASE"))

    def get_hubs(self) -> Set[str]:
        return self.db.tables()