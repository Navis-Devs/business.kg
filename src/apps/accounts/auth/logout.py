from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class LogoutAccountView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        user = request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response({'message': 'Вы вышли с аккаунта!', 'response': True}, status=status.HTTP_200_OK)