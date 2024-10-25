from rest_framework import generics, views, response, permissions

Response = response.Response

from .models import AutoUP, Urgent, Highlight
from .serializers import AutoUPSerializer, UrgentSerializer, HighlightSerializer


class BaseTariffView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    model = None
    serializer_class = None

    def get(self, request, *args, **kwargs):
        balance = request.user.balance
        queryset = self.model.objects.all().order_by("-days")
        data = {"data": self.serializer_class(queryset, many=True).data, "currentBalance": balance}
        return Response(data, status=200)


class AutoUPView(BaseTariffView):
    model = AutoUP
    serializer_class = AutoUPSerializer


class UrgentView(BaseTariffView):
    model = Urgent
    serializer_class = UrgentSerializer


class HighlightView(BaseTariffView):
    model = Highlight
    serializer_class = HighlightSerializer