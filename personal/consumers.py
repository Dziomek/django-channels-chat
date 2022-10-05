import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        #########################
        self.room_group_name = None

    async def connect(self):
        self.room_group_name = 'test'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(str(text_data))
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            })

    @database_sync_to_async
    def create_message(self, content):
        message = Message.objects.create(content=content)
        message.save()
        return message

    async def chat_message(self, event):
        content = event['message']

        message = await self.create_message(content)

        await self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message.content
        }))