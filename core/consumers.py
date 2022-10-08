import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from channels.auth import logout


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        #########################
        self.room_group_name = None
        self.user = None

    async def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['room_name']
        print('ROOM:', self.room_group_name)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        await self.send(text_data=json.dumps({
            'type': 'connection',
            'message': 'connected',
        }))

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
        room_name = self.scope['url_route']['kwargs']['room_name']
        username = self.scope['url_route']['kwargs']['username']
        message = Message.objects.create(content=content, username=username, room_name=room_name)
        message.save()
        return message

    async def chat_message(self, event):
        content = event['message']

        message = await self.create_message(content)

        await self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message.content,
            'username': message.username
        }))