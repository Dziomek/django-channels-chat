import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        self.accept()
        self.send(text_data=json.dumps(
            {
                'type': 'connection_established',
                'message': 'You are connected now'
            }
        ))

    def websocket_receive(self, text_data):
        message = text_data['message']

        print('Message:', message)
