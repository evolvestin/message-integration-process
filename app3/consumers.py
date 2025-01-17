import json
from channels.consumer import AsyncConsumer
from .services.front_messages_service import FrontMessagesService


class WSConsumer(AsyncConsumer):
    def __init__(self):
        pass

    async def websocket_connect(self, event):
        await self.send({'type': 'websocket.accept'})

    async def websocket_receive(self, data):
        received_message = json.loads(data['text'])
        message = {
            'messageType': received_message['messageType'],
            'mail': received_message['message']['mail'],
        }
        await FrontMessagesService.process_message(message, self)

    async def websocket_disconnect(self, event):
        pass

    async def websocket_send(self, data):
        await self.send({
            'type': 'websocket.send',
            'text': json.dumps(data)
        })
