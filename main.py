import os
import json

from googleapiclient.channel import Channel
from googleapiclient.discovery import build


# API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('API KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'

channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

print(json.dumps(channel, indent=2, ensure_ascii=False))

