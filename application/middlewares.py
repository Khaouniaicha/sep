from rest_framework.authtoken.models import Token
from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser

@database_sync_to_async
def get_user_from_token(token_key):
    try:
        user = Token.objects.get(key=token_key).user
        print(f"User fetched: {user.username}")  # Debug: Check the user fetched
        return user
    except Token.DoesNotExist:
        print("Token not found")  # Debug: Token was not valid
        return AnonymousUser()

class TokenAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        query_string = scope.get('query_string', b'')
        print(query_string)
        parsed_query = parse_qs(query_string.decode())
        print( parsed_query)
        token_key = parsed_query.get('token', [None])[0]
        print(token_key)

        if token_key:
            scope['user'] = await get_user_from_token(token_key)
            print(scope['user'])
        else:
            print("No token provided")  # Debug: No token in query
            scope['user'] = AnonymousUser()

        return await self.app(scope, receive, send)
