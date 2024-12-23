from rest_framework.permissions import IsAuthenticated
from apps.accounts.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class DeleteAccountView(APIView):
    permission_classes = [IsAuthenticated, ]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({'message': 'Аккаунт успешно удалён!', 'response': True}, status=status.HTTP_200_OK)