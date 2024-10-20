import os
from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from ..app3.routing import ws_urlpatterns
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')


django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(ws_urlpatterns)
    )
})
