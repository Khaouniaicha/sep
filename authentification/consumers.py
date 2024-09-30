import json
import logging
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
logger = logging.getLogger(__name__)
from asgiref.sync import sync_to_async
# consumers.py
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async
import logging

logger = logging.getLogger(__name__)


# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token


from channels.generic.websocket import AsyncJsonWebsocketConsumer

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        print(self.user)
        if self.user.is_authenticated:
            await self.accept()
            print('accept')
            await self.channel_layer.group_add('global_notify', self.channel_name)
            print('add to channle oki')
        else:
            await self.close()

    async def disconnect(self, close_code):
        if self.user.is_authenticated:
            await self.channel_layer.group_discard('global_notify', self.channel_name)

    async def send_alert(self, event):
        message = event['message']
        print( message )
        await self.send_json({
            'alert': message,
        })
        print('sends')