# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path,re_path
from authentification import consumers
from authentification.consumers import ChatConsumer
from application.middlewares import TokenAuthMiddleware

websocket_urlpatterns = [
 
    path('ws/notification/', ChatConsumer.as_asgi()),



]

application = ProtocolTypeRouter({
    "http": URLRouter([
    ]),
    "websocket":TokenAuthMiddleware(AllowedHostsOriginValidator(
     (
          (URLRouter(
                websocket_urlpatterns
            ))
        )),
    ),
})
