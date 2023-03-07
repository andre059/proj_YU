import os
import json
from googleapiclient.discovery import build


class Youtube:
    def __init__(self, channel_id, api_key):
        """
        Получение API ключа и ID каналла
        :param channel_id: ID каналла
        :param api_key: API ключа
        """
        self.channel_id = channel_id
        self.api_key: str = os.getenv(api_key)  # api ключь
        self.youtube = None
        self.channel = None

    def print_info(self):
        """
        Работа с данными каналла
        :return:
        """
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)  # специальный объект для работы с API
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return json.dumps(self.channel, indent=2, ensure_ascii=False)


item = Youtube('UC1eFXmJNkjITxPFWTy6RsWg', 'API KEY')

print(item.print_info())

