from rest_framework import generics, views, response, permissions
Response = response.Response

from .models import AutoUP
from .serializers import AutoUPSerializer

class AutoUPView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        balance = request.user.balance
        queryset = AutoUP.objects.all()
        data = {"data": AutoUPSerializer(queryset, many=True).data}, {"currentBalance": balance}
        return Response(data, status=200)
