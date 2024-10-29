from rest_framework import generics, views, response, permissions

Response = response.Response

from .models import AutoUP, Urgent, Highlight, Top
from .serializers import (
    TopSerializer,
    AutoUPSerializer,
    UrgentSerializer,
    HighlightSerializer,
    SubscribeToTariffSerializer
)


class BaseTariffView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    model = None
    serializer_class = None

    def get(self, request, *args, **kwargs):
        balance = request.user.balance
        queryset = self.model.objects.all().order_by("-days")
        data = {"data": self.serializer_class(queryset, many=True).data, "currentBalance": balance}
        return Response(data, status=200)


class TopView(BaseTariffView):
    model = Top
    serializer_class = TopSerializer


class AutoUPView(BaseTariffView):
    model = AutoUP
    serializer_class = AutoUPSerializer


class UrgentView(BaseTariffView):
    model = Urgent
    serializer_class = UrgentSerializer


class HighlightView(BaseTariffView):
    model = Highlight
    serializer_class = HighlightSerializer

from django.apps import apps

class SubscribeToTariffView(generics.GenericAPIView):
    def get_queryset(self):
        return None

    def get_serializer_class(self):
        return SubscribeToTariffSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj_table = serializer.validated_data["obj_table"]
        obj_id = serializer.validated_data["obj_id"]

        tariff_table = serializer.validated_data["tariff_table"]
        tariff_id = serializer.validated_data["tariff_id"]

        '''Получаем модель для obj_table'''
        model_dict = {
            'CarsPosts': 'cars_posts.CarsPosts',
            'Property': 'house.Property',
        }

        if obj_table not in model_dict:
            return Response(
                {
                    "response": False,
                    "message": f"Модель с именем {obj_table} не найдена."
                }
            )
        app_name, model_name = model_dict[obj_table].split('.')

        try:
            obj_model = apps.get_model(app_name, model_name)
        except LookupError:
            return Response(
                {"response": False, "message": f"Model {obj_table} not found."},
                status=400
            )

        '''Получаем объект по obj_id'''
        try:
            obj_instance = obj_model.objects.get(id=obj_id, user=user)
        except obj_model.DoesNotExist:
            return Response(
                {"response": False, "message": f"{obj_table} with ID {obj_id} not found."},
                status=404
            )

        '''Получаем модель для tariff_table'''
        try:
            tariff_model = apps.get_model("tariffs", tariff_table)
        except LookupError:
            return Response(
                {"response": False, "message": f"Model {tariff_table} not found."},
                status=400
            )

        '''Получаем объект тарифа по tariff_id'''
        try:
            tariff_instance = tariff_model.objects.get(id=tariff_id)
        except tariff_model.DoesNotExist:
            return Response(
                {"response": False, "message": f"{tariff_table} with ID {tariff_id} not found."},
                status=404
            )

        return Response(
            {
                "response": True,
                "message": f"{tariff_table} tariff has been successfully activated for {obj_table}",
                "obj_table": obj_table,
                "obj_id": obj_id,
                "tariff_table": tariff_table,
                "tariff_id": tariff_id,
                "obj_instance": str(obj_instance),  # Можно заменить на нужную информацию
                "tariff_instance": str(tariff_instance)  # Также можно изменить вывод
            }
        )