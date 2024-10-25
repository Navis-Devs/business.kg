from rest_framework import generics, views, response, permissions
Response = response.Response

from .models import AutoUP, Urgent
from .serializers import AutoUPSerializer, UrgentSerializer


class AutoUPView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        balance = request.user.balance
        queryset = AutoUP.objects.all().order_by("-days")
        data = {"data": AutoUPSerializer(queryset, many=True).data}, {"currentBalance": balance}
        return Response(data, status=200)


class UrgentView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        balance = request.user.balance
        queryset = Urgent.objects.all().order_by("-days")
        data = {"data": UrgentSerializer(queryset, many=True).data}, {"currentBalance": balance}
        return Response(data, status=200)