from collections import namedtuple
import os
from typing import Dict
from dotenv import load_dotenv
from subscribers.clients.client_interface import ClientInterface
from subscribers.clients.telegram import Telegram

load_dotenv()

registry: Dict[str, ClientInterface] = {
    "telegram": Telegram(os.getenv("TELEGRAM_API_TOKEN"), os.getenv("TELEGRAM_CHAT_ID"))
}