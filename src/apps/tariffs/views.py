from rest_framework.generics import ListAPIView
from apps.tariffs import serializers
from apps.tariffs import models
from rest_framework import response, permissions
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

class TarrifList(ListAPIView):
    queryset = models.Tariff.objects.all()
    serializer_class = serializers.TariffSerializers
    pagination_class = None


class ApplyTariffView(APIView):
    def post(self, request):
        serializer = serializers.ApplyTariffSerializer(data=request.data)
        
        if serializer.is_valid():
            property_instance = serializer.apply_tariff()
            return Response({
                'message': 'Тариф успешно применен.',
                'property_id': property_instance.id,
                'tariff_id': property_instance.product_id.id,
                'tariff_until': property_instance.tariff_untill,
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)