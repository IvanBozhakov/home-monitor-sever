import requests
from subscribers.clients.client_interface import ClientInterface

class Telegram(ClientInterface):
    def __init__(self, api_token, chat_id):
        self.__chat_id = chat_id
        self.__url = f"https://api.telegram.org/bot{api_token}/sendMessage"

    def echo(self, message):
        params = {
            "chat_id": self.__chat_id,
            "text": message
        }

        response = requests.post(self.__url, params=params)
        if response.status_code == 200:
            return True
        else:
            raise Exception(f"ERROR code: {response.status_code}, response: {str(response.json())}")