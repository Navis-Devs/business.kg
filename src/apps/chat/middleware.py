from urllib.parse import parse_qs
from rest_framework.authentication import TokenAuthentication
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.contrib.auth.models import AnonymousUser



class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)
        self.token_auth = TokenAuthentication()

    @database_sync_to_async
    def authenticate(self, token):
        try:
            user, _ = self.token_auth.authenticate_credentials(token)
            return user
        except Exception as e:
            print(f"Ошибка аутентификации: {e}")
            return None

    async def __call__(self, scope, receive, send):
        if scope["type"] == "websocket":
            query_string = scope.get("query_string", b"").decode()
            token = parse_qs(query_string).get("token", [None])[0]

            if token:
                # print(f"Получен токен: {token}")
                auth_result = await self.authenticate(token)

                if auth_result:
                    scope["user"] = auth_result
                else:
                    # print("Не удалось авторизовать пользователя.")
                    scope["user"] = AnonymousUser()
            else:
                # print("Токен не передан.")
                scope["user"] = AnonymousUser()

        return await super().__call__(scope, receive, send)


# class TokenAuthMiddleware(BaseMiddleware):
#     def __init__(self, inner):
#         super().__init__(inner)
#         self.token_auth = TokenAuthentication()

#     @database_sync_to_async
#     def authenticate(self, token):
#         try:
#             user, _ = self.token_auth.authenticate_credentials(token)
#             return user
#         except Exception as e:
#             return None

#     async def __call__(self, scope, receive, send):
#         if scope["type"] == "websocket":
#             query_string = scope.get("query_string", b"").decode()
#             token = parse_qs(query_string).get("token", [None])[0]

#             if token:
#                 print(f"Получен токен: {token}")
#                 auth_result = await self.authenticate(token)

#                 if auth_result:
#                     scope["user"] = auth_result
#                 else:
#                     scope["user"] = AnonymousUser()
#             else:
#                 scope["user"] = AnonymousUser()

#         else:
#             return await super().__call__(scope, receive, send)

#         return await super().__call__(scope, receive, send)

# from channels.auth import AuthMiddlewareStack
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import AnonymousUser


# class TokenAuthMiddleware:
#     """
#     Token authorization middleware for Django Channels 2
#     """

#     def init(self, inner):
#         self.inner = inner

#     def call(self, scope):
#         headers = dict(scope['headers'])
#         if b'authorization' in headers:
#             try:
#                 token_name, token_key = headers[b'authorization'].decode().split()
#                 if token_name == 'Token':
#                     token = Token.objects.get(key=token_key)
#                     scope['user'] = token.user
#             except Token.DoesNotExist:
#                 scope['user'] = AnonymousUser()
#         return self.inner(scope)

# TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))