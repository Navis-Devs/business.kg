from rest_framework.generics import ListAPIView
from apps.tariffs import serializers
from apps.tariffs import models
from rest_framework import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView

class TarrifList(ListAPIView):
    queryset = models.Tariff.objects.all()
    serializer_class = serializers.TariffSerializers
    pagination_class = None

class ApplyTariffView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = serializers.ApplyTariffSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            instance = serializer.apply_tariff()
            return Response({
                "message": f"Тариф успешно применён. Он будет действовать до: {instance.id} дня.",
                'object_id': instance.id,
                # "status": response.status_code
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)